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
LABEL maintainer="Chris Myers <chris.myers@colorado.edu>"

# Install requirements
RUN apt-get update --fix-missing \
	&& DEBIAN_FRONTEND=noninteractive \
	   apt-get install -y maven
RUN apt-get install python3.7 -y \
	&& apt-get install python3-pip -y \
	&& pip3 install -U setuptools \
	&& apt install openjdk-8-jdk -y \
	&& apt install git -y \
	&& git clone https://github.com/MyersResearchGroup/iBioSim.git
WORKDIR ./iBioSim
RUN mvn package -Dmaven.javadoc.skip=true
WORKDIR ..
RUN apt-get -y install build-essential \
	&& apt-get -y install dos2unix \
	&& apt-get -y install libxml2-dev

# Copy code for command-line interface into image and install it
COPY . /root/Biosimulators_iBioSim
RUN python3.7 -m pip install /root/Biosimulators_iBioSim
	
WORKDIR root/Biosimulators_iBioSim/Dependencies
RUN chmod +x newbuild.sh \
	&& dos2unix newbuild.sh \
	&& sh newbuild.sh


# Entrypoint
ENTRYPOINT ["iBioSim"]
CMD []