## Setting up pip!

# What is pip?

Pip is a package manager for Python that allows us to install our projects dependencies
It connects to the Python Package Index(PyPI) which is an online repo of python packages

# Setting up our virutal environment

1. `python3 -m venv myvenv`
2. `source myvenv/bin/activate`

# Setting up pipreqs!

pipreqs is a python library that will create the requirements.txt file, which stores all the information about 
the projects dependencies. We can use this to install all the dependencies at once, meaning we don't have to individually
install all libraries with pip!

1. `pip install pipreqs`
2. `pipreqs ./ --ignore myvenv`

Now the requirements.txt file is created in the projects root!
To download all the dependencies:

`pip install -r requirements.txt`