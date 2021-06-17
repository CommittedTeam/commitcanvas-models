from sklearn.metrics import precision_recall_fscore_support
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import classification_report


raw_data = pd.read_csv("../classification_reports/cross_project/raw_prediction_output.csv",index_col=0)
project_names = ["angular-cli","sequelize"]
selected_projects = raw_data[raw_data["name"].isin(project_names)]


labels = ['chore', 'docs', 'fix', 'feat', 'refactor', 'test']

import numpy as np

def my_precision_recall(true,predicted,labels):

    cm = confusion_matrix(true, predicted,labels=labels)

    true_pos = np.diag(cm)
    false_pos = np.sum(cm, axis=0) - true_pos
    false_neg = np.sum(cm, axis=1) - true_pos

    precision = np.sum(true_pos / (true_pos + false_pos))/len(labels)
    recall = np.sum(true_pos / (true_pos + false_neg))/len(labels)

    return(precision,recall)


def scikit_learn_precision_recall(true,predicted):

    precision, recall, fscore, support = precision_recall_fscore_support(true,predicted,average="macro")
    return (precision,recall)


def print_classification_report(true,predicted):
    my_precision,my_recall = my_precision_recall(true, predicted,labels=labels)
    sci_precision,sci_recall = scikit_learn_precision_recall(true, predicted)

    print("My calculated precision: ",my_precision)
    print("My calculated recall: ",my_recall)
    print("Scikit presicion: ",sci_precision)
    print("Scikit recall",sci_recall)


# print classification report for each project
for name in project_names:

    project_specific_data = selected_projects[selected_projects["name"] == name]
    print("\nproject name: {}".format(name))
    print_classification_report(project_specific_data.commit_type,project_specific_data.predicted)


# print classificatin report for the full data (without splitting based on project name)
print("\nreport for full data")
print_classification_report(selected_projects.commit_type,selected_projects.predicted)