"""Get statistical information for the given data"""
from sklearn.metrics import precision_recall_fscore_support
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import helpers

def label_total_ratio(data):
    # This function is not used yet
    print("ratio of commits for each label in the entire commit data")
    ratios = data.commit_type.value_counts(normalize=True)
    print(ratios)
    return ratios

def commitcanvas_classification_report(data,project):

    true = data.commit_type
    predicted = data.predicted

    precision, recall, fscore, support = precision_recall_fscore_support(true,predicted,average='weighted',zero_division=0)

    data = {

            "name": project,
            "precision": precision,
            "recall": recall,
            "fscore": fscore
        }

    return data

def plot_confusion_matrix(data,save_plots,name=None,title=None):
  # this feature doens't work yet
  true = data.commit_type
  predicted = data.predicted

  labels = ['chore', 'docs', 'fix', 'feat', 'refactor', 'test']
  cm = confusion_matrix(true, predicted, labels=labels)

  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
  disp.plot(cmap='Greys',values_format="d")

  if name:
      plt.savefig("{}/{}.jpg".format(save_plots,name))
  else:
      plt.title(title,fontsize=14)
      plt.savefig(save_plots)
      
      
def get_training_set_count(test_data):

    filtered_data = md.select_training_data()

    train_data = filtered_data[~filtered_data["commit_hash"].isin(test_data.commit_hash)]

    train_grouped = helpers.groupby_dummy_transformer(train_data,'commit_type','name').set_index('name')
    test_grouped = helpers.groupby_dummy_transformer(test_data,'commit_type','name').set_index('name')
    total_grouped = helpers.groupby_dummy_transformer(filtered_data,'commit_type','name').set_index('name')

    train = train_grouped.add_suffix('_train')
    test = test_grouped.add_suffix('_test')
    total = total_grouped.add_suffix('_total')
    
    combined = pd.concat([total,train,test],axis=1).reset_index()

    return combined


def total_counts_commits(path):
    columns_sufixes = ["total","train","test"]

    project_data = pd.read_csv(path,index_col=0)

    for i in columns_sufixes:

        selected_columns = project_data.filter(regex='{}$'.format(i),axis=1)
        total = selected_columns.sum()
        print(total)
        print("\nTotal count of commits in {} set: ".format(i),total.sum(),"\n")