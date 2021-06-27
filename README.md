# commitcanvas-models

## Set up the environment

- clone the repository.
- Download the data `angular_data.ftr` from releases. Place the file inside `comitcanvas_models/data`
- Install [poetry](https://python-poetry.org/) or ensure that you have all the dependencies listed in `pyproject.toml` installed
- Install the dependencies `poetry install`
- Enter poetry shell `poetry shell`

## Commands for experiments

### Train the model

- `commitcanvas train <mode> <save_report> <split>`

   - `mode` can be either `project` or `cross_project`. If `project` is selected then each repository listed in `data/training_data/training_repo.csv` will be split into train and test sets for experimentation. If `cross_project` is selected then each repository listed in `data/training_data/training_repo.csv` will be cross-project validated.

   - `save_report` path to save the report

   - `split` option takes the ratio. This ratio will be used as a size of the test set for the `project` mode. By default the value of `split` is 0.25. This means that if one project has 800 commits then top(chronologically newest) 200 will be set aside for testing, and the rest 600 will be used for training.

sample usage: `commitcanvas train project data_experiments/raw_predictions/project/90_10.csv --split 0.10`

### Create classification reports

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

### Project metadata

List of repositories that follow angular's conventional commit guidelines.
The files also includes other meta data such as dominant programming language,criticality score etc.

[repositories for deployed model](data_experiemnts/projects_metadata/angualr_repos.csv)

[repositories for experimentation](data_experiemnts/projects_metadata/training_repos.csv)

### Data stats

The projects for deployed model have crticality score higher than 0.60. The projects have commits that follow conventional commit standard
- total number of projects for deployed model: 304
- total number of commits for training the deployed model: 515643

The projects for experimentation have crticality score higher than 0.60. And have at least 50 commits per label `chore`, `docs` `feat` `fix` `refactor` `test`
- total number of projects for experimentation: 54
- total number of commits used in experimentation: 213192