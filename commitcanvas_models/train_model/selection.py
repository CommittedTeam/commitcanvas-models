import pandas as pd
from sklearn.model_selection import train_test_split

# once you use this function make sure to split the labels
#labels_list = column_names.split(",")
def filter_columns(data,column_names):
    """Keep selected columns in the dataframe."""   
    selected_columns = data[column_names]
    return selected_columns

#data = data.set_index("name") make sure to set the name as index
def filter_rows_by_value(data, min):
    """Select rows where each value is greater than the given min threshhold."""  
    rows = data[data > min].dropna().astype(int)
    return rows

# dummy_val is commit_type groupby is name
def groupby_dummy_transformer(data, dummy_val, groupby_val):
    """Groupby dummies based on given columns."""
    repo = data[[dummy_val,groupby_val]]
    grouped = pd.get_dummies(repo, columns=[dummy_val],dtype=int, prefix='', prefix_sep='').groupby([groupby_val], as_index=False).sum()
    return grouped

def proportionate_subset_selection(size, value, group):
    """Proportionate random subset selection.""" 
    # group will be language and the value will be name data[language] data[name]
    X_train, X_test, y_train, y_test = train_test_split(
            value, group, stratify = group, train_size = size, shuffle=True, random_state=42)

    return (X_train,y_train)

def filter_projects_by_label(data, labels, min_label_count):

    # count the number of commits per label in each repository
    count = groupby_dummy_transformer(data,'commit_type','name')
    # select the given labels
    selected_labels = filter_columns(count.set_index('name'),labels.split(","))
    # select repositories where count of commits in each label is higher than given threshold
    filtered_repos = filter_rows_by_value(selected_labels,min_label_count).reset_index()

    return filtered_repos

def map_language_to_name(dataset):
    repo_meta_data = pd.read_csv("data/angular_repos.csv")

    repos = filter_columns(repo_meta_data,['name','language'])
    repos = repos[repos["name"].isin(dataset.name.tolist())]
    return repos

def select_projects_subset(dataset,subset_size):
    # takes csv file with language counts
    # drop the repos that have Nan in language column
    dataset = map_language_to_name(dataset)
    data = dataset.dropna()
    # drop languages that have only 1 instance
    data = data.groupby('language').filter(lambda x : len(x)>1)

    # random proportionate repository selection based on the language
    name, language = proportionate_subset_selection(subset_size,data['name'],data['language'])

    return (name.reset_index(drop=True),language.reset_index(drop=True))