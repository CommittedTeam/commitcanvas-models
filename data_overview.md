## Data Overview

### Select repositories for commit data collection

Select the repositories based on following criteria:

- open source project on Github
- criticality score higher than 0.60

    criticality score measures the importance of software repository. The algorithm uses metrics like number of stars on Github, contributor count, dependents count, commit frequency and so on. In this project we used latest(02/28/2021) release of list of repositories with computed criticality scores. The release can be accessed [here](https://commondatastorage.googleapis.com/ossf-criticality-score/index.html)

- commits in the repository follow angular's conventional commit standard.

 https://docs.google.com/document/d/1QrDFcIiPjSLDn3EL15IJygNPiHORgU1_OOAqWjiDU5Y/edit 
 
 https://github.com/angular/angular/blob/master/CONTRIBUTING.md

Highlights:

- The previous works do the similar work of labeling the commits by the maintanace activities. However, usually they use manually labeled commits for training(labeled by the researchers). This approach may fail to take into account the context once the commit was created and be error prone, and is also labor intensive. On the other hand, conventional commits are labeled by the developers in the software development process and we can automatically collect hundreds of thousands of such commits.

Threats to validity:

- We only looked at open source repositories since we only had access to those. This excludes many private repositories where commit message standards may be different.

- We don't have a guarantee that the commits were labeled correctly by the developers.By selecting highly critical repsitories we only increase the chance that the commits should be labeled properly, but we can't automatically eliminate mislabeled commits

 ### Commit data collection

 From the selected repositories we collected data for each commit that follows angular's conventional commit syntax.

`name`: name of the repository

`commit_hash`: commit hash

`commit_msg`: commit message

`commit_subject`: subject line of the commit message

`commit_type`: conventional label

`commit_author_name`: name of the commit author

`commit_author_email`: email of the commit author

`isbot`: determine if the commit was made by the bot based on the commit author name and email [supporting work](https://dl.acm.org/doi/abs/10.1145/3379597.3387478)       

`file_paths`: list of the file paths that were modified by the commit

`num_files`: number of files modified

`test_files`: number of files that could be related to the software testing [supporting work](https://softwareprocess.es/pubs/hindleICPC2009-large-changes-classification.pdf)

`unique_file_extensions`: list of unique file extensions

`num_unique_file_extensions`: number of file extensions

`num_lines_added`: total number of added lines as shown from –shortstat

`num_lines_removed`: total number of deleted lines as shown from –shortstat

`num_lines_total`: total number of added+deleted as shown from –shortstat

Highlights:

- these metrics are easy to collect and do not take much time compared to more complex source code analysis methods.


### Select repositories for experimentation

The most common labels are `chore`, `docs` `feat` `fix` `refactor` `test`

the repository should meet the following criteria

- have at least 50 commits for each conventional commit label
- the dominant programming language of the repositories is also used in at least one other repository(The idea is to drop programming languages that have only one repository represented in the dataset)

### Data pre-processing and feature engineering

#### data pre-processing steps

- Select commits that are labeled by one of the following  `chore`, `docs` `feat` `fix` `refactor` `test`
- check the duplicate commits from the dataset(based on commit hash). There were no duplicate commits identified
- Remove the commits that have bots 
- Remove rows with Nan values

#### selecting features

commit_subject: tokenize the commit message subject, select alpha tokens that are not stopwords, do stemming. do countvectorizer, tfidf on commit subjet data

num_files

num_test_files

test_files_ratio: ratio of test related files over total number of files modified

unique_file_extensions: find the most unique words for each label

num_unique_file_extensions: do countvectorizer, tfidf on unique file extensions

num_lines_added

num_lines_removed

num_lines_total

threats to validity:

- small number of commit messages may be in language other than english



### Data stats

The projects mentioned here have crticality score higher than 0.60. The projects have commits that follow conventional commit standard
- total number of projects for deployed model: 304
- total number of commits for training the deployed model: 515643

The projects mentioned here have crticality score higher than 0.60. And have at least 50 commits per label `chore`, `docs` `feat` `fix` `refactor` `test`
- total number of projects for experimentation: 54
- total number of commits used in experimentation: 213192







