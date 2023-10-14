#!/usr/bin/env bash

# This is script is for whenever I need to reinstall Ubuntu from fresh. This script will take care of almost everything while it installs everything that I personally need
# Works in Linux

echo -e "\n--- Ari's Ubuntu 22.04 Setup Script ---"
cd

echo -e "\nEssential apt & snap update/refresh"
sudo apt update
sudo apt upgrade -y
sudo snap refresh

echo -e "\nInstalling all packages recommended by Ari"
sudo apt install --no-install-recommends wine lm-sensors ffmpeg git gh asciinema adb openscad apksigner qbittorrent hwinfo powertop powerstat fancontrol traceroute tint quadrapassel gnome-disk-utility gdebi gedit steam vlc obs-studio krita inkscape telegram-desktop kamoso kdenlive imagemagick baobab tlp tlp-rdw apktool plasma-workspace-wayland cmake qt5-qmake flatpak audacity hw-probe blender virtualbox freecad libnotify-bin python3-pip default-jre default-jdk software-properties-common gimp meshlab nmap net-tools bible-kjv docker.io acpi pv neofetch zpaq torbrowser-launcher npm fprintd libpam-fprintd w3m w3m-img xautomation r-base-core d1x-rebirth d2x-rebirth curl ca-certificates libxext-dev clang gcc python3.10-venv nomacs heif-gdk-pixbuf heif-thumbnailer qt6-base-dev qt6-base-private-dev libqt6svg6-dev make g++ pkg-config libavcodec-dev libavformat-dev libavutil-dev libswscale-dev easytag libxi-dev libxrandr-dev libudev-dev libevdev-dev libsfml-dev libminiupnpc-dev libmbedtls-dev libcurl4-openssl-dev libhidapi-dev libsystemd-dev libbluetooth-dev libasound2-dev libpulse-dev libpugixml-dev libbz2-dev libzstd-dev liblzo2-dev libpng-dev libusb-1.0-0-dev gettext python3-pyqt5.qtsvg img2pdf gifsicle jstest-gtk supertuxkart php-common libapache2-mod-php php-cli composer dos2unix edid-decode mediainfo frei0r-plugins qdirstat gcc-arm-none-eabi binutils-arm-none-eabi build-essential autoconf automake libgtk2.0-dev libglu1-mesa-dev libsdl1.2-dev libglade2-dev zlib1g-dev libosmesa6-dev intltool libagg-dev libsoundtouch-dev libpcap-dev texinfo mkvtoolnix -y

echo -e "\nRemoving KTorrent, GwenView & GIMP (replaced with QBitTorrent, Nomacs & Inkscape)"
sudo apt remove ktorrent gwenview gimp -y

echo -e "\nInstalling AIMP"
wget `curl -Ls -o /dev/null -w %{url_effective} "https://www.aimp.ru/?do=download.file&id=26"` && sudo dpkg --install --force-depends aimp*.deb

echo -e "\nInstalling Discord"
wget `curl -Ls -o /dev/null -w %{url_effective} "https://discord.com/api/download?platform=linux&format=deb"` && sudo dpkg --install --force-depends discord*.deb

echo -e "\nInstalling Minecraft"
wget https://launcher.mojang.com/download/Minecraft.deb && sudo dpkg --install --force-depends Minecraft.deb && rm *.deb

echo -e "\nInstalling Grabber"
sudo flatpak install https://dl.flathub.org/repo/appstream/org.bionus.Grabber.flatpakref -y

echo -e "\Installing PPSSPP"
sudo flatpak install flathub org.ppsspp.PPSSPP -y

echo -e "\nInstalling melonDS"
sudo flatpak install flathub net.kuribo64.melonDS -y

echo -e "\nInstalling xemu"
sudo flatpak install -y app.xemu.xemu

echo -e "\nInstalling snaps"
sudo snap install pdftk zoom-client openjdk gzdoom yt-dlg dolphin-emulator mgba
sudo snap install sublime-text --classic
sudo snap install android-studio --classic
sudo snap install flutter --classic

echo -e "\nInstalling Rust"
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

mkdir .local/bin
export PATH="$HOME/.local/bin:$PATH"

echo -e "\nEnabling tlp.service"
sudo systemctl enable tlp.service

