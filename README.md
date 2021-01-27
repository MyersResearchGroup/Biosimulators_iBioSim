# Biosimulators_iBioSim
BioSimulators-compliant command-line interface to the [iBioSim](https://github.com/MyersResearchGroup/iBioSim) simulation program.

## Contents
* [Installation](#installation)
* [Usage](#local-usage)
* [License](#license)
* [Development team](#development-team)
* [Questions and comments](#questions-and-comments)

## Installation
### Install Docker image
```
docker pull paytonco/ibiosim
```

## Local Usage
```
usage: iBioSim [-h] [-d] [-q] -i ARCHIVE [-o OUT_DIR] [--directory DIRECTORY]
               [-p PROPERTIES] [-ti INITTIME] [-tl LIMTIME] [-ot OUTTIME]
               [-pi PRINTINTERVAL] [-m0 MINSTEP] [-m1 MAXSTEP] [-aErr ABSERR]
               [-sErr RELERR] [-sd SEED] [-r RUNS] [-sim SIMULATION] [-v]
iBioSim: error: the following arguments are required: -i/--archive

C:\Users\payto\Biosimulators_iBioSim>docker run ibiosim -h
usage: iBioSim [-h] [-d] [-q] -i ARCHIVE [-o OUT_DIR] [--directory DIRECTORY]
               [-p PROPERTIES] [-ti INITTIME] [-tl LIMTIME] [-ot OUTTIME]
               [-pi PRINTINTERVAL] [-m0 MINSTEP] [-m1 MAXSTEP] [-aErr ABSERR]
               [-sErr RELERR] [-sd SEED] [-r RUNS] [-sim SIMULATION] [-v]

BioSimulatiors-compliant command-line interface to the iBioSim simulation program <https://github.com/MyersResearchGroup/iBioSim>.

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           full application debug mode
  -q, --quiet           suppress all console output
  -i ARCHIVE, --archive ARCHIVE
                        Arbitrary SBML, SED-ML, or Combine Archive file
  -o OUT_DIR, --out-dir OUT_DIR, -outDir OUT_DIR
                        Where the output should be stored
  --directory DIRECTORY
                        Project directory
  -p PROPERTIES, --properties PROPERTIES
                        Loads a properties file
  -ti INITTIME, --inittime INITTIME
                        Non-negative double initial simulation time
  -tl LIMTIME, --limtime LIMTIME
                        Non-negative double simulation time limit
  -ot OUTTIME, --outtime OUTTIME
                        Non-negative double output time
  -pi PRINTINTERVAL, --printinterval PRINTINTERVAL
                        Positive double for print interval
  -m0 MINSTEP, --minstep MINSTEP
                        Positive double for minimum step time
  -m1 MAXSTEP, --maxstep MAXSTEP
                        Positive double for maximum step time
  -aErr ABSERR, --abserr ABSERR
                        Positive double for absolute error
  -sErr RELERR, --relerr RELERR
                        Positive double for relative error
  -sd SEED, --seed SEED
                        Long for random seed
  -r RUNS, --runs RUNS  Positive integer for number of runs
  -sim SIMULATION, --simulation SIMULATION
                        Simulation type. Options are: ode, hode, ssa, hssa,
                        dfba, jode, jssa
  -v, --version         show program's version number and exit
```

## Usage Through Docker Container
```
docker run \
  --tty \
  --rm \
  --mount type=bind,source="$(pwd)"/tests/fixtures,target=/root/in \
  --mount type=bind,source="$(pwd)"/tests/results,target=/root/out \
  paytonco/ibiosim:latest \
    -i /root/in/BIOMD0000000297.omex \
    -o /root/out
```

## License
This package is released under the [Apache-2.0](License)

## Development Team
This package was developed by the [Genetic Logic Lab](https://myersresearchgroup.github.io/) at the University of Colorado Boulder.

## Questions and comments
Please contact the [Genetic Logic Lab](mailto:chris.myers@colorado.edu) with any questions or comments.


