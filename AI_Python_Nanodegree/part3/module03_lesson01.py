"""
This module is about OOP concepts

class: vessel (sacha) to create different objects. blueprint




Conda:



Anaconda is actually a distribution of software that comes with conda, Python, and over 150 scientific packages and their dependencies.
The application conda is a package and environment manager.

package related:
conda install package
conda remove package
conda update --all
conda search *search_item*

managing environments:
conda create -n env_name python=3.3 list of packages
source activate my_env
conda env export > environment.yaml
conda env create -f environment.yaml
conda env remove -n env_name

also include include a pip requirements.txt file using pip freeze
for people not using conda


Pyjupiter
conda install jupyter notebook
jupyter notebook    ->   http://localhost:8888
conda install nb_conda  ->   Notebook Conda to help manage your environments

Here we will talk about jupyter notebook and conda

install miniconda, it is small with minimum packages, you can install other packages later

if you face inssue in older environment not getting detected by jupyter, ipykernel may be missing from old env

: first create conda env
activate myenv   : or activate D:/path/to/env
conda install ipykernel  : if you face issue of SSL error in above code
path = %path%;C:\Miniconda3;C:\Miniconda3\Scripts;C:\Miniconda3\Library\bin;    : add minoconda in path env

conda install jupyter notebook    : First install jupyter notebook
jupyter notebook     : to launch server  http://localhost:8888
conda install nb_conda  : Notebook Conda to help manage your environments

: you can create one env and use it for many projects
"""