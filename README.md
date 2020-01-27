# Lab 1 (Decision Trees)
0. 
> Each one of the datasets has properties which makes
them hard to learn. Motivate which of the three problems is most
difficult for a decision tree algorithm to learn.

Answer: For the first dataset two attributes, a_1 and a_2, are related therefore it is hard for the decision tree to split between these. The second dataset two arbitrary attributes are needed to have the value one to be true, hence it is the hardest dataset to split. The third dataset contains the smallest training set and noise.

1.
> The file dtree.py defines a function entropy which
calculates the entropy of a dataset. Import this file along with the monks datasets and use it to calculate the entropy of the training
datasets.

Answer: 

| Dataset        | Entropy           |
| ------------- |:-------------:| 
| MONK-1    | 1  | 
| MONK-2      | 0.957117428264771   |  
| MONK-3 |    0.9998061328047111  | 

> Explain entropy for a uniform distribution and a non-uniform distribution, present some example distributions with
high and low entropy.

Answer: Entropy measures the uncertainty. Hence in reference to lecture 2, rolling a fake dice, a nonuniform distribution, with an higher probability to land on one side implies the entropy becomes numerically lower in comparison to rolling a real dice, which is a uniform distribution. In other words since the probability is higher for one side on the fake dice, the total uncertainty of the total fake dice is lower than for a real dice.


4.asdasfnaipfgpasfpsoafpoasnfpasnfpanfpanfpoasnfpoasndp
