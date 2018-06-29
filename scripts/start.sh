#cd /app/forging/
export PATH=~/anaconda3/bin:$PATH

touch /app/resolv.conf 
cat <<EOF | tee /app/resolv.conf 
search default.svc.cluster.local svc.cluster.local cluster.local
options ndots:5
nameserver 8.8.8.8
nameserver 8.8.4.4
EOF
cp /app/resolv.conf /etc/resolv.conf

conda create -y --name python36 python=3.6 
source activate python36  
activate python36 
cd /app/app/
npm install
npm start