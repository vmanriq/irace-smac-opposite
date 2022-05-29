#!/usr/bin/python3

import sys
import argparse
import os
import re
__copyright__ = "Copyright 2021, AutoML.org Freiburg-Hannover"
__license__ = "3-clause BSD"

from subprocess import Popen, PIPE


def get_optimum(instance):
    all_opts = {'a280': 2579, 'ali535': 202310, 'att48': 10628,
                'att532': 27686, 'bayg29': 1610, 'bays29': 2020, 'berlin52': 7542, 'bier127': 118282,
                'brazil58': 25395, 'brg180': 1950, 'burma14': 3323, 'ch130': 6110, 'ch150': 6528, 'd198': 15780,
                'd493': 35002, 'd657': 48912, 'd1291': 50801, 'd1655': 62128, 'dantzig42': 699, 'dsj1000': 18659688, 
                'eil51': 426, 'eil76': 538, 'eil101': 629, 'fl417': 11861, 'fl1400': 20127, 'fnl4461': 182566, 'fri26': 937,
                'gil262': 2378, 'gr17': 2085, 'gr21': 2707, 'gr24': 1272, 'gr48': 5046, 'gr96': 55209, 'gr120': 6942, 'gr137': 69853,
                'gr202': 40160, 'gr229': 134602, 'gr431': 171414, 'gr666': 294358, 'hk48': 11461, 'kroA100': 21282, 'kroB100': 22141,
                'kroC100': 20749, 'kroD100': 21294, 'kroE100': 22068, 'kroA150': 26524, 'kroB150': 26130, 'kroA200': 29368, 'kroB200': 29437,
                'lin105': 14379, 'lin318': 42029, 'linhp318': 41345, 'nrw1379': 56638, 'p654': 34643, 'pa561': 2763, 'pcb442': 50778, 'pcb1173': 56892,
                'pcb3038': 137694, 'pla7397': 23260728, 'pr76': 108159, 'pr107': 44303, 'pr124': 59030, 'pr136': 96772, 'pr144': 58537,
                'pr152': 73682, 'pr226': 80369, 'pr264': 49135, 'pr299': 48191, 'pr439': 107217, 'pr1002': 259045, 'pr2392': 378032, 
                'rat99': 1211, 'rat195': 2323, 'rat575': 6773, 'rat783': 8806, 'rd100': 7910, 'rd400': 15281, 'rl1304': 252948, 'rl1323': 270199, 
                'rl1889': 316536, 'si535': 48450, 'si1032': 92650, 'st70': 675, 'swiss42': 1273, 'ts225': 126643, 'tsp225': 3919, 'u159': 42080,
                'u574': 36905, 'u724': 41910, 'u1060': 224094, 'u1423': 152970, 'u1817': 57201, 'u2152': 64253, 'u2319': 234256, 'ulysses16': 6859,
                'ulysses22': 7013, 'vm1084': 239297, 'vm1748': 336556, 'sii175': 21407 }
    instance_name = instance.split('/')[-1].split('.')[0]
    return all_opts[instance_name]
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='wrapper acotsp')
    parser.add_argument('-algorithm', '--algorithm', action='store', dest='algorithm')
    parser.add_argument('-ls', '--ls', action='store', dest='ls')
    parser.add_argument('-alpha', '--alpha', action='store', dest='alpha')
    parser.add_argument('-beta', '--beta', action='store', dest='beta')
    parser.add_argument('-rho', '--rho', action='store', dest='rho')
    parser.add_argument('-ants', '--ants', action='store', dest='ants')
    parser.add_argument('-nnls', '--nnls', action='store', dest='nnls')
    parser.add_argument('-q0', '--q0', action='store', dest='q0')
    parser.add_argument('-dlb', '--dlb', action='store', dest='dlb')
    parser.add_argument('-rasranks', '--rasranks', action='store', dest='rasranks')
    parser.add_argument('-elitistants', '--elitistants', action='store', dest='elitistants')

    args, unkown = parser.parse_known_args()
    instance = unkown[3]
    seed = unkown[2]
    instance_opt = get_optimum(instance)
    arguments_to_call = ['-r', '1', '--seed', seed, '-i', instance, '-o', str(instance_opt), '--quiet', '--tours', '10000']
    all_arguments = ['algorithm', 'ls', 'alpha', 'beta', 'rho', 'ants', 'nnls', 'q0', 'dlb', 'rasranks', 'elitistants']
    for argument in all_arguments:
        value = getattr(args, argument)
        if value == None: continue

        if argument == 'algorithm':
            arguments_to_call.append(f"--{value}")
        else:
            arguments_to_call.append(f"--{argument}")
            arguments_to_call.append(value)


    cmd = ['./acotsp']
    cmd += arguments_to_call
    io = Popen(cmd, stdout=PIPE)
    out_, err_ = io.communicate()
    result = out_.decode("utf-8").strip()
    best = re.findall(r'Best [-+0-9.e]+', result)[0].split(' ')[-1]
    updated_best = 100*(abs(instance_opt - float(best)))/instance_opt
    print(updated_best)
    sys.exit(0)
