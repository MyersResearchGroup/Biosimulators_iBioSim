""" Methods for executing SED tasks in COMBINE archives and saving their outputs

:Author: Myers Research Group. chris.myers@colorado.edu
:Date: 2020-06-12
:Copyright: 2020
:License: Apache-2.0
"""

import os


__all__ = ['exec_combine_archive']


def exec_combine_archive(archive_file, out_dir):
    """ Execute the SED tasks defined in a COMBINE archive and save the outputs

    Args:
        archive_file (:obj:`str`): path to COMBINE archive
        out_dir (:obj:`str`): directory to store the outputs of the tasks
    """
    cmd = r"java -jar /iBioSim/analysis/target/iBioSim-analysis-3.1.0-SNAPSHOT-jar-with-dependencies.jar -sim jode "
    os.system(cmd+archive_file)
