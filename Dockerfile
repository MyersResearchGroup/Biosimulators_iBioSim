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
LABEL about.tags="kinetic modeling,dynamical simulation,systems biology,biochemical networks,SBML,SED-ML,COMBINE,OMEX,BioSimulators"
LABEL extra.identifiers.biotools="ibiosim"
LABEL maintainer="Chris Myers <chris.myers@colorado.edu>"

# Install requirements
RUN apt-get update --fix-missing \
	&& apt-get install python3.7 -y \
	&& apt-get install python3-pip -y \
	&& pip3 install -U setuptools \
	&& pip3 install python-libsbml

RUN apt install openjdk-8-jdk -y \
	&& apt install maven -y \
	&& apt install git -y \
	&& git clone https://github.com/MyersResearchGroup/iBioSim.git 

RUN cd iBioSim \
	&& mvn package -Dmaven.javadoc.skip=true

# Copy code for command-line interface into image and install it
COPY . /root/Biosimulators_iBioSim
RUN python3.7 -m pip install /root/Biosimulators_iBioSim

#Installing reb2sac and GeneNet
#need to compile reb2sac outside of image and copy it in 

# Entrypoint
ENTRYPOINT ["iBioSim"]
CMD []
