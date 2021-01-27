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
                                       help='Arbitrary SBML, SED-ML, or Combine Archive file')),
            (['-o', '--out-dir', '-outDir'], dict(type=str,
                                       default='.',
                                       help='Where the output should be stored')),
            (['--directory'], dict(type=str,
                                       required=False,
                                       help='Project directory')),
            (['-p', '--properties'], dict(type=str,
                                       required=False,
                                       help='Loads a properties file')),
            (['-ti', '--inittime'], dict(type=str,
                                       required=False,
                                       help='Non-negative double initial simulation time')),
            (['-tl', '--limtime'], dict(type=str,
                                       required=False,
                                       help='Non-negative double simulation time limit')),
            (['-ot', '--outtime'], dict(type=str,
                                       required=False,
                                       help='Non-negative double output time')),
            (['-pi', '--printinterval'], dict(type=str,
                                       required=False,
                                       help='Positive double for print interval')),
            (['-m0', '--minstep'], dict(type=str,
                                       required=False,
                                       help='Positive double for minimum step time')),
            (['-m1', '--maxstep'], dict(type=str,
                                       required=False,
                                       help='Positive double for maximum step time')),
            (['-aErr', '--abserr'], dict(type=str,
                                       required=False,
                                       help='Positive double for absolute error')),
            (['-sErr', '--relerr'], dict(type=str,
                                       required=False,
                                       help='Positive double for relative error')),
            (['-sd', '--seed'], dict(type=str,
                                       required=False,
                                       help='Long for random seed')),
            (['-r', '--runs'], dict(type=str,
                                       required=False,
                                       help='Positive integer for number of runs')),
            (['-sim', '--simulation'], dict(type=str,
                                       required=False,
                                       help='Simulation type. Options are: ode, hode, ssa, hssa, dfba, jode, jssa')),
            (['-v', '--version'], dict(action='version',
                                       version=Biosimulators_iBioSim.__version__)),
        ]

    @cement.ex(hide=True)
    def _default(self):
        args = self.app.pargs
        exec_combine_archive(args.archive, args.out_dir, args.directory, args.properties, args.inittime, args.limtime, args.outtime, args.printinterval, args.minstep, args.maxstep, args.abserr, args.relerr, args.seed, args.runs, args.simulation)


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