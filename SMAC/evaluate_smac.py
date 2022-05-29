import subprocess
import random 
import os
import sys 


SEED = 3
NUMBER_OF_SEEDS = 10


random.seed(SEED)





def exec_algorithm(algorithm, instance, params, seed):
    TOTAL_EVAL = '1000'
    cmd = [algorithm, instance, str(seed), params['ants'], TOTAL_EVAL, params['alpha'], params['beta'], params['ph-max'], params['ph-min'], params['rho']]
    cmd += ['0','0','0','0','0','0','0','0']
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                  universal_newlines=True)
    stdout_, stderr_ = p.communicate()
    return stdout_.strip()



def evaluate_params(algorithm, instance_folder, seeds_number, params):
    resumen = []
    for filename in os.listdir(instance_folder):
        instance = os.path.join(instance_folder, filename)
        if os.path.isfile(instance):
            values = []
            print(f"----------------- INSTANCE: {filename} ----------------------")
            for _ in range(seeds_number):
                instance_seed = random.randint(0, 9999)
                output = exec_algorithm(algorithm, instance, params, instance_seed)
                values.append(output)
                print(f"VALUE: {output} ; SEED: {instance_seed}")
            values = list(map(float, values))
            promedio = sum(values)/len(values)
            resumen.append((filename, promedio))
            print(f"El promedio es {promedio}")
    print(resumen)
    return resumen

#example cal python evaluate_smac.py /ak/target_algorithm/AK testingEasy

algorithm_path, instances_type = sys.argv[1:]

ALGORITHM =  f"./algorithms/{algorithm_path}"
INSTANCE_FOLDER = f"./algorithms/instances/testing/{instances_type}"

param_values = [
                {'alpha': '1.6','ants': '15', 'beta': '7.6', 'ph-max': '6.7', 'ph-min': '0.01', 'rho': '0.1'},
                {'alpha': '1.8','ants': '18', 'beta': '7.7', 'ph-max': '7.9', 'ph-min': '0.01', 'rho': '0.1'},
                #{'alpha':'1.3', 'ants': '20', 'beta': '5.9', 'ph-max': '2.0', 'ph-min': '0.01', 'rho': '0.4'},
                #{'alpha': '3.7','ants': '8', 'beta': '6.1', 'ph-max': '7.7', 'ph-min': '0.01', 'rho': '0.8'},
                #{'alpha': '5.0','ants': '15', 'beta': '3.9', 'ph-max': '8.9', 'ph-min': '0.01', 'rho': '0.1'},
               ]

resumen_general = []
for params in param_values:
    print(f"Parámetros obtenidos por SMAC {params}")
    resumen = evaluate_params(ALGORITHM, INSTANCE_FOLDER, NUMBER_OF_SEEDS, params)
    resumen_general.append((params, resumen))
    print("\n\n")

print(resumen_general)


print(algorithm_path)
print(instances_type)