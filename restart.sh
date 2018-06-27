export PATH=~/anaconda3/bin:$PATH
conda create --name python36 python=3.6 
#conda config --set show_channel_urls yes
source activate python36  
#pip install pandas
#pip install matplotlib
#pip install xlsxwriter
#pip install -U scikit-learn
#docker pull continuumio/anaconda3
kill -9 $(lsof -t -i:8055)

npm install
npm start