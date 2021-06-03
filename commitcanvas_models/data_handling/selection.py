import pandas as pd
from sklearn.model_selection import train_test_split

def filter_by_label(data, commit_types, min):
    """Select repositories that use given labels and have certain amount of commits per label"""
    # takes combined ftr file
    given_labels = commit_types.split(",")
    data = data.set_index("name")
    selected_columns = data[given_labels]
    selected_repos = selected_columns[selected_columns > min].dropna().astype(int)

    return selected_repos


def subset_selection(data, size):
    """Proportionate random subset selection based on the programming language"""
    # takes csv file with language counts
    repo_meta_data = pd.read_csv("data/angular_repos.csv")
    repo_languages = repo_meta_data[['name','language']]
    merged = pd.merge(data,repo_languages,on=['name'])

    data = merged[['name','language']].drop_duplicates().reset_index(drop=True)
    # dropt the repos that have Nan in language
    data = data.dropna()
    # drop languages that have only 1 instance
    data = data.groupby('language').filter(lambda x : len(x)>1)
      
    names = data.name
    languages = data.language

    X_train, X_test, y_train, y_test = train_test_split(
            names, languages,stratify=languages, test_size = size, shuffle=True)

    return (X_test,y_test)


def commit_count_per_label(data):
    """Count number of commits for each label in each repository."""
    repo = data[['name','commit_type']]
    grouped = pd.get_dummies(repo, columns=['commit_type'],dtype=int,prefix='', prefix_sep='').groupby(['name'], as_index=False).sum()
    return grouped


# data = {
#     "gator": [0.80,0.90,0.76],
#     "srverless": [0.40,0.98,0.76]
# }

# print(pd.DataFrame.from_dict(data, orient='index',columns=["accuracy",'precision','recall']))








# angular_repos = pd.read_feather("../data/angular_data.ftr")
# print(angular_repos.columns)

# repos = angular_repos.name.unique()
# print(repos)


# for repo in repos:
#     print(repo)
#     repo_sorted = angular_repos.loc[angular_repos['name'] == repo]
#     repo_sorted.reset_index(drop=True).to_feather("repos/{}.ftr".format(repo))



# raw_data = pd.concat(map(pd.read_feather, glob.glob('repo/*.ftr')))
# print(raw_data)
# print(raw_data.columns)




# data = pd.read_feather("../data/data.ftr")

# labels = data.commit_type.value_counts(normalize=True)
# print(labels.head(50))


# TODO: remove the column with test_files ratio, make sure to update the list of repos as well
# from commitcanvas_models.data_handling import stats












