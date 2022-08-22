# Sequential Model Algorithm Configuration (SMAC)

El presente código representa un fork del repositorio principal de [SMAC](https://github.com/automl/SMAC3) con las modificaciones respectivas para implemetación de la estrategia opuesta.

Para su utilización:

1. Generar un entorno virtual de python por medio del comando `python3 -m venv [nombre env]`
2. Luego activarlo mediante `source [nombre env]/bin/activate`
3. Instalar requerimientos de la libreria mediante `pip install -r requirements.txt`
4. Agregar el algoritmo que se desea sintonizar dentro de la carpeta algorithms
5. Posicionarse sobre la carpeta del algoritmo que se desa sintonizar y ejecutar

```shell
python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed $SEED --OL $OL_FLAG --budget_prob_0 100 --prob_decay $PROB_DECAY --filter $FILTER
```

Donde:

+ **$SEED**: es el número de semilla a ejecutar
+ **$OL_FLAG**: puede tomar el valor {True, False} y denota si es que se esta utilizando o no la estrategia opuesta
+ **$PROB_DECAY**: es la velocidad en que decae la pobabilidad de aceptación y esta va de [0,1]
+ **$FILTER**: Permite manejar el umbral con el cual se filtraran las configuraciones descartadas [0, 1]

Se presentan dos algoritmos de ejemplo para la utilización del sintonizador, este son GA y ACOTSP

## Ejemplo de aplicación 

1. Posicionarse sobre SMAC/algorithms/acotsp
2. Ejecutar 🤓
```shell
python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed 4 --OL True --budget_prob_0 100 --prob_decay 0.9 --filter 0.2
```