"""Get statistical information for the given data"""

from commitcanvas_models.train_model.model import report
import pandas as pd


def label_total_ratio(data):
    print("ratio of commits for each label in the entire commit data")
    ratios = data.commit_type.value_counts(normalize=True)
    print(ratios)
    return ratios

