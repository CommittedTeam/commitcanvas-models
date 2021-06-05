"""Get statistical information for the given data"""

import pandas as pd

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


labels = pd.read_csv("../classification_reports/project/test_75_25.csv")
print(labels)