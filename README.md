# Cookiecutter Data Science
My personal adpation of a ...
> _... logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

Based on [Cookiecutter Data Science by drivendata](http://drivendata.github.io/cookiecutter-data-science/)


## Requirements to use the cookiecutter template:

 - Python 3.8+
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```


### To start a new project, run:
------------

    cookiecutter -c v1 https://github.com/jonaschu/cookiecutter-data-science


### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
│
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── reports            <- Generated analysis, reports as HTML, images, PDFs, etc.
│
├── test               <- Folder containing unit tests
│
├── YOUR_PACKAGE_NAME  <- Source code for use in this project. Name will be set during creation.
│   ├── __init__.py    <- Makes src a Python module
│   │
│   ├── data           <- Scripts to download or generate data
│   │   └── make_dataset.py
│   │
│   ├── features       <- Scripts to turn raw data into features for modeling
│   │   └── build_features.py
│   │
│   ├── models         <- Scripts to train models and then use trained models to make
│   │   │                 predictions
│   │   ├── predict_model.py
│   │   └── train_model.py
│   │
│   └── visualization  <- Scripts to create exploratory and results oriented visualizations
│       └── visualize.py
│
├──.env                <- File to store secrets/values that should not be comitted
│
├──.gitignore          <- .gitignore file filled with default values for various OS and IDEAs
│
└── README.md          <- The top-level README for developers using this project.
```
