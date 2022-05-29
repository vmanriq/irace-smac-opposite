./execIraceBash.sh acotsp_normal 1 5 ./acotsp scenario.txt FALSE instances-list.txt 0.4 0.2 &
# variacion generacion
./execIraceBash.sh acotsp_g20_f10 1 5 ./acotsp scenario.txt TRUE instances-list.txt 0.2 0.1
./execIraceBash.sh acotsp_g30_f10 1 5 ./acotsp scenario.txt TRUE instances-list.txt 0.3 0.1 &
./execIraceBash.sh acotsp_g40_f10 1 5 ./acotsp scenario.txt TRUE instances-list.txt 0.4 0.1
#variacin de filtro 
./execIraceBash.sh acotsp_g20_f20 1 5 ./acotsp scenario.txt TRUE instances-list.txt 0.2 0.2 &
./execIraceBash.sh acotsp_g20_f30 1 5 ./acotsp scenario.txt TRUE instances-list.txt 0.2 0.3 
./execIraceBash.sh acotsp_g30_f40 1 5 ./acotsp scenario.txt TRUE instances-list.txt 0.2 0.4 &
