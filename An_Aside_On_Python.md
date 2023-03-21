# An Aside On Python
As of writing, Python is the most popular [programming language](https://www.tiobe.com/tiobe-index/) globally. It is designed to be easy to use while not forgoing functionality. Python is famous for being slow compared to many languages. For non-production code, this is often not a problem. The syntax's ease of implementation, readability, and efficiency make it a superior choice for many scientific and industrial analysis applications, where speed is not the top priority.

In previous courses at Durham, The Jupyter Notebook format has probably been used. Running code on a pre-configured server like that in Level-2 discovery skills is straightforward. However, running off a local machine can become beneficial when projects grow in complexity and with more dependencies. [Anaconda](https://www.anaconda.com/) provides a straightforward way to get a Python install with lots of the commonly used scientific libraries. 

## Environments and Packages
Environments are designed so that when code is run somewhere else or at a different time, it still functions. Further, they contain any dependency problems one might encounter with packages. A package is a third party library for Python. For example, Tensorflow's compatibility with the newest version of Numpy is not guaranteed. To ensure that Numpy in other projects is up to date, but Tensorflow functions correctly. An environment can be made where the required version of both packages are kept, for said project. 

There are multiple different options for environments. However, this text recommends pip venvs for their compatibility with Jupyter Book. More can be read about setting up an environment like that in this book [here](./editing_the_book.md) 


## Readability and Naming
The development of readable maintainable code is not something often taught in an undergraduate Physics course. However, when working with others or on long projects, the veracity of 'Code is read more than it is written'-Guido Van Rossum becomes evident. Becuase of this, the author would recommend that you are accustomed to [PEP-8](https://peps.python.org/pep-0008/) and [PEP-484](https://peps.python.org/pep-0484/). In addition, the [Google Python Style](https://google.github.io/styleguide/pyguide.html) guide has some very prudent suggestions worth reading. This, in conjunction with good naming practices and reasonable amounts of comments, makes deciphering code a feasible task. Such procedures outlined in these documents will help the reader and future contributors collaborate and maintain 
this and other work.

Further, because people are fallible and consistency in code makes for easier reading, coding auto formatters such as [black](https://black.readthedocs.io/en/stable/) and [yapf](https://github.com/google/yapf) are helpful, as they make formatting more consistent.  

## Documentation
There is an extensive documentation website for most of the packages in this project. This is an extremely useful reference. Many of the features of the libraries are implemented excellently. One should avoid writing redundant code for which there is already a built-in function. Further,
```
help('some object')
``` 
prints out all of the docstrings and methods for the object. This can be very useful if recalling the exact details of an object is difficult.   

## Git
Git can be used to version control code and is almost universally used when collaborating on code projects, so that multiple people's changes do not ruin the existing codebase. In addition, websites like [GitHub](https://github.com/) provide free code repository hosting and a wealth of features. For solo projects, there is no need to use Git. However, it can be useful to work on projects from any machine anywhere. 