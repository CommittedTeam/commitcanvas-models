"""Get statistical information for the given data"""

from commitcanvas_models.train_model.model import report
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import helpers

def label_total_ratio(data):
    print("ratio of commits for each label in the entire commit data")
    ratios = data.commit_type.value_counts(normalize=True)
    print(ratios)
    return ratios

def get_project_train_data(data):

  training_data = pd.read_feather("../data/training_data/processed_angular_data_droped_non_eng.ftr")
  project_name = data.name.tolist()[1]
  project_data = training_data[training_data['name'] == project_name]
  test_commits = data.commit_hash.tolist()
  project_train_data = project_data[~project_data['commit_hash'].isin(test_commits)]

  return project_train_data

def classification_report(data,project):

    true = data.commit_type
    predicted = data.predicted

    precision, recall, fscore, support = precision_recall_fscore_support(true,predicted,average='weighted',zero_division=0)

    data = {

            "name": project,
            "precision": round(precision,2),
            "recall": round(recall,2),
            "fscore": round(fscore,2)
        }

    return data

def plot_confusion_matrix(data, save):
  # this feature doens't work yet
  true = data.commit_type
  predicted = data.predicted

  labels = ['chore', 'docs', 'fix', 'feat', 'refactor', 'test']
  cm = confusion_matrix(true, predicted, normalize='true')

  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
  disp.plot(cmap='Greys')

  name = data['name'].tolist()[0]
  plt.savefig("{}/{}.jpg".format(save,name))

def stats(mode, save):

    if (mode == "project"):
        data = pd.read_csv("../data/classification_reports/project/split_80_20.csv")
    else:
        data = pd.read_csv("../data/classification_reports/cross_project/classification_report.csv")

    projects = data.name.unique()

    report = []
    test_label_count = []

    for project in projects:

        project_data = data[data["name"]==project]

        report.append(classification_report(project_data,project))

        test_label_count.append(project_data.commit_type.value_counts().to_dict())

        plot_confusion_matrix(project_data,save)
    # reports = pd.DataFrame(report)
    # test_counts = pd.DataFrame(test_label_count)
    # combined = pd.concat([reports,test_counts],axis=1)
    # combined.to_csv("computed_classification_report_project.csv")
    

stats("cross_project","../data/classification_reports")   

# import matplotlib.pyplot as plt
# import numpy as np
 
# project = pd.read_csv("computed_classification_report_project.csv").fscore
# # Creating dataset 
# cross_project = pd.read_csv("computed_classification_report_cross_project.csv").fscore

# # Import libraries
# import seaborn as sns

# np.random.seed(111)

# all_arr = [cross_project,
#            project]

# sns.boxplot(data=all_arr,color='grey')

# import matplotlib.pyplot as plt
# plt.savefig("boxplot_cross_project_and_project.jpg")
