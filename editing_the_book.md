# Editing The Book

Hi, welcome this is a short guide on getting set up with the project if you would like to contribute.

Firstly you will need to clone the Github repository. This can be found [here](https://github.com/seancraven/CDS_book). After these files are copied, I suggest you download Miniconda, if you don't have it or Anaconda already. 

From here in a terminal, swap /path/to/ with your path:
```
conda env create --file /path/to/CDSenv.yml
```
Then activate the environment.
```
conda activate CDS_310
```
From here to build the local Jupyter Book; navigate to the directory in which your book files are located(The ones you cloned from github). Then run
```
jb build ./
```
you