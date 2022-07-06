# Welcome
Welcome to the readme.md of the CDS Book. Currently, this contains the plan for the project. However, I will write some short instructions on how to add pages etc and set up an enviroment such that one can contributre to the book easily. 

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
#### Chapter 2
- Global Temperature rise, Predictive modelling 

- [x] Discuss the limited scope of curve fitting. Explore the error quantification.
    - [x] Page one and solution to the previous question
    - [x] Discussion section on the results.
- [ ] The errors on the constant and the value of the X parameter are huge. Understand This.
Pages:
- [x] Global CO_2 example
- [x] Comparison of moving average of CO_2 and Temp
- [ ] testing simple model
- [ ] Global Temperature Data exploration and Bayesian predictions of warming temperatures crossed.
    - Match 3 approximate scenarios to some of those in the SRES
        - [x] Have approximately matched and found literature doing similar analysis. Implementation is probably not that difficult now as of 05.07.22. 

- [x] Figure out how to use the Berkly Earth Data that is formatted weirdly.
```{note}
Berkeley Earth website is down currently using kaggle data.
```

Formating:
- [ ] Hide Code Cells
- [ ] Standardise
- [ ] Initial Proof
#### Chapter 3
- Radiation Modeling: Building Packages, Large Datasets 
- [ ] refactoring the code from last year. 

### Journal of Reading/ Personal Skills Development
- 05.07.22: Bayesian Methods and bootstrapping covered in ESL

### Notes About Setup
- Currently, Jupyter Book uses a different kernel to execute the notebooks. The matplotlibrc file has to be copied into the specific directories where all of the 