#cd /app/forging/
export PATH=~/anaconda3/bin:$PATH
conda create -y --name python36 python=3.6 
source activate python36  
npm install
npm start