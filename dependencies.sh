#/bin/sh
sudo apt install python3 -s
sudo apt install python3-virtualenv -s
sudo apt install python3-tk -s
virtualenv venv
source venv/bin/activate
pip3 install beautifulsoup4
pip3 install urllib3

