import os
from statistics import pstdev

ignored = ['resumeEval.py']
evals = [x for x in os.listdir('./') if x not in ignored] 
evals.sort()

with open('global.dat', 'a') as globalFile:
    for eval in evals:
        with open(eval, 'r') as file:
            lines  = file.readlines()
            lines = [line.strip() for line in lines]
            lines = list(map(int, lines))
            name_instance = '_'.join(eval.split('_')[1:-1])
            average = round(sum(lines)/len(lines), 3)
            desviacion = round(pstdev(lines), 3)
            globalFile.write(f"{name_instance} {average} {desviacion} \n")
