#!/bin/bash
if [ "$EUID" -ne 0 ]
  then echo "Please run as root"
  exit
fi

echo "Updating repositories:"
sudo apt update
echo ""

echo "Installing Git:"
sudo apt install git -y
echo ""

echo "Downloading the module:"
sudo rm -r /usr/lib/python3/dist-packages/odoo/addons/journals_audit_enabler
sudo git clone https://github.com/FherStk/journals_audit_enabler.git /usr/lib/python3/dist-packages/odoo/addons/journals_audit_enabler
echo ""

echo "Installing the module:"
sudo service odoo restart
echo ""

echo "The module has been succesfully added to Odoo. Please, refresh the app list and install it manually."
