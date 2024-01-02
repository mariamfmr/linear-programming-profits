# Title: Project
# Description: Project for the course of Analysis and Synthesis of Algorithms
# Author: Maria Ramos, 105875 Guilherme Campos, 106909

'''
Projeto 3:

O Professor Natalino Caracol foi contratado pela empresa UbiquityInc, 
em Rovaniemi na Lapónia, para desenvolver um programa que permita 
estimar o lucro máximo que pode ser obtido com a produção e venda de 
brinquedos durante o Natal.

A empresa produz diariamente um conjunto de n brinquedos de madeira 
{x1,...,xn}, onde cada brinquedo xi tem um lucro li. Para além de um 
limite máximo de produção de cada brinquedo devido a restrições de 
linha de montagem, a empresa está limitada a uma quantidade máxima total 
de brinquedos que podem ser produzidos por dia, devido a restrições de corte
da floresta boreal. 

Adicionalmente, este Natal a empresa decidiu, para além de vender cada 
brinquedo individualmente, vender também pacotes especiais contendo três 
brinquedos distintos, cujo lucro é maior do 
que a soma dos lucros individuais dos brinquedos que o constituem.

O objectivo consiste em indicar ao Rüdolf, CEO da UbiquityInc, qual o 
lucro máximo que se pode obter diariamente. A UbiquityInc, tratará
posteriormente do problema da distribuição.

A implementação deve ser baseada em Python com recurso à biblioteca 
PuLP para resolução de problemas LP (https://pypi.org/project/PuLP/). 
Exemplos disponíveis em https://github.com/coin-or/pulp/tree/master/examples.
'''

'''
Input:
O ficheiro de entrada contém informação sobre os n produtos, o lucro e 
a capacidade de produção da empresa de cada um, da seguinte forma:

• Uma linha contendo três inteiros: ti ndicando o número de diferentes
brinquedos passíveis de serem produzidos, p indicando o número de pacotes 
especiais, e max indicando o número máximo de brinquedos que podem ser 
produzidos por dia;

• Uma lista de n linhas, em que cada linha contém dois inteiros li e ci, 
indicando o lucro e a capacidade de produção do brinquedo i.
• Uma lista de p linhas, em que cada linha contém quatro inteiros 
i, j, k, e li jk, indicando o lucro li jk do pacote especial {i, j, k}, e 
o nome dos produtos i, j, e k que o constituem.
Quaisquer inteiros numa linha estão separados por exactamente um 
espaço em branco, não contendo qualquer outro carácter, a não ser o fim de linha.

'''

'''
Output:
O programa deverá escrever no output um inteiro correspondendo ao lucro 
máximo que o Rüdolf pode obter diariamente.

Exemplo 1:

Input
5 2 150
50 27
30 33
45 30
40 37
35 35
1 3 5 130
2 3 4 130

Output
6440

Exemplo 2:

Input
5 2 15
50 27
30 33
45 30
40 37
35 35
1 3 5 129
2 3 4 130

Output
750
'''
from pulp import *

# Read the number of toys, number of special packages, and maximum number of toys that can be produced per day
n, p, max_toys = map(int, input().split())

# Initialize the problem
prob = LpProblem("Maximize Profit", LpMaximize)

# Create a list for toys and their profits and production capacities
toys = []
profits = {}
capacities = {}

for i in range(1, n+1):
    profit, capacity = map(int, input().split())
    toys.append(i)
    profits[i] = profit
    capacities[i] = capacity

# Create a list for special packages and their profits
packages = []
package_profits = {}
package_toys = {}

for i in range(1, p+1):
    toy1, toy2, toy3, profit = map(int, input().split())
    packages.append(i)
    package_profits[i] = profit
    package_toys[i] = [toy1, toy2, toy3]

# Create the decision variables
toy_vars = LpVariable.dicts("Toy", toys, 0, None, LpInteger)
package_vars = LpVariable.dicts("Package", packages, 0, None, LpInteger)

# Add the objective function to the problem
prob += lpSum([profits[i]*toy_vars[i] for i in toys]) + lpSum([package_profits[i]*package_vars[i] for i in packages]), "Total Profit"

# Add the constraints to the problem
for i in toys:
    prob += toy_vars[i] + lpSum([package_vars[j] for j in packages if i in package_toys[j]]) <= capacities[i], f"Capacity_{i}"

prob += lpSum([toy_vars[i] for i in toys]) + 3*lpSum([package_vars[i] for i in packages]) <= max_toys, "MaxToys"

# Solve the problem
prob.solve(GLPK(msg=0))

# Print the results
print(value(prob.objective))