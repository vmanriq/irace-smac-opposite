
for i in 1 2 3 4 5
do
	command python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed $i --OL True --budget_prob_0 100 --prob_decay 0.9 --filter 0.2 > acotsp_d90_f20_$i.txt
done

for i in 1 2 3 4 5
do
	command python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed $i --OL True --budget_prob_0 100 --prob_decay 0.9 --filter 0.3 > acotsp_d90_f30_$i.txt
done&

for i in 1 2 3 4 5
do
	command python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed $i --OL True --budget_prob_0 100 --prob_decay 0.9 --filter 0.4 > acotsp_d90_f40_$i.txt
done

