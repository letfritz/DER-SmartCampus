# Optimal siting and sizing of distributed energy resources in a Smart Campus <img src="https://skillicons.dev/icons?i=python" /> <img src="https://github.com/letfritz/DER-SmartCampus/assets/161434060/4696e7f4-d998-4032-8fb5-ad344b01b02e" style="max-width: 50%; height: 50px;">

<div align="center"><br/>
  <div style="display: inline-block;">
    <img align="center" alt="stars" src="https://img.shields.io/github/stars/letfritz/DER-SmartCampus">
    <img align="center" alt="watchers" src="https://img.shields.io/github/watchers/letfritz/DER-SmartCampus">
    <img align="center" alt="forks" src="https://img.shields.io/github/forks/letfritz/DER-SmartCampus">
  </div>
  <div style="display: inline-block;">
    <img align="center" alt="downloads" src="https://img.shields.io/github/downloads/letfritz/DER-SmartCampus/total.svg">
    <img align="center" alt="issues" src="https://img.shields.io/github/issues/letfritz/DER-SmartCampus/total.svg">
    <img align="center" alt="issues-closed" src="https://img.shields.io/github/issues-closed/letfritz/DER-SmartCampus/total.svg">
    <img align="center" alt="issues-pr" src="https://img.shields.io/github/issues-pr/letfritz/DER-SmartCampus/total.svg">
    <img align="center" alt="issues-pr-closed" src="https://img.shields.io/github/issues-pr-closed/letfritz/DER-SmartCampus/total.svg">
    <img align="center" alt="issues-pr-closed" src="https://img.shields.io/github/license/letfritz/DER-SmartCampus.svg">
  </div>
</div><br/>

Python code for optimizing the siting and sizing of distributed energy resources within a Smart Campus.

