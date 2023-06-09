# Vulnerability analysis of public transport networks
### Luuk Boekestein, Linka Mitome and Shantanu Motiani 

## Project goals

Public transport networks play a crucial role in ensuring efficient mobility for millions of people in major European cities. However, due to maintenance disruptions, overpopulation, epidemics or changing urban dynamics, these networks often face challenges related to efficiency, robustness and vulnerability. In order to improve the overall performance of public transport systems, one must address these challenges and come up with innovative solutions. By analyzing the nuances of these public transit networks and identifying new potential connections or stops that can increase network connectivity, this project aims to explore strategies for enhancing the robustness of public transport networks in major European cities.

## Research

A detailed documentation of our research questions, approach, findings and discussions can be found in the [documentation](/docs/) folder of this repository, which contains the [project plan](docs/Project%20Work%20Plan.pdf) and [final report](/docs/).

## Dataset
The dataset we used contains a collection of public transport network data sets for 25 cities. The data includes all public transport modes (metro, tram, bus, etc.) and walking distances between different public transport stops.
The data is available for download online [here](https://zenodo.org/record/1186215#.ZEfKMXZBy5c), and the data for a selection of the cities can be found in the [dataset](/dataset/) folder of this repository.

## Code

The code we wrote for this project can be found in the [src](/src/) folder of this repository. We first performed an exploratory analysis of both cities, which can be found in the [analysis](/src/analysis.ipynb) notebook.

 The [auxiliaries.py](/src/auxiliaries.py), contains the auxiliary functions that we made for this project. We made custom functions that:
- Read in the network data
- Vizualize the network data
- Calculate the distance between nodes
- Calculate travel time measures
- Perform percolation on the data
- Perform repeated experiments

We then used these functions to perform experiments on both Berlin and Helsinki. The results and code for these experiments can be found in seperate files in the `src` folder for [Berlin](/src/experiments_berlin.ipynb) and [Helsinki](/src/experiments_helsinki.ipynb).

The packages that need to be installed in order to run the code are listed in the [requirements.txt](/requirements.txt) file.