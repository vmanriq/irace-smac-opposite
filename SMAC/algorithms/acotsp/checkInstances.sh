while read p; do 
  echo "./target_algorithm/acotsp -i $p -r 1 --tours 3 --time 0"
  command ./target_algorithm/acotsp -i $p -r 1 --tours 3 --time 0 --quiet
done<instances.txt
