# R < iraceRun.R --no-save --args 10 ./ak scenario.txt TRUE trainInstancesHARD.txt 0.3 0.2
# se necesita estar parado en la carpeta  tunners/irace/tunning
library('irace')
library('devtools')
load_all()

args <- commandArgs()

cat("Los commands Args son", args, "\n")
setwd(args[5])
#
seed <- args[4]

scenario <- readScenario(filename = args[6])
scenario$seed <- seed
scenario$OL <- as.logical(args[7])
scenario$trainInstancesFile <- args[8]
scenario$generationPercentage <- as.double(args[9])
scenario$filterThresh <- as.double(args[10])
irace.main(scenario = scenario)
