# commitcanvas-models

## running the experiment

- clone the repository and navigate to `commitcanvas-model` branch. Then download the data release `data-0.1.0.tar.gz` from releases. Inside  `data-0.1.0.tar.gz` you will find `data` directory. Place it inside `commitcanvas_models` directory.
- `poetry install`
- `poetry shell`
- `commitcanvas train <mode> <save_report> <split>`

   - `mode` can be either `project` or `cross_project`. If `project` is selected then each repository listed in `data/training_data/training_repo.csv` will be split into train and test sets for experimentation. If `cross_project` is selected then each repository listed in `data/training_data/training_repo.csv` will be cross-project validated.

   - `save_report` path to save the report

   - `split` option takes the ratio. This ratio will be used a size of the test set for the `project` mode. By default the value os `split` is 0.25. This means that if one project has 800 commits then top(chronologically newest) 200 will be set aside for testing, and the rest 600 will be used for training.



## Data Overview

## classification reports

classification reports are csv files that have three columns: `Commit hash`, `true labels`, `predicted labels`. 

- cross_project

    classification reports from cross project validation

- project

    classification reports once model is trained and tested on one repository

## project metadata

dataset of repositories that follow angular conventional commit guidelines.
csv file also includes other meta data such as dominant programming language,criticality score etc.

## training data

- angular_data.ftr

This dataset has commit data for over 300 repositories that follow angular conventional guidelines

- processed_angular_data.ftr

This dataset is pre-processed version of angular_data.ftr. preprocessing steps include removing commtis made by the bots, removing duplicate commits if any, removing rows with Nan values.

- training_repos.ftr

These repositories will be used in the experiments. Repositories included in this
file is subset of repositories in `projects_metadata/angular_repos.csv`. These repositories were selected sicne they at least use following labels `fix,feat,chore,refactor,test,docs` and have at least 50 commits per label