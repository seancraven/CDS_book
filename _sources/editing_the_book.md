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
Connect to your GitHub with:
```{shell}
git config --global user.name "your github username"
git config --global user.email "your github emial"
```

Now navigate to the folder in which you want to store the project from there 
perform a git clone:
```{shell}
git clone https://github.com/seancraven/CDS_book.git
```
In the cloned files, there is a `requirements.txt` file, from which all the required packages can be installed, first we install the virtual environments package:
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
With the environment activated all the required packages can be installed,
```{shell}
pip install -r requirements.txt
```
With the environment for the book set up it can be built. 
The build command is targeted at a directory with the `_config.yml` and `_toc.yml`. If you have cloned the git repository these will be in the `CDS_book` directory. From here
```{shell}
jupyter-book build /path/to/book/
```
This will provide you with a HTML document that can be opened in a web browser. 

## Publishing a Jupyter Book

Jupyter Book is integrated with GitHub pages, this makes it easy to publish updates to your book in one line from the terminal. The GitHub pages package can be obtained with a normal pip install:
```{shell}
pip install ghp-import
```
Before the project can be published on a GitHub page it needs a GitHub repo. The first author of the book doesn't maintain the repository it is better that new iterations clone and publish new cloned repos. 
This means that a new repo for the project should be made on [GitHub](https://github.com). When you make this repo do not initialise it with any files such as a readme or a licence. 
```{tip}
When working with GitHub if you are asked for a password in the shell, this is not the website password but a gpg key that you can generate from your github page online. Instructions are found [here](https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account)
```
After you have done this you will have to rename the original remote:
```{shell}
git remote rename origin upstream
```
Add your GitHub remote:
```{shell}
git remote add origin  https://github.com/your-account/your-repository.git
```
Finally we push the content to the repo:
```{shell}
git push origin main 
```
Now with the version control setup you can record changes with commits and store all the work on GitHub. Git can be hard to learn and making mistakes can be even harder to fix. Stackexchange is your friend as well as [ohshitgit](https://ohshitgit.com/). 


With a repo for the project the GitHub page can be setup easily. First navigate to the main directory where the `_build` folder of the book is located and run 
```{shell}
ghp-import -n -p -f _build/html
```
 