from asyncio.subprocess import PIPE
import shutil
from subprocess import Popen
import sys
import os
import threading
import re



INSTANCES_PATH = './instancesEval'

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
                'u574': 36905, 'u724': 41910, 'u1060': 224094, 'u1432': 152970, 'u1817': 57201, 'u2152': 64253, 'u2319': 234256, 'ulysses16': 6859,
                'ulysses22': 7013, 'vm1084': 239297, 'vm1748': 336556, 'sii175': 21407 }
    instance_name = instance.split('/')[-1].split('.')[0]
    return all_opts[instance_name]

def readParams(file):
    file = sys.argv[1]
    with open(file) as paramFile:
        lines = paramFile.readlines()
        lines = [line.strip() for line in lines]
        file_name = file.split('.')[0]
        return (file_name, lines)

def formatParam(alpha, ants, beta, dlb, elitistants, localsearch, nnls, rho):
    params = ['--alpha', alpha, '--beta',beta, '--ants',ants,  '--dlb', dlb, '--elitistants', elitistants, '--localsearch', localsearch, '--nnls', nnls, '--rho', rho]
    return params


def testConfiguration(alpha, ants, beta, dlb, elitistants, localsearch, nnls, rho, folder, index):
    instances_dir = os.listdir(INSTANCES_PATH)
    for instance in instances_dir:
        evals = []
        instance_path = os.path.join(INSTANCES_PATH, instance)
        instance_opt = get_optimum(instance.split('.')[0])
        format_parameters = formatParam(alpha, ants, beta, dlb, elitistants, localsearch, nnls, rho)
        for seed in range(11):
            cmd = ['./acotsp', '-i', instance_path, '--seed', str(seed), '-r', '1', '--quiet', '--tours', '10000', '--eas', '-o', str(instance_opt)]
            cmd += format_parameters
            io = Popen(cmd, stdout=PIPE)
            out_, err_ = io.communicate()
            result = out_.decode("utf-8").strip()
            best = re.findall(r'Best [-+0-9.e]+', result)[0].split(' ')[-1]
            updated_best = 100*(abs(instance_opt - float(best)))/instance_opt
            evals.append(str(updated_best))
        all_evals = '\n'.join(evals)
        with open(os.path.join(folder, f"eval_{instance}_{str(index)}"), 'a') as respaldo_file:
            respaldo_file.write(all_evals)
    return 


if __name__ == "__main__":
    file = sys.argv[1]
    file_name, lines = readParams(file)
    os.mkdir(file_name)
    threads = []

    for index, param in enumerate(lines):
        folder = os.path.join(file_name, f"{file_name}_{index}")
        os.mkdir(folder)
        shutil.copyfile('resumeACO.py', os.path.join(folder, 'resumeACO.py'))
        alpha, ants, beta, dlb, elitistants, localsearch, nnls, rho = param.split(' ')
        print(f"param {index}")
        t = threading.Thread(target=testConfiguration, args=(alpha, ants, beta, dlb, elitistants, localsearch, nnls, rho, folder, index))
        threads.append(t)
        t.start()

