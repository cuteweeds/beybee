import gc

import adafruit_displayio_ssd1306
import displayio
import terminalio
from adafruit_display_text import label

from kmk.extensions import Extension

def init_display(i2c):
    display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
    display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=32)

    # Make the display context
    splash = displayio.Group()
    display.show(splash)

    color_bitmap = displayio.Bitmap(128, 32, 1)
    color_palette = displayio.Palette(1)
    color_palette[0] = 0xFFFFFF  # White

    bg_sprite = displayio.TileGrid(color_bitmap, pixel_shader=color_palette, x=0, y=0)
    splash.append(bg_sprite)

    # Draw a smaller inner rectangle
    inner_bitmap = displayio.Bitmap(118, 24, 1)
    inner_palette = displayio.Palette(1)
    inner_palette[0] = 0x000000  # Black
    inner_sprite = displayio.TileGrid(inner_bitmap, pixel_shader=inner_palette, x=5, y=4)
    splash.append(inner_sprite)

    # Draw a label
    text = "Hello World!"
    text_area = label.Label(terminalio.FONT, text=text, color=0xFFFF00, x=28, y=15)
    splash.append(text_area)

class OledDisplayMode:
    TXT = 0
    IMG = 1


class OledReactionType:
    STATIC = 0
    LAYER = 1


class OledData:
    def __init__(
        self,
        image=None,
        corner_one=None,
        corner_two=None,
        corner_three=None,
        corner_four=None,
    ):
        if image:
            self.data = [image]
        elif corner_one and corner_two and corner_three and corner_four:
            self.data = [corner_one, corner_two, corner_three, corner_four]

# Peg Oled display extension, modified to accept I2C objects passed in.
# This is because it seems that I2C objects cannot be instantiated multiple times,
# and must be passed around.
class Oled(Extension):
    def __init__(
        self,
        i2c,
        views,
        toDisplay=OledDisplayMode.TXT,
        oWidth=128,
        oHeight=32,
        flip: bool = False,
    ):
        displayio.release_displays()
        self.rotation = 180 if flip else 0
        self._views = views.data
        self._toDisplay = toDisplay
        self._width = oWidth
        self._height = oHeight
        self._prevLayers = 0
        self._i2c = i2c
        gc.collect()

    def returnCurrectRenderText(self, layer, singleView):
        # for now we only have static things and react to layers. But when we react to battery % and wpm we can handle the logic here
        if singleView[0] == OledReactionType.STATIC:
            return singleView[1][0]
        if singleView[0] == OledReactionType.LAYER:
            return singleView[1][layer]

    def renderOledTextLayer(self, layer):
        splash = displayio.Group()
        self._display.show(splash)
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[0]),
                color=0xFFFFFF,
                x=0,
                y=10,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[1]),
                color=0xFFFFFF,
                x=64,
                y=10,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[2]),
                color=0xFFFFFF,
                x=0,
                y=25,
            )
        )
        splash.append(
            label.Label(
                terminalio.FONT,
                text=self.returnCurrectRenderText(layer, self._views[3]),
                color=0xFFFFFF,
                x=64,
                y=25,
            )
        )
        gc.collect()

    def renderOledImgLayer(self, layer):
        splash = displayio.Group()
        self._display.show(splash)
        odb = displayio.OnDiskBitmap(
            '/' + self.returnCurrectRenderText(layer, self._views[0])
        )
        image = displayio.TileGrid(odb, pixel_shader=odb.pixel_shader)
        splash.append(image)
        gc.collect()

    def updateOLED(self, sandbox):
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(sandbox.active_layers[0])
        if self._toDisplay == OledDisplayMode.IMG:
            self.renderOledImgLayer(sandbox.active_layers[0])
        gc.collect()

    def on_runtime_enable(self, sandbox):
        return

    def on_runtime_disable(self, sandbox):
        return

    def during_bootup(self, board):
        displayio.release_displays()
        self._display = adafruit_displayio_ssd1306.SSD1306(
            displayio.I2CDisplay(self._i2c, device_address=0x3C),
            width=self._width,
            height=self._height,
            rotation=self.rotation,
        )
        if self._toDisplay == OledDisplayMode.TXT:
            self.renderOledTextLayer(0)
        if self._toDisplay == OledDisplayMode.IMG:
            self.renderOledImgLayer(0)
        return

    def before_matrix_scan(self, sandbox):
        if sandbox.active_layers[0] != self._prevLayers:
            self._prevLayers = sandbox.active_layers[0]
            self.updateOLED(sandbox)
        return

    def after_matrix_scan(self, sandbox):

        return

    def before_hid_send(self, sandbox):
        return

    def after_hid_send(self, sandbox):
        return

    def on_powersave_enable(self, sandbox):
        return

    def on_powersave_disable(self, sandbox):
        return
