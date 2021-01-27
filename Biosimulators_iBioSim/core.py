""" Methods for executing SED tasks in COMBINE archives and saving their outputs

:Author: Myers Research Group <chris.myers@colorado.edu>
:Date: 2020-06-12
:Copyright: 2020
:License: Apache-2.0
"""

import os
#import zipfile
import shutil

__all__ = ['exec_combine_archive']

def exec_combine_archive(archive_file, out_dir, directory, properties, inittime, limtime, outtime, printinterval, minstep, maxstep, abserr, relerr, seed, runs, simulation):
    """ Execute the SED tasks defined in a COMBINE archive and save the outputs

    Args:
        archive_file (:obj:`str`): path to COMBINE archive
        out_dir (:obj:`str`): directory to store the outputs of the tasks
    """
    
    os.environ["BIOSIM"] = "/iBioSim"
    os.environ["PATH"] = os.environ["BIOSIM"]+r"/bin:"+os.environ["BIOSIM"]+r"/lib:"+os.environ["PATH"]
    os.environ["LD_LIBRARY_PATH"] = os.environ["BIOSIM"] + r"/lib:"
    
    if not os.path.isfile(archive_file):
        raise FileNotFoundError("File does not exist: {}".format(archive_file))
        
    '''if not zipfile.is_zipfile(archive_file):
        raise IOError("File is not an OMEX Combine Archive in zip format: {}".format(archive_file))'''
        
    cmd = r"java -jar /iBioSim/analysis/target/iBioSim-analysis-3.1.0-SNAPSHOT-jar-with-dependencies.jar " #hode sim is java based
    if not directory is None:
        cmd += "-d " + directory
    if not properties is None:
        cmd += "-p " + properties
    if not inittime is None:
        cmd += "-ti " + inittime
    if not limtime is None:
        cmd += "-tl " + limtime
    if not outtime is None:
        cmd += "-ot " + outtime
    if not printinterval is None:
        cmd += "-pi " + printinterval
    if not minstep is None:
        cmd += "-m0 " + minstep
    if not maxstep is None:
        cmd += "-m1 " + maxstep
    if not abserr is None:
        cmd += "-aErr " + abserr
    if not relerr is None:
        cmd += "-sErr " + relerr
    if not seed is None:
        cmd += "-sd " + seed
    if not runs is None:
        cmd += "-r " + runs
    if not simulation is None:
        cmd += "-sim "  + simulation
           
    os.system(cmd+" "+archive_file)
    shutil.move(archive_file.rsplit('.',1)[0],out_dir)
    