# Welcome
Welcome to the readme.md of the CDS Book. Currently, this contains the plan for the project. However, I will write some short instructions on how to add pages etc and set up an environment such that one can contribute to the book easily. 

## Timetable
Part 1

Finish book in Current state: 
 - [x] Chapter 3 proofed and complete Friday 5th August.
   - Simple Trans needs some additional work the coupling and packing into a module is more complex than anticipated
 - [ ] Chapter 2 proofed and complete Wednesday 10th August.

Part 2 

Improved accessibility:
 - [ ] Jupyter book setup guide 12th August. 

Week of 15th August:
 - [ ] Glossary and topic links
 - [ ] Improved python explanations
 - [ ] Further depth on concepts. 

## Standards for the book
Code cell line width: 75 Characters
Black Formatter. 
###
Writing style: 
- Exclusively in 3rd person.
- Formal
### Matplotlib Defaults:
- Colours:
    - [x] Dur_utils module that contains colours.
    - [x] Decide on a gradient colour scheme for 3d/many line plots: Rocket
- [x] Consistent Figure sizes (10,6) for single depth Page Wide Plots
- [x] Consistent Font size/style for figures and text 
- [x] Consistent tick spacing 
    - [x] Edit RCparams
- [x] Matplotlib Updates
- [x] Fixed file tracking
- Fix matplotlib latex use
- fix durutils

## Plan 
### Landing Page
- [ ] Gallery of best visualisations
#### Chapter 1:
- Global $\textrm{CO}_2$: Question Can we identify Global CO_2 change because of Pandemic 

Pages:
- [x] Data Exploration
- [x] Curve fitting
- [x] Hypothesis Testing 
  - [ ] More Heurisitics about chisq
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
- [x] predictive modeling
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
Pages:
- [ ] Atmospheric Physics Primer
  - [ ] Black Body
  - [ ] Vibrational Transitions: Charles
  - [x] Line Shapes 
- [x] Temperature Dependence and HITRAN-api
- [ ] Two Stream
- [x] Implementation of absorbtion co-efficient db
- [ ] Multigas
- [x] Absorption

Formating:
- [ ] Hide Code Cells
- [ ] Standardise
 - [x] matplotlibrc edited
- [ ] Initial Proof

### Backend Chapters 
Relational Database:
  - [x] Short Introduction to ERD and SQL
SimpleTrans:
  - [ ] Brief Overview of Functionality. Partially Complete
  - [ ] SimpleTrans Install Guide


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