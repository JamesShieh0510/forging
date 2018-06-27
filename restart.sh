# export PATH=~/anaconda3/bin:$PATH
# conda create -y --name python36 python=3.6 
# #conda config --set show_channel_urls yes
source activate python36  
# pip install pandas
# pip install matplotlib
# pip install xlsxwriter
# pip install -U scikit-learn
# pip install scipy
# pip install ipython

#docker pull continuumio/anaconda3
#kill -9 $(lsof -t -i:8055)

npm install
npm start

#kill -9 $(lsof -t -i:8055) && nohup npm start  > /dev/null 2>&1 &
#curl 127.0.0.1:8055/start