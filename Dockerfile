# Base OS
FROM ubuntu:18.04

LABEL base_image="ubuntu:18.04"
LABEL version="1.0.0"
LABEL software="iBioSim"
LABEL software.version="3.1.0"
LABEL about.summary="CAD tool aimed for the modeling, analysis, and design of genetic circuits"
LABEL about.home="https://github.com/MyersResearchGroup/iBioSim"
LABEL about.documentation="https://github.com/MyersResearchGroup/iBioSim"
LABEL about.license_file="https://github.com/MyersResearchGroup/iBioSim/blob/master/LICENSE.txt"
LABEL about.license="Apache-2.0"
LABEL about.tags=""
LABEL extra.identifiers.biotools="ibiosim"
LABEL maintainer="Chris Myers <chris.myers@colorado.edu>"

# Install requirements
RUN echo no-cache1
RUN apt-get update --fix-missing

RUN apt-get install python3.7 -y

RUN apt-get install python3-pip -y

RUN pip3 install -U setuptools

#RUN pip3 install cement

RUN apt install openjdk-8-jdk -y	

RUN apt install maven -y 

RUN apt install git -y

RUN git clone https://github.com/MyersResearchGroup/iBioSim.git

RUN cd iBioSim \
	&& mvn package -Dmaven.javadoc.skip=true

# Copy code for command-line interface into image and install it
COPY . /root/Biosimulations_iBioSim
RUN python3.7 -m pip install /root/Biosimulations_iBioSim

#Installing reb2sac and GeneNet
RUN apt-get install libgsl-dev -y
RUN apt install gcc



# Entrypoint
ENTRYPOINT ["iBioSim"]
CMD []