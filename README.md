# Max Profit Linear Programming with PuLP

This repository contains a Python implementation of a linear programming model to optimize the production and packaging of toys, along with a version (`max-profit-chrono.py`) that measures the execution time for each input.
The problem given aims to maximize the profit obtained by producing toys and special packages, restrained by constraints on production capacities and maximum number of toys that can be produced per day. 
Initially, the toys, their profits, and production capacities are organized into a dictionary, representing potential production configurations. Following this organization, linear programming is applied to explore all possible combinations of toy production and packaging, thus obtaining the maximum values of subproblems until reaching a global solution.
Our solution employs the PuLP library, a Python linear programming API, to calculate the maximum achievable profit, and the GNU Linear Programming Kit (GLPK), a software package intended for solving large-scale linear programming problems.
More information on PuLP and GLPK can be found here (https://pypi.org/project/PuLP/) and here (https://www.gnu.org/software/glpk/).

## Getting Started

Clone the repository to your local machine using the following command in your terminal or command prompt:

```bash
git clone https://github.com/mariamfmr/linear-programming-profit/
```

### Prerequisites

- Python 3
- PuLP library
- GLPK solver

 Python3 can be installed with the following command:

```bash
sudo apt isntall python3-pip
```

 The PuLP library can be installed with the following command:

```bash
python -m pip install pulp
```

The GLPK package can be installed with the following command:

```bash
sudo apt-get install glpk-utils
```

### Build and Run

To execute the script for each input file in the `testsTime` folder, run the following commands:

```bash
make test
```

To clean the generated output files from the testsTime folder, use:

```bash
make clean
```

To check the current python version running, use:

```bash
make checkpy
```

To run the script on a specific input file:
```bash
python3 max-profit.py < testfile
```

### Test Data

The repository includes a total of 14 tests located in the testsTime folder, ranging from simple tests, to larger input ones.
Each test in `testsTime/` includes a set of toys with randomized profits and production capacities, and special packages with randomized profits and associated toys. 
To generate additional tests, use the following command:

```bash
./gen_ubiquity <T> <P> <Tcmin> <Tcmax> <Tlmax> <Pok> <seed>
```
- `T`: number of toys
- `P`: number of packs
- `Tcmin`: Toy min capacity
- `Tcmax`: Toy max capacity
- `Tlmax`: Toy max profit
- `Pok`: % valid packs [0,100]
- `seed`: random seed generator (optional)

### Contents

- src/max-profit.py: Main algorithm implementation in python language.
- src/max-profit-chrono.py: Algorithm version that measures execution time.
- src/gen_ubiquity: Auxiliar tool to generate additional test inputs.
- makefile: Makefile for running (`max-profit-chrono.cpp`) on all the inputs files in testsTime.
- relatorio.pdf: Document explaining the main problem, summarizing the solution, and drawing conclusions from both practical and theoretical analyses.

### Conclusion

Practical analysis is further detailed in the relatorio.pdf.

