import os
import sys
import glob
from subprocess import Popen, PIPE
from pathlib import Path
import threading
import shutil

INSTANCES_PATH = './InstanceTestingALL'
RESPALDOS_PATH = './respaldos'
CURRENT_PATH = os.path.dirname(__file__)
hyperParametersTries = {}



def testConfiguration(cp, mt, p, index, folder):
    instances_dir = os.listdir(INSTANCES_PATH)
    #cada dir de instancias
    for dir in instances_dir:
        evals_of_nk = []
        instances = os.listdir(os.path.join(INSTANCES_PATH, dir))
        #cada instancia dentro de cada dir
        for instance in instances:
            instance_path = os.path.join(INSTANCES_PATH, dir, instance)
            #10 semillas por instancias 
            for seed in range(11):
                cmd = ['./ga-nk', instance_path, f"temp_{instance}_{cp}_{mt}_{p}_{seed}.dat", cp, mt, p, '100000', str(seed), '1']
                io = Popen(cmd, stdout=PIPE)
                out_, err_ = io.communicate()
                with open(f"temp_{instance}_{cp}_{mt}_{p}_{seed}.dat", "r") as file:
                    data = file.read().strip()
                    evals = data.split(' ')[-1]
                    os.remove(f"temp_{instance}_{cp}_{mt}_{p}_{seed}.dat")
                    evals_of_nk.append(evals)
        all_evals = '\n'.join(evals_of_nk)
        with open(os.path.join(folder, f"eval_{dir}_{index}"), 'a') as respaldo_file:
            respaldo_file.write(all_evals)
    #ejecutar resumen instancias
  #  cmd = ['python3', os.path.join(folder, 'resumeEval.py')]
   # io = Popen(cmd, stdout=PIPE)
    #out_, err_ = io.communicate()



file = sys.argv[1]
with open(file) as paramFile:
    lines = paramFile.readlines()
    lines = [line.strip() for line in lines]
    file_name = file.split('.')[0]
    hyperParametersTries[file_name] = lines
print(hyperParametersTries)


threads = []
for hyperParam, paramList in hyperParametersTries.items():
    os.mkdir(hyperParam)

    #evaluar cosas
    for index,param in enumerate(paramList):
        folder = os.path.join(hyperParam, f"{hyperParam}_{index}")
        os.mkdir(folder)
        shutil.copyfile('resumeEval.py', os.path.join(folder, 'resumeEval.py'))
        cp, mt, p = param.split(' ')
        print(f"cp {cp} mt {mt} p {p}")
        t = threading.Thread(target=testConfiguration, args=(cp, mt, p, index, folder))
        threads.append(t)
        t.start() 
