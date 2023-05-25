SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR

if [[ $(pwd) == '/Users/litdistco/Desktop/MyLife/dev/hardware/beybee/firmware/numpad' ]]; then
	read -p "Write numpad firmware to CIRCUITPY device? (y/n) " yn
	case $yn in
		[Yy]* )
			echo "This will take a few moments…"
			cp -R * /Volumes/CIRCUITPY
			;;
		[Nn]* )
			exit	
	esac
fi