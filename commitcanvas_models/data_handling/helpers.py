"""Select repositories"""
import pandas as pd
from sklearn.model_selection import train_test_split


def filter_columns(data,column_names):
    """Keep selected columns in the dataframe."""   
    selected_columns = data[column_names]
    return selected_columns

def filter_rows_by_value(data, min):
    """Select rows where each value is greater than the given min threshhold."""  
    rows = data[data > min].dropna().astype(int)
    return rows

def groupby_dummy_transformer(data, dummy_val, groupby_val):
    """Groupby dummies based on given columns."""
    repo = data[[dummy_val,groupby_val]]
    grouped = pd.get_dummies(repo, columns=[dummy_val],dtype=int, prefix='', prefix_sep='').groupby([groupby_val], as_index=False).sum()
    return grouped

def proportionate_subset_selection(data,size):
    """Proportionate random subset selection.""" 
    # group will be language and the value will be name data[language] data[name]
    data = drop_by_language(data,1)
    value,group = data['name'],data['language']
    X_train, X_test, y_train, y_test = train_test_split(
            value, group, stratify = group, train_size = size, shuffle=True, random_state=42)

    return (X_train,y_train)

def filter_projects_by_label(data, labels, count):

    # Take repositories that use at least goven commit labels
    selected_commits = data[data['commit_type'].isin(labels.split(","))]

    # count number of commits per label in each repository
    grouped_labels = groupby_dummy_transformer(selected_commits,'commit_type','name')
    
    # only keep the repositories that have at least 50 commmits per label group
    filtered_repos = filter_rows_by_value(grouped_labels.set_index('name'),count).reset_index()

    return filtered_repos

def map_language_to_name(dataset):
    repo_meta_data = pd.read_csv("data/projects_metadata/angular_repos.csv")

    repos = filter_columns(repo_meta_data,['name','language'])
    repos = repos[repos["name"].isin(dataset.name.tolist())]
    return repos

def drop_by_language(data,count):
    data = data.groupby('language').filter(lambda x : len(x)>count)
    return data

# NOTE: this feature most likely will not be used
def select_projects_subset(dataset,subset_size):
    # takes csv file with language counts
    # drop the repos that have Nan in language column
    dataset = map_language_to_name(dataset)
    data = dataset.dropna()
 
    # random proportionate repository selection based on the language
    name, language = proportionate_subset_selection(subset_size,data)
    selected = pd.concat([name, language], axis=1).reset_index(drop=True)
    return selected