import pytest
from commitcanvas_models.train_model import model as md
import pandas as pd


data = {
    "name": ["group0", "group1", "group2", "group3", "group4", "group5", "group6", "group7" ],
    "id": [50, 40, 45, 60, 70, 54, 34, 46],
    }

df = pd.DataFrame(data)

def test_train_test_split():
    """Checks that project is split properly into train and test set"""
    selected = md.train_test_split(df,0.25)
    train,test = selected[0],selected[1]
    assert len(test) == 2
    assert len(train) == 6
    assert list(test.name) == ['group0','group1']

def test_cross_val_split():
    """Checks that one project at a time is held out"""
    train,test = md.cross_val_split(df,"group1")
    assert len(train) == 7
    assert len(test) == 1
    assert list(test.name) == ["group1"]

def test_feature_label_split():
    """Checks that correct columns are allocated to feature and label set"""
    df = pd.DataFrame(columns = ['commit_hash','commit_type','commit_subject',"num_files","test_files","test_files_ratio","unique_file_extensions","num_unique_file_extensions","num_lines_added","num_lines_removed","num_lines_total"])
    feature,label = md.feature_label_split(df)
    assert len(feature.columns) == 9
    