"""Get statistical information for the given data"""

import pandas as pd

def commit_count_per_label(data):
    """Count number of commits for each label in each repository."""
    repo = data[['name','commit_type']]
    grouped = pd.get_dummies(repo, columns=['commit_type'],dtype=int,prefix='', prefix_sep='').groupby(['name'], as_index=False).sum()
    return grouped

def label_frequency(grouped_data):
    """Count number of repositories per label."""
    print("\nHow many repositories use each commit label.")
    frequencies = grouped_data.drop("name",axis=1).astype(bool).sum(axis=0)
    print(frequencies)
    return frequencies

def label_total_ratio(data):
    print("ratio of commits for each label in the entire commit data")
    ratios = data.commit_type.value_counts(normalize=True)
    print(ratios)
    return ratios

"language stats", "criticality score stats"


data = pd.read_feather("../data/angular_data.ftr")
grouped_data = commit_count_per_label(data)
print(grouped_data)




# print(df.dropna())

