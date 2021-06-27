# commitcanvas-models

## running the experiment

- clone the repository and navigate to `commitcanvas-model` branch. Then download the data release `data-0.1.0.tar.gz` from releases. Inside  `data-0.1.0.tar.gz` you will find `data` directory. Place it inside `commitcanvas_models` directory.
- `poetry install`
- `poetry shell`

### Train the model

- `commitcanvas train <mode> <save_report> <split>`

   - `mode` can be either `project` or `cross_project`. If `project` is selected then each repository listed in `data/training_data/training_repo.csv` will be split into train and test sets for experimentation. If `cross_project` is selected then each repository listed in `data/training_data/training_repo.csv` will be cross-project validated.

   - `save_report` path to save the report

   - `split` option takes the ratio. This ratio will be used as a size of the test set for the `project` mode. By default the value of `split` is 0.25. This means that if one project has 800 commits then top(chronologically newest) 200 will be set aside for testing, and the rest 600 will be used for training.

sample usage: `commitcanvas train project data_experiments/raw_predictions/project/90_10.csv --split 0.10`

### create classification reports

`commitcanvas report <data_path>`

input: `data_path` path to the raw data that has true and predicted labels. The data is located in `data_experimnets/raw_predictions`

output: the generated file will include weighted precision, recall, f-1, size of test set, size of train set and the size of total set for each label in each project. The file will be saved in `data_experimnets/classification_reports`. The file name will be same as the input file name.

sample usage:

Report for Project-specific with 60/40 train test split

`commitcanvas report 80_20.csv`

Report for project agnostic

`commitcanvas report project_agnostic.csv`


### Run statistical tests

`commitcanvas mwu <path1> <path2>`

Input: Paths to the classification report files.

Output: Mann-Whitney U Test and Vargha and Delaney effect size for precision, recall and f-1 scores

sample usage:

Project-specific split 75/25 vs Project-specific split 80/20
`commitcanvas mwu 75_25.csv 80_20.csv`

Project-agnostic vs Project-specific 80/20
`commitcanvas mwu project_agnostic.csv 80_20.csv`

### Generate plots

- `commitcanvas plots <report_path> <save> <title>`

Input:

  - `path` path to the file with specific split configuration
  - `save` name of the file where the plot will be saved
  - `title` title of the plot

Output:

confusion matrix and the boxplot will be saved in `data_experiments/plots`

boxplot stats such as median, mean, whishi, whislo. And get projects names near those values

sample usage:

`commitcanvas plots 80_20.csv project_specific_80_20.pdf --title "Project-Specific (80/20)"`


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

- training_repos.ftr

These repositories will be used in the experiments. Repositories included in this
file is subset of repositories in `projects_metadata/angular_repos.csv`. These repositories were selected since they at least use following labels `fix,feat,chore,refactor,test,docs` and have at least 50 commits per label