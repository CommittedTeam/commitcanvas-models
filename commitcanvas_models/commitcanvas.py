"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import helpers
from commitcanvas_models.data_handling import statistics
import pandas as pd
import seaborn as sns
import pingouin as pg
import matplotlib.pyplot as plt
from matplotlib.cbook import boxplot_stats
# from commitcanvas_models.train_model.tokenizers import dummy
# from commitcanvas_models.train_model.tokenizers import stem_tokenizer

app = typer.Typer()

@app.callback()
def callback():
    """
    please see the documentation regarding acceptable command line options
    """

@app.command()
def select(labels: str = "fix,feat,chore,docs,refactor,test", min_label: int = 50, subset: bool = False, subset_size: float = 0.50):
    """Select and save repositories for training"""
    data = pd.read_feather("data/training_data/angular_data.ftr")
    # select repositories that use the given labels and have at least given amount of commits per label
    filtered = helpers.filter_projects_by_label(data,labels,min_label)
    if subset:
        selected_set = helpers.select_projects_subset(filtered,subset_size)
    else:
        selected_set = helpers.map_language_to_name(filtered)

    # drop languages that have only one project
    filtered = helpers.drop_by_language(selected_set,1).reset_index(drop=True)

    # save the repository names for training
    filtered.to_csv("data/training_data/training_repos.csv")


    print("\nSelected labels: ", labels)
    print("Minimum amount of commits required per label: ",min_label)
    if subset:
        print("ratio of subset: ", subset_size)
    print("\nTotal number of subset repositories",len(filtered.name))
    print(filtered.name)
    print("\nCount of programming languages")
    print(filtered.language.value_counts())

@app.command()
def train(mode: str,  save_report: str, split: float = 0.25):
    
    valid_modes = ['project','cross_project']
    if mode not in valid_modes:
        typer.echo("\nInvalid mode: {}. Valid modes are <project> and <cross_project. Please see the documentation for more details\n".format(mode))
        raise typer.Exit()

    filtered_data = md.select_training_data()

    md.report(filtered_data,mode,split,save_report)

# data/classification_reports/project/{}.csv
# data/classification_reports/cross_project/prediction_output.csv

@app.command()
def report(data_path, save_report:str=None, save_plots:str=None):

    data = pd.read_csv(data_path)

    projects = data.name.unique()

    report = []
    for project in projects:

        project_data = data[data["name"]==project]

        report.append(statistics.classification_report(project_data,project))
        # save confusion matrix for each project
        if save_plots:
            statistics.plot_confusion_matrix(project_data,save_plots,project)


    # classification report for each project
    reports = pd.DataFrame(report)
    combined = reports.merge(statistics.get_training_set_count(data))
    print(combined)
    if save_report:
        combined.to_csv(save_report)


@app.command()
def statistical_tests(path1: str, path2: str):
    scores = ['precision','recall','fscore']
    data1 = pd.read_csv(path1)
    data2 = pd.read_csv(path2)
    for score in scores:
        mwu_results = pg.mwu(data1[score], data2[score], tail='one-sided')
        print("\n Result for {}".format(score))
        print(mwu_results)

# save "../classification_reports/boxplots/cross_project"
@app.command()
def plot_boxplot(plot_data_path: str, save: str=None):
    # make sure to fix the plot labels
    plot_data = pd.read_csv(plot_data_path,index_col=0)
    scores = ["precision","recall","fscore"]
    sns.boxplot(data=plot_data[scores],color='grey')
    for score in scores:
        stats = boxplot_stats(plot_data[score])
        median = plot_data[plot_data[score] == round(stats[0]["mean"],2)]
        whishi = plot_data[plot_data[score] == stats[0]["whishi"]] 
        whislo = plot_data[plot_data[score] == stats[0]["whislo"]] 
        fliers =  plot_data[plot_data[score].isin(stats[0]["fliers"])]

        print("\nOverall boxplot stats for {}".format(score))
        print(stats)
        print("\nProject at the value of median")
        print(median)
        print("\nProject at the value of whishi")
        print(whishi)
        print("\nProject at the value of whislo")
        print(whislo)
        print("\nFar outlier projects")
        print(fliers)
        print("\n")

    if save:
        plt.savefig(save)


    

