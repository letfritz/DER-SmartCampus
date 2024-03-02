# Optimal siting and sizing of distributed energy resources in a Smart Campus <img src="https://skillicons.dev/icons?i=python" />
<div align="center"><br/>
  <div style="display: inline-block;">
    <img align="center" alt="stars" src="https://img.shields.io/github/stars/letfritz/CPVT3N.svg">
    <img align="center" alt="watchers" src="https://img.shields.io/github/watchers/letfritz/CPVT3N.svg">
    <img align="center" alt="forks" src="https://img.shields.io/github/forks/letfritz/CPVT3N.svg">
  </div>
  <div style="display: inline-block;">
    <img align="center" alt="downloads" src="https://img.shields.io/github/downloads/letfritz/CPVT3N/total.svg">
    <img align="center" alt="issues" src="https://img.shields.io/github/issues/letfritz/CPVT3N/total.svg">
    <img align="center" alt="issues-closed" src="https://img.shields.io/github/issues-closed/letfritz/CPVT3N/total.svg">
    <img align="center" alt="issues-pr" src="https://img.shields.io/github/issues-pr/letfritz/CPVT3N/total.svg">
    <img align="center" alt="issues-pr-closed" src="https://img.shields.io/github/issues-pr-closed/letfritz/CPVT3N/total.svg">
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
1. Download the package to a local folder (e.g. ~/DER-SmartCampus/) by running:
  ```
    git clone https://github.com/letfritz/DER-SmartCampus.git
  ```
2. Run Python IDE and navigate to the folder (~/DER-SmartCampus/), then run the main.py script.

## Usage


## Tips to Begin


## License
Released under MIT license.

## DER-SmartCampus Folder Contents
1. Folders

2. Files
    

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
