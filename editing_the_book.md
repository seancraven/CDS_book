# Editing The Book

Hi, welcome this is a short guide on getting set up with the project if you would like to contribute.

Unfortunately the Jupyter Book project is in the early stages and only has provisional support for windows. However, Windows users can use Windows subsystem for Linux. This should avoid any windows related problems. You can find instructions to set up wsl [here]( https://docs.microsoft.com/en-us/windows/wsl/install). 

We have not tested Jupyter Book on Mac Os, so your mileage may vary. There is always the option of running a linux virtual machine. 

If you are new to Linux, The [Ubuntu](https://ubuntu.com/wsl) distro, is very popular.

With some form of Linux install you will need a python and pip. 
First check the system is up to date,
```{shell}
sudo apt update
```
Then install pip,
```{shell}
sudo apt install python3-pip
```
You can check that this has installed correctly with:
```{shell}
pip3 --version
```
## Setting Up a New Jupyter Book
If you are looking to make a new project, then setting up ones own book is quite simple. 
First download the package:
```{shell}
pip install -U jupyter-book 
```
Now, I would recommend creating a virtual environment, this enables you to have a siloed version of python to work from, so that it does not affect your other work. 
Creating a folder to contain the project is sensible, navigate in the shell to this folder:
```{shell}
cd /path/to/my/project/folder/
```
from here create a virtual environment:
```{shell}
pip install -U virtualenv
```
Here you replace `the_name_of_the_environment`, with a name for your environment.
```{shell}
python3 -m venv the_name_of_the_environment
```
Now activate that environment, from the directory in which you created the environment:
```{shell} 
source ./the_name_of_the_environment/bin/activate
```
We now create the book: 
```{shell}
jupyter-book create mynewbook/ 
```
This will create a new jupyter book with a `_toc.yml` and a `.config.yml`. 
This template book can be edited. Full details on how to use the books are provided on the [Jupyter Book](https://jupyterbook.org/en/stable/start/your-first-book.html)

## Editing This Book 

To edit this book we begin with cloning the GitHub repository. Before, this however git must be installed: 
```{shell} 
sudo apt install git 
```

Now navigate to the folder in which you want to store the project from there 
perform a git clone:
```{shell}
git clone 