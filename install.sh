sudo apt-get update

sudo apt-get upgrade

sudo apt-get dist-upgrede

sudo apt-get install -y build-essential tk-dev libncurses5-dev libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev zlib1g-dev libffi-dev libc6-dev libzbar-dev libzbar0 bluetooth libbluetooth-dev vim

wget https://www.python.org/ftp/python/3.6.6/Python-3.6.6.tgz

tar -zxvf Python-3.6.6.tgz

cd Python-3.6.6

./configure --prefix=/usr/local

sudo make

sudo make install

sudo pip3 install -U pip

sudo pip3 install -U setuptools

cd ..

sudo pip3 install pybluez beacontools datetime
