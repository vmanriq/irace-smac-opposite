import argparse
import os
__copyright__ = "Copyright 2021, AutoML.org Freiburg-Hannover"
__license__ = "3-clause BSD"

from subprocess import Popen, PIPE
    


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='wrapper ga-nk')
    parser.add_argument('-cr', '--cr', action='store', dest='cr')
    parser.add_argument('-mr', '--mr', action='store', dest='mr')
    parser.add_argument('-ps', '--ps', action='store', dest='ps')

    args, unkown = parser.parse_known_args()
    instance = unkown[0]
    seed = unkown[-1]
    co = '1'
    me='100000'
    temp_name = f"{args.cr}_{args.mr}_{args.ps}_{seed}.dat"
    cmd = ['./target_algorithm/ga-nk', instance, temp_name, args.cr, args.mr, args.ps, me, seed, co ]
    io = Popen(cmd, stdout=PIPE)
    out_, err_ = io.communicate()
    with open(temp_name, "r") as file:
        data = file.read().strip()
        evals = data.split(' ')[-1]
    os.remove(temp_name)
    print(f"Result for SMAC: SUCCESS, -1, -1, {evals}, {seed}")
    
