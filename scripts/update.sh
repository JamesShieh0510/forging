WORKPATH=$(pwd)
cd /home/autolab/volume/
rm -rf ./forging
git clone https://github.com/JamesShieh0510/forging.git
cp ./forging/scripts/start.sh /home/autolab/volume/forging/
chmod 777 /home/autolab/volume/forging/start.sh
cd $WORKPATH

#start-bpm-service.sh
