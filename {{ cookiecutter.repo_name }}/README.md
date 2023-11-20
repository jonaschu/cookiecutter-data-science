# {{cookiecutter.project_name}}

{{cookiecutter.description}}

## Start your project
1. Intialize a new poetry project
``` bash
poetry init
```
2. Add recommended dependecies
``` bash
poetry add python-dotenv # for .env support
```
3. Add recommended development dependecies
``` bash
poetry add --group=dev ipykernel # for notebook support
```
4. Install all packages
``` bash
poetry install
```
5. Intialize version control by git
```bash
git init
```
5. Prepare VS Code
    - Make sure that the extension 

## Project Organization
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
├── {{ cookiecutter.package_name }}  <- Source code for use in this project.
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

--------

<p><small>Project based on the apdated <a target="_blank" href="https://github.com/jonaschu/cookiecutter-data-science">cookiecutter data science project template</a> by jonaschu. #cookiecutterdatascience</small></p>