## 📷 Screenshot
Flowchart of the proposed methodology:<br></br>
![rede-metodologia](https://github.com/letfritz/DER-SmartCampus/assets/161434060/b1975bf6-6899-40af-90c4-d781c3a9ab13)

<br></br>
Topology of the university campus:
<br></br>
![rede-unifilar](https://github.com/letfritz/DER-SmartCampus/assets/161434060/9346bf1a-af1f-4cae-b082-622e1cba64d3)

<br></br>
Pareto Frontier with objective function 1 on the 𝑥-axis and objective function 2 on the 𝑦-axis
<br></br>
![pareto](https://github.com/letfritz/DER-SmartCampus/assets/161434060/a2e4093f-8a40-4f93-82f5-3a253eba2738)


## Installation
1. Install the `py_dss_interface`:
   ```
   pip install py-dss-interface
   ```
3. Download the package to a local folder (e.g. ~/DER-SmartCampus/) by running:
  ```
    git clone https://github.com/letfritz/DER-SmartCampus.git
  ```
3. Run Python IDE and navigate to the folder (~/DER-SmartCampus/), then run the main.py script.

## Usage
  - Running the main.py to compile the code.
  - People can change the excel file with the load and generation curves.
  - People can change the OpenDSS file with the University Campus grid.

## License
Released under MIT license.

## DER-SmartCampus Folder Contents
1. Folders
    - results: Folder with the results generated in the simulation. It contains files from the last simulation.
    
2. Files
    - main.py: main code.
    - analise_sensibilidade.py: File with the code for sensitivity analysis.
    - charts.py: File with code for generating charts of the results.
    - csdata.py: File with code for creating charge station curves.
    - gaoptimization.py: File with code for genetic algorithm optimization.
    - generationdata.py: File with code for creating dummy curves.
    - loaddata.py: File with code for organizing input files.
    - output.py: File with code for organizing the results.
    - scenarios.py: File with code for Monte Carlo simulation.
    - Modelagem_Circ_Dist_UFJF.dss: OpenDSS file with the grid model.
    - subestacao_VLN_Node.dss: OpenDSS file with the node specification.
    - Demanda_Cargas.xlsx: File with substation demand curves.
    - input_cs.xlsx: File with charge station load curves.
    - input_load.xlsx: File with buses load curves.
    - input_pv.xlsx: File with future photovoltaic generation curves.
    - PV_UFJF.xlsx: File with existing photovoltaic generation curves.

## 📝 About this Project
The advent of distributed energy resources (DERs) in microgrids has provided significant benefits. University campus microgrids can manage their DER efficiently to minimize consumption, energy losses, and environmental impacts. Thus, to boost the transition from a traditional university campus to a sustainable and smart campus, this paper proposes an optimal siting and sizing study of photovoltaic systems and electric vehicle charging stations for a microgrid of a Brazilian university. This problem is formulated as mixed-integer nonlinear programming and is carried out in two stages. The first stage minimizes grid losses by locating and sizing photovoltaic panels, while the second stage minimizes the grid losses and maximizes the proximity of charging stations to the load centers by optimizing the place and sizing of charging stations. In addition, this work considers load uncertainty through the Monte Carlo method with a scenario reduction technique. The 
results estimate that photovoltaic systems can reduce 13.48% of the monthly electricity cost. The optimal charging station location is usually near the photovoltaic system siting or the substation. However, the increase in the number of chargers in buses with high consumption causes an increase of around 5% in grid losses. Furthermore, this paper discusses possible scenarios for photovoltaic systems and charging station installation based on the benefits of the transition to a sustainable and smart campus, considering Brazilian electricity sector policies.

See more in [![Blog](https://img.shields.io/website?label=myDER-SmartCampus-paper.com&url=https://www.sciencedirect.com/science/article/abs/pii/S0378779622011440?via%3Dihub)](https://www.sciencedirect.com/science/article/abs/pii/S0378779622011440?via%3Dihub)

## 💡 Tool Innovation
To contribute to the studies of smart and sustainable university campuses, the paper [![Blog](https://img.shields.io/website?label=myDER-SmartCampus-paper.com&url=https://www.sciencedirect.com/science/article/abs/pii/S0378779622011440?via%3Dihub)](https://www.sciencedirect.com/science/article/abs/pii/S0378779622011440?via%3Dihub) investigates the optimal 
siting and sizing of Photovoltaic (PV) plants and EVCSs in a Brazilian public university campus, the Federal University of Juiz de Fora (UFJF). The proposed methodology seeks to minimize electrical loss 
costs and maximize the proximity of charging stations to the highest consumption buses, providing flexibility and convenience in charging EVs near workplaces. The loss minimization approach is traditionally 
used for the initial analysis of the network model, although there are many significant criteria to evaluate the grid such as reliability, hosting capacity of distributed resources, well-being, and others. In 
addition, it is possible to minimize the purchase of energy without considering price variations by minimizing losses, and thus to estimate the microgrid operating cost, supporting the decision-making related to 
investment and planning.
In this paper, the mixed-integer nonlinear optimization is performed in two stages based on a Genetic Algorithm (GA). Furthermore, load and generation uncertainties are considered through the Monte Carlo 
method. In this scope, this paper seeks to:
  - Apply the Monte Carlo method to generate scenarios from the load and generation curves;
  - Apply scenario reduction techniques to reduce computational
  - Minimize electrical loss costs from the optimal DGs location and sizing;
  - Optimize the EVCSs siting and sizing to minimize electrical loss costs and maximize the proximity to the highest consumption buses;
  - Provide discussions for the University campus transition to a smart and sustainable University campus through a sensitivity study.
The proposed methodology can be applied on other University campuses and in other microgrids. In this sense, this paper seeks to contribute to mathematical models and political discussions about the stages of the energy transition of a smart campus through a case study on a Brazilian University.

## Citation
```
@article{HENRIQUE2023109095,
title = {Optimal siting and sizing of distributed energy resources in a Smart Campus},
journal = {Electric Power Systems Research},
volume = {217},
pages = {109095},
year = {2023},
issn = {0378-7796},
doi = {https://doi.org/10.1016/j.epsr.2022.109095},
url = {https://www.sciencedirect.com/science/article/pii/S0378779622011440},
author = {Letícia F. Henrique and Walquiria N. Silva and Caio C.A. Silva and Bruno H. Dias and Leonardo W. Oliveira and Madson C. de Almeida}
}
```
