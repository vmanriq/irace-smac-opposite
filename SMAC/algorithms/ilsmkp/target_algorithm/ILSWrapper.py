import sys

__copyright__ = "Copyright 2021, AutoML.org Freiburg-Hannover"
__license__ = "3-clause BSD"

from subprocess import Popen, PIPE

"""
This is a wrapper used by SMAC to optimize parameters on the branin-function.

To run this example, execute:
    $ cd examples/quickstart/branin
    $ python3 ../../scripts/smac --scenario scenario.txt

We optimize the branin-function (see "examples/quickstart/branin/branin.py").

To use the commandline, we need two files:
- a scenario-file: located in "examples/quickstart/branin/scenario.txt"
                   specifies SMAC-parameters, e.g. runtime, output, etc.
- a pcs-file:      located in "examples/quickstart/branin/param_config_space.pcs"
                   specifies the parameter configuration space (here: x1, x2)

SMAC calls this wrapper during optimization, because it is specified in the
"algo"-parameter of the scenario-file.
SMAC calls this file via the commandline, passing information in additional
commandline-arguments.
The target algorithm parameters (here: x1, x2) are also passed as
commandline-arguments.
A full call by SMAC looks like this:
    <algo>           <instance> <instance specific> <cutoff time>  <runlength> <seed> <algorithm parameters>
    python3 branin.py 0          0                   99999999999999 0           12345  -x1 0 -x2 0

SMAC processes results from the commandline, therefore the print-statement is
crucial. The format of the results must be:
    Result for SMAC: <STATUS>, <runtime>, <runlength>, <quality>, <seed>, <instance-specifics>
"""


if __name__ == '__main__':
    # Unused in this example:
    # instance, instance_specific, cutoff, runlength = sys.argv[1:5]
    instance = sys.argv[1]
    seed = sys.argv[5]
    #argv 6 es el nombre del param
    k = sys.argv[7]
    TOTAL_EVAL = '3000'
    cmd = ['./target_algorithm/ILSMKP', instance, seed, TOTAL_EVAL ,k]
    io = Popen(cmd, stdout=PIPE)
    out_, err_ = io.communicate()
    result = out_.decode("utf-8").strip()
    print(f"Result for SMAC: SUCCESS, -1, -1, {result}, {seed}")