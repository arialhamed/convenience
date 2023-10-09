#!/bin/bash

notify-send "start.sh may require bio-authentication" "Check if fingerprint reader is glowing"

if sudo python3 -m keyring --disable
then notify-send "start.sh has been given authentication" "Script is running now"
else notify-send "Bio-authentication has failed" "Please try again by running start.sh in Unified"
fi

sh /media/ari/Unified/organize.sh

if sudo apt update && sudo apt upgrade -y && sudo snap refresh
then notify-send "System apt & snap updated by login script."
else notify-send "System apt & snap was not auto-updated by login script." "Check script, settings & internet connection." --urgency=critical
fi

if echo 85 | sudo tee /sys/class/power_supply/BAT0/charge_stop_threshold
then notify-send "Charge stop threshold is set to 85% by login script."
else notify-send "Charge stop threshold is NOT set." "Battery is not connected" --urgency=critical
fi

if echo 75 | sudo tee /sys/class/power_supply/BAT0/charge_start_threshold
then notify-send "Charge start threshold is set to 75% by login script."
else notify-send "Charge start threshold is NOT set." "Battery is not connected" --urgency=critical
fi

if java -jar /media/ari/Unified/AppImages/ripme.jar -u https://reddit.com/r/thinkpad
then notify-send "Refresh ripping r/thinkpad successful"
else notify-send "RipMe has failed" "Please check connection or output directory"
fi
