echo Pulling latest
git pull

echo Running Axel-Robot on Background
screen -dmS axelrobot sudo python3 ./robot01.py