# Aliases
echo -e "\nInserting aliases into ~/.bashrc"
echo "alias orange='sudo python3 -m Orange.canvas --no-sandbox &'" >> ~/.bashrc
echo "alias citra='flatpak run org.citra_emu.citra'" >> ~/.bashrc
echo "alias ripme='java -jar ~/ripme.jar -u'" >> ~/.bashrc
echo "alias yt='~/yt-dlp'" >> ~/.bashrc
echo "alias desmume='~/desmume'" >> ~/.bashrc
echo "alias hori='jstest-gtk'" >> ~/.bashrc
echo "alias gzdoom='gzdoom -file'" >> ~/.bashrc
echo "alias update='sudo apt update ; sudo apt upgrade -y ; sudo apt autoremove -y ; sudo snap refresh'" >> ~/.bashrc
echo "alias {find100M,find100m}='f(){ find \"\$@\" -type f -size +100M ; unset -f f; }; f'" >> ~/.bashrc
echo "alias editbash='nano ~/.bashrc'" >> ~/.bashrc
echo "alias {rekonsole,rek}='(sleep .1 ; konsole) & exit'" >> ~/.bashrc
echo "alias stfu='shutdown -P 0'" >> ~/.bashrc
echo "alias kill='f(){ kill -9 \$(ps -x | grep \"\$@\") ;  unset -f f; }; f'" >> ~/.bashrc
echo "alias nano='nano --tabsize=4 --constantshow --softwrap --atblanks --autoindent --smarthome --cutfromcursor'" >> ~/.bashrc
echo "alias watch='watch -n .5'" >> ~/.bashrc
echo "alias cp2='rsync -aP'" >> ~/.bashrc
echo "alias mv2='rsync -aP --remove-source-files'" >> ~/.bashrc
echo "alias neofetch='neofetch --ascii_distro Kubuntu'" >> ~/.bashrc
echo "alias python='python3'" >> ~/.bashrc
echo "alias hw-probe='sudo -E hw-probe --all --upload'" >> ~/.bashrc
echo "alias grabber='flatpak run org.bionus.Grabber --filename \"%search%/%date:format=yyyy-MM-dd%_%md5%.%ext%\"'" >> ~/.bashrc
echo "alias melon='flatpak run net.kuribo64.melonDS'" >> ~/.bashrc
echo "alias {psp,ppsspp}='flatpak run org.ppsspp.PPSSPP'" >> ~/.bashrc
echo "alias xemu='flatpak run app.xemu.xemu'" >> ~/.bashrc

echo -e "\nCreating Battery Threshold script"
sudo touch /usr/bin/batterythreshold.sh
sudo echo "!/bin/bash" >> /usr/bin/batterythreshold.sh
sudo echo "echo 85 | tee /sys/class/power_supply/BAT0/charge_stop_threshold" >> /usr/bin/batterythreshold.sh
sudo echo "echo 75 | tee /sys/class/power_supply/BAT0/charge_start_threshold" >> /usr/bin/batterythreshold.sh

echo -e "\nCreating Battery Threshold service"
sudo touch /etc/systemd/system/batterythreshold.service
sudo echo "[Unit]" >> /etc/systemd/system/batterythreshold.service
sudo echo "Description=Battery Threshold service" >> /etc/systemd/system/batterythreshold.service
sudo echo "" >> /etc/systemd/system/batterythreshold.service
sudo echo "[Service]" >> /etc/systemd/system/batterythreshold.service
sudo echo "Type=simple" >> /etc/systemd/system/batterythreshold.service
sudo echo "User=root" >> /etc/systemd/system/batterythreshold.service
sudo echo "Group=root" >> /etc/systemd/system/batterythreshold.service
sudo echo "TimeoutStartSec=0" >> /etc/systemd/system/batterythreshold.service
sudo echo "Restart=on-failure" >> /etc/systemd/system/batterythreshold.service
sudo echo "RestartSec=30s" >> /etc/systemd/system/batterythreshold.service
sudo echo "#ExecStartPre=" >> /etc/systemd/system/batterythreshold.service
sudo echo "ExecStart=/usr/bin/batterythreshold.sh" >> /etc/systemd/system/batterythreshold.service
sudo echo "SyslogIdentifier=Diskutilization" >> /etc/systemd/system/batterythreshold.service
sudo echo "#ExecStop=" >> /etc/systemd/system/batterythreshold.service
sudo echo "" >> /etc/systemd/system/batterythreshold.service
sudo echo "[Install]" >> /etc/systemd/system/batterythreshold.service
sudo echo "WantedBy=multi-user.target" >> /etc/systemd/system/batterythreshold.service

sudo systemctl start batterythreshold.service
sudo systemctl enable batterythreshold.service

# CONSIDER implementing a way to detect desktop environment, this script is meant for KDE (Kubuntu)

# Restarting system
sudo apt update; sudo apt upgrade -y; sudo apt autoremove -y; sudo snap refresh
reboot
