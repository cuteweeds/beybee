#mdutil -i off /Volumes/RPI-RP2
#mdutil -i off /Volumes/CIRCUITPY


#SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

#cd /Volumes/RPI-RP2
#if [[ $(pwd) == "/Volumes/RPI-RP2" ]]; then
#	echo 'Bare RPI device detected' ; else
#	echo 'Error: RPI device not detected' ; exit ; fi


### NOTES
# ask to nuke //cp
# ask to nuke //rp
# do that
# wait for reconnect
# flash cp tp rp
# ask to install full version of kmk

echo 'Attempting to put device in Bootsel mode.'
stty -f /dev/cu.usbmodem1101 1200 2> /dev/null
read -p "Press ENTER to confirm RPI-RP2 is connected…"
read -p "Reset /Volumes/RPI-RP2? (y/n) " yn 
case $yn in 
	[Yy]* ) 
		echo 'Resetting device…' 
		cp -x 'flash_nuke.uf2' /Volumes/RPI-RP2 2> /dev/null
		;; 
	[Nn]* ) 
		echo 'Cancelling operation' & echo
		exit 
		;;
	* ) 
		echo "Cancelling operation" & echo
		exit 
		;;
esac

read -p "Press ENTER when RPI-RP2 is connected…"
echo "Please wait a few moments for installation to complete. RPI-RP2 will disconnect when complete, and CIRCUITPY will connect a moment later."
cp -x 'adafruit-circuitpython-seeeduino_xiao_rp2040-en_US-8.0.4.uf2' /Volumes/RPI-RP2 2> /dev/null


read -p "Press ENTER when CIRCUITPY is connected…"
echo "Install full version of KMK?"
read -p "Note: some specific builds include lightweight kmk installs and don't require full version. Install? (y/n) " yn
case $yn in
	[Yy]* ) 
		echo 'Copying KMK firmware…'
		mkdir /Volumes/CIRCUITPY/kmk & echo
		cp boot.py /Volumes/CIRCUITPY 2> /dev/null
		cp -r kmk-FULL/* /Volumes/CIRCUITPY/kmk
		;;
	[Nn]* ) 
		echo 'Operation complete.' 
		exit 
		;;
	* ) 
		echo 'Operation complete.' 
		exit 
		;;
esac