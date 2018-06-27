FROM continuumio/anaconda3:5.1.0
# set the base image

# author
MAINTAINER James Shieh <p96044168@student.ncku.edu.tw>

# extra metadata
LABEL version="1.0.0"
LABEL description="Container Based Image For Forging Modules"


# install app runtimes and modules
RUN apt-get update
RUN apt-get install -y r-base
RUN apt-get install -y curl

RUN curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
RUN bash nodesource_setup.sh
RUN apt-get install -y nodejs
RUN apt-get install -y npm

#sudo curl -sL https://deb.nodesource.com/setup_8.x -o nodesource_setup.sh
#sudo bash nodesource_setup.sh
#sudo apt-get install -y nodejs && sudo apt-get install -y npm

RUN export PATH=~/anaconda3/bin:$PATH
RUN conda create -y --name python36 python=3.6 
#RUN source activate python36  
RUN pip install pandas
RUN pip install matplotlib
RUN pip install xlsxwriter
RUN pip install -U scikit-learn
RUN pip install scipy
RUN pip install ipython

RUN mkdir /app
ADD ./application-source-code/ /app

EXPOSE 8055
# COPY ./application-source-code/forging/restart.sh /app/restart.sh
# ENTRYPOINT ["sh","/app/forging/restart.sh"]
