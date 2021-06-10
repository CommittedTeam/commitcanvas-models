"""Get statistical information for the given data"""
import pandas as pd
from sklearn.metrics import precision_recall_fscore_support
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
import seaborn as sns

def label_total_ratio(data):
    # This function is not used yet
    print("ratio of commits for each label in the entire commit data")
    ratios = data.commit_type.value_counts(normalize=True)
    print(ratios)
    return ratios

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

def plot_confusion_matrix(data,save_plots,name):
  # this feature doens't work yet
  true = data.commit_type
  predicted = data.predicted

  labels = ['chore', 'docs', 'fix', 'feat', 'refactor', 'test']
  cm = confusion_matrix(true, predicted, normalize='true', labels=labels)

  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
  disp.plot(cmap='Greys')

  name = data['name'].tolist()[0]
  plt.savefig("{}/{}.jpg".format(save_plots,name))



project_75_25 = pd.read_csv("../classification_reports/project/classification_report_75_25.csv")
project_80_20 = pd.read_csv("../classification_reports/project/classification_report_80_20.csv")
project_60_40 = pd.read_csv("../classification_reports/project/classification_report_60_40.csv")
cross_project = pd.read_csv("../classification_reports/cross_project/classification_report.csv")

sns.boxplot(data=cross_project[["precision","recall","fscore"]],color='grey')
plt.savefig("../classification_reports/boxplots/cross_project")
