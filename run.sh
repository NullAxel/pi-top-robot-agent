echo Pulling latest
git pull

echo Running Axel-Robot on Background


export ANVIL_TOKEN="CHANGEME"
sudo python3 ./robot01.py
