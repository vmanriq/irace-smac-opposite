#!/usr/bin/python3

import argparse
import os
import sys
from subprocess import Popen, PIPE
    


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description='wrapper ga-nk')
    parser.add_argument('-cr', '--cr', action='store', dest='cr', nargs='+')
    parser.add_argument('-mr', '--mr', action='store', dest='mr')
    parser.add_argument('-ps', '--ps', action='store', dest='ps')

    args, unkown = parser.parse_known_args()
    instance = unkown[3]
    seed = unkown[2]
    co = '1'
    me='100000'
    temp_name = f"{args.cr[0]}_{args.mr}_{args.ps}_{seed}.dat"
    cmd = [os.path.expanduser('./ga-nk'), instance, temp_name, args.cr[0], args.mr, args.ps, me, seed, co ]
    io = Popen(cmd, stdout=PIPE)
    out_, err_ = io.communicate()
    with open(os.path.expanduser(temp_name), "r") as file:
        data = file.read().strip()
        evals = data.split(' ')[-1]
    os.remove(temp_name)
    print(evals)
    sys.exit(0)
    
