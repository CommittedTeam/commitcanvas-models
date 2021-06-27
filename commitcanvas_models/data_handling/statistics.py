"""Get statistical information for the given data"""
from sklearn.metrics import precision_recall_fscore_support
import pandas as pd
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import helpers
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats
import seaborn as sns

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

def plot_confusion_matrix(data,save,title=None):
  # this feature doens't work yet
  true = data.commit_type
  predicted = data.predicted

  labels = ['chore', 'docs', 'fix', 'feat', 'refactor', 'test']
  cm = confusion_matrix(true, predicted, labels=labels)

  disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
  disp.plot(cmap='Greys',values_format="d")

  plt.title(title,fontsize=14)
  plt.savefig("data_experiments/plots/matrix_{}".format(save))
      
def boxplot(plot_data, save: str=None, title: str=None):
    # make sure to fix the plot labels
    scores = ["precision","recall","fscore"]
    meanlineprops = dict(linestyle='--', color='black')
    # hide the median line
    medianlineprops = dict(linewidth=0)
    box_plot = sns.boxplot(data=plot_data[scores],color='grey',meanline=True, showmeans=True, meanprops=meanlineprops,medianprops=medianlineprops)
    plt.ylim(0.3, 0.9)
    plt.yticks(fontsize=14)
    plt.xticks([0,1,2], ["Precision","Recall","F-Score"], fontsize=14)
    

    for score in scores:
        stats = boxplot_stats(plot_data[score])
        mean = plot_data[round(plot_data[score],2) == round(stats[0]["mean"],2)]
        whishi = plot_data[plot_data[score] == stats[0]["whishi"]] 
        whislo = plot_data[plot_data[score] == stats[0]["whislo"]] 
        fliers =  plot_data[plot_data[score].isin(stats[0]["fliers"])]

        print("\nOverall boxplot stats for {}".format(score))
        print(stats)
        print("\nProjects close to value of mean")
        print(mean)
        print("\nProject at the value of whishi")
        print(whishi)
        print("\nProject at the value of whislo")
        print(whislo)
        if stats[0]["fliers"].any():
            print("\nFar outlier projects")
            print(fliers)
        print("\n")

        # style the boxplots
        x_pos = scores.index(score)
        mean_val = round(stats[0]['mean'],2)
        plt.text(
        x_pos, 
        mean_val, 
        f'{mean_val}', 
        ha='center',
        va='center',
        fontweight='bold', 
        size=10,
        color='black',
        bbox=dict(facecolor='#d3d3d3'))

    plt.title(title,fontsize=16)
    print(save)
    if save:
        plt.savefig("data_experiments/plots/boxplot_{}".format(save))

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