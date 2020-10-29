""" BioSimulators-compliant command-line interface to the `iBioSim <https://github.com/MyersResearchGroup/iBioSim>`_ simulation program.

:Author: Myers Research Group <chris.myers@colorado.edu>
:Date: 2020-06-12
:Copyright: 2020
:License: Apache-2.0
"""

from .core import exec_combine_archive
import Biosimulators_iBioSim
import cement


class BaseController(cement.Controller):
    """ Base controller for command line application """

    class Meta:
        label = 'base'
        description = ("BioSimulatiors-compliant command-line interface to the "
                       "iBioSim simulation program <https://github.com/MyersResearchGroup/iBioSim>.")
        help = "iBioSim"
        arguments = [
            (['-i', '--archive'], dict(type=str,
                                       required=True,
                                       help='Path to OMEX file which contains one or more SED-ML-encoded simulation experiments')),
            (['-o', '--out-dir'], dict(type=str,
                                       default='.',
                                       help='Directory to save outputs')),
            (['-v', '--version'], dict(action='version',
                                       version=Biosimulators_iBioSim.__version__)),
        ]

    @cement.ex(hide=True)
    def _default(self):
        args = self.app.pargs
        exec_combine_archive(args.archive, args.out_dir)


class App(cement.App):
    """ Command line application """
    class Meta:
        label = 'iBioSim'
        base_controller = 'base'
        handlers = [
            BaseController,
        ]


def main():
    with App() as app:
        app.run()
