#!/usr/bin/bash
if [ $(/usr/bin/id -u) -ne 0 ]; then
    echo "Requires root user access"
    exit
fi

# Make configurations folder
mkdir -pv /etc/psc
cp -r ./src/configs/. /etc/psc/.

# Add binaries
mkdir -pv /usr/bin/psc_
cp -r ./src/psc* /usr/bin/psc_/
ln -f /usr/bin/psc_/psc.py /usr/bin/psc 
chmod +x /usr/bin/psc