# An Aside On Python
As of writing, Python is the most popular [programming language](https://www.tiobe.com/tiobe-index/) globally. It is designed to be easy to use while not forgoing functionality. Python is famous for being slow compared to many languages. For non-production code, this is often not a problem. The syntax's ease of implementation, readability, and efficiency make it a superior choice for many scientific and industrial analysis applications, where speed is not the top priority.

In previous courses at Durham, The Jupyter Notebook format has probably been used. Running code on a pre-configured server like that in Level-2 discovery skills is straightforward. However, running off a local machine can become beneficial when projects grow in complexity and with more dependencies. [Anaconda](https://www.anaconda.com/) provides a straightforward way to get a Python install with lots of the commonly used scientific libraries. 

## Environments and Packages
Environments are designed so that when code is run somewhere else or at a different time, it still functions. Further, they contain any dependency problems one might encounter with packages. A package is a third party library for Python. For example, Tensorflow's compatibility with the newest version of Numpy is not guaranteed. To ensure that Numpy in other projects is up to date, but Tensorflow functions correctly. An environment can be made where the required version of both packages are kept, for said project. 

There are multiple different options for environments. However, this text recommends anacondas [envs](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html). For the exercises in this book, create a new environment from this 'link here' .yml file. Then, navigate to the file's location in anaconda prompt(Windows) or your shell(Linux, Mac). Finally, run this command to create an environment with the dependencies. 
``` 
conda env create -f cds_book.yml
``` 
To get python to run with these packages, to activate the environment. The enviroment name can be found in the first line of the .yml file.
  
'''
conda activate env_name
'''
In an editor(VScode, Jypter,..), select the kernel with the same name as the environment. This is editor/IDE dependant, and should be in the respective guide.   


## Readability and Naming
The development of readable maintainable code is not something often taught in an undergraduate Physics course. However, when working with others or on long projects, the veracity of 'Code is read more than it is written'-Guido Van Rossum becomes evident. Becuase of this, the author would recommend that you are accustomed to [PEP-8](https://peps.python.org/pep-0008/) and [PEP-484](https://peps.python.org/pep-0484/). In addition, the [Google Python Style](https://google.github.io/styleguide/pyguide.html) guide has some very prudent suggestions worth reading. This, in conjunction with good naming practices and reasonable amounts of comments, makes deciphering code a feasible task. Such practices outlined in these documents will help the reader and future contributors collaborate and maintain this and other work.

## Git
Git can be used to version control code, and is almost universally used when collaborating on code projects, so that multiple people's changes do not ruin the existing codebase. In addition, websites like [GitHub](https://github.com/) provide free code repository hosting and a wealth of features. For solo projects, there is no need to use Git. However, it can be useful to work on projects from any machine anywhere. 