# IRACE

El presente código representa un fork de [IRACE](https://cran.r-project.org/web/packages/irace/vignettes/irace-package.pdf) con las modificaciones respectivas para implemetación de la estrategia opuesta.

Para su utilización:

1. Ingresar a R e instalar irace y devtools
```R
install.packages('irace')
install.packages('devtools')
```
Devtools se demora bastante y puede dar errores, para solucionar estos principalmente basta con instalar los siguientes paquetes

```shell
sudo apt-get install libzmq3-dev libharfbuzz-dev libfribidi-dev libfreetype6-dev libpng-dev libtiff5-dev libjpeg-dev build-essential libcurl4-openssl-dev libxml2-dev libssl-dev libfontconfig1-dev

```

2. Ejecutar 

```shell
 ./execIraceBash.sh $nameFile $iterLower $iterUpper $algorithm_folder $scenario_name $oppositeFlag $nameInstances $generationPercentage $filterThresh
```

Donde: 

+ **nameFile**: nombre del archivo en el cual se va a guardar el output
+ **iterLower**: número  desde el cual va  a empezar la iteración
+ **iterUpper**: número hasta cual va llegar la iteración
+ **algorithm_folder**: nombre de la carpeta donde se encuentra el algoritmo a sintonizar
+ **scenario_name**: nombre del archivo donde se encuentra el escenario
+ **oppositeFlag**: Flag que denota si se esta utilizando la estrategia opuesta o no. Si es True esta se encuentra utilizando
+ **nameInstances**: archivo con el nombre de las instancias a utilizar
+ **generationPercentage**: Porcentaje inicial de configuraciones opuestas que se van a utilizar
+ **filterThresh**: Umbral con el cual se filtrarán las configuraciones descartadas