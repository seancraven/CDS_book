# Welcome
Welcome to the readme.md of the CDS Book. Currently, this contains the plan for the project. However, I will write some short instructions on how to add pages etc and set up an enviroment such that one can contribute to the book easily. 

## Standards for the book
Code cell line width: 75 Characters
###
Writing style: 
- Exclusively in 3rd person.
- Formal
### Matplotlib Defaults:
- Colours:
    - [x] Dur_utils module that contains colours.
    - [ ] Decide on a gradient colour scheme for 3d/many line plots
- [x] Consistent Figure sizes (10,6) for single depth Page Wide Plots
- [x] Consistent Font size/style for figures and text 
- [x] Consistent tick spacing 
    - [x] Edit RCparams
- Make an environment.yml file that has packages and changes to matplolib 
    - [ ] .yml
- [x] Fixed file tracking

## Plan 
### Landing Page
- [ ] Gallery of best visualisations
#### Chapter 1:
- Global $\textrm{CO}_2$: Question Can we identify Global CO_2 change because of Pandemic 

Pages:
- [x] Data Exploration
- [x] Curve fitting
- [x] Hypothesis Testing 
- [x] Conclusion And Questions

Formating:
- [x] Hide Code Cells
- [x] Standardise
- [x] Inital Proof
- [ ] Have all inline math go as follows
```{math}
:label:
```
#### Chapter 2
- Global Temperature rise, Predictive modelling 
Using Bayesian methods podudce distributions on the probability of warming targets being crossed

Pages:
- [x] Global CO_2 example
    - [x] Discuss the limited scope of curve fitting. Explore the error quantification.
    - [x] Page one and solution to the previous question
    - [x] Discussion section on the results.
- [x] Comparison of moving average of CO_2 and Temp
    - [x] The errors on the constant and the value of the X parameter are huge. Understand This.
    - Still not sure why; however, a more accurate quantification of the errors has been implemented.
- [x] Three SRES scenarios, plotted and discussed
    - [x] Have approximately matched and found literature doing similar analysis.
    - [ ] Implementation of natural cubic spline for CO_2 on [scipy](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.CubicSpline.html) 
- [ ] Bayesian Random Variables S & C

- [ ] Comparison and evaluation of final model

### Chapter 3
- Pyrads 

- [ ] Reformatting code 
    - [x] Split Functions file into multiple sensible little files
    - [ ] Add docstrings
    - [ ] Remove Redudant Functions
    - [ ] Type Hints
Files That Have Been Formatted:
- [x] plank.py
- [x] gas.py
    - apart from two functions
- [ ] isa.py is not my file could format it properly
- [x] lorenzian.py 
    - apart from the function that is the one that needs to be rewritten
- [x] plank.py
- [x] radation.py
- [x] reighligh.py

Optimization:
- [ ] Profile expensive functions 
- [ ] Improve expensive functions
Pages:
- [ ] Lorentzian Broadening 
    - [ ] rewrite the broadening function
    - [ ] write an overview of where line broadening comes from.
    - [ ] write an overview of how vibrational transitions work
    - [ ] write an overview of how electronic transitions work
    - [ ] look at the effect of how $S_{ij}$ is effected by [temperature](https://hitran.org/docs/definitions-and-units/)
- [ ] Atomic Crossections
- [ ] Absorbtion
- [ ] Short Wave
    


Formating:
- [ ] Hide Code Cells
- [ ] Standardise
 - [x] matplotlibrc edited
- [ ] Initial Proof
#### Chapter 3
- Radiation Modeling: Building Packages, Large Datasets 
- [ ] Refactoring the code from last year. 

### Journal of Reading/ Personal Skills Development/ Implementation Challenges
- 05.07.22: Bayesian Methods and bootstrapping covered in ESL
- [x] 03.07.22: Figure out how to use the Berkly Earth Data.

### Notes About Setup
- Currently, Jupyter Book uses a different kernel to execute the notebooks. The matplotlibrc file has to be copied into the specific directories where all of the 

### Important HITRAN links
- Remember key gen 
- [HITRAN](https://hitran.org/docs/definitions-and-units/)
    - HITRAN definitions and explanation
- [hapi docs](https://hitran.org/static/hapi/hapi_manual.pdf)
    - HITRAN api docs
- [hapi paper](https://www.sciencedirect.com/science/article/pii/S0022407315302466?via%3Dihub)
- [2020 Paper](https://www.sciencedirect.com/science/article/pii/S0022407321004416?via%3Dihub)
    - HITRAN paper
- [2017 TIPS](https://www.sciencedirect.com/science/article/pii/S0022407321002065)
    - Partition sum Paper
- [bytran](http://www.bytran.org/howtolbl.htm)
    - bytran is a phone app that implements HITRAN, link is to the physics documentation 