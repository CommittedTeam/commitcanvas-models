"""Training and evaluating the model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import helpers
from commitcanvas_models.data_handling import statistics
import pandas as pd
import pingouin as pg
import joblib

app = typer.Typer()

@app.callback()
def callback():
    """
    please see the documentation regarding acceptable command line options
    """

@app.command()
def select(labels: str = "fix,feat,chore,docs,refactor,test", min_label: int = 50, subset: bool = False, subset_size: float = 0.50):
    """Select and save repositories for training"""
    data = pd.read_feather("data/angular_data.ftr")
    # select repositories that use the given labels and have at least given amount of commits per label
    filtered = helpers.filter_projects_by_label(data,labels,min_label)
    if subset:
        selected_set = helpers.select_projects_subset(filtered,subset_size)
    else:
        selected_set = helpers.map_language_to_name(filtered)

    # drop languages that have only one project
    filtered = helpers.drop_by_language(selected_set,1).reset_index(drop=True)

    # save the repository names for training
    filtered.to_csv("data_experiments/projects_metadata/training_repos.csv")


    print("\nSelected labels: ", labels)
    print("Minimum amount of commits required per label: ",min_label)
    if subset:
        print("ratio of subset: ", subset_size)
    print("\nTotal number of subset repositories",len(filtered.name))
    print(filtered.name)
    print("\nCount of programming languages")
    print(filtered.language.value_counts())

@app.command()
def train(data:str, save:str, types:str = "chore,docs,feat,fix,refactor,test"):
    '''
    Train the pipeline for deployment
    '''
    collected_data = pd.read_feather(data)
    print(collected_data)
    processed_data = md.data_prep(collected_data, types)
    print(processed_data)
    train_features,train_labels = md.feature_label_split(processed_data)

    pipeline = md.build_pipline()
    pipeline = pipeline.fit(train_features, train_labels)

    print("saving the model")
    joblib.dump(pipeline, "{}/trained_model.pkl".format(save))
    print("saving model complete")

    return pipeline

@app.command()
def experiment(mode: str,  save_report: str, split: float = 0.25):
    
    valid_modes = ['project','cross_project']
    if mode not in valid_modes:
        typer.echo("\nInvalid mode: {}. Valid modes are <project> and <cross_project. Please see the documentation for more details\n".format(mode))
        raise typer.Exit()

    filtered_data = md.select_training_data()
    md.report(filtered_data,mode,split,save_report)

@app.command()
def report(data_path):

    data = pd.read_csv("data_experiments/raw_predictions/{}".format(data_path))
    projects = data.name.unique()

    # collect classification report for each project
    report = []
    for project in projects:

        project_data = data[data["name"]==project]
        report.append(statistics.commitcanvas_classification_report(project_data,project))
      
    reports = pd.DataFrame(report)
    combined = reports.merge(statistics.get_training_set_count(data))
    print(combined)
    # save the report
    combined.to_csv("data_experiments/classification_reports/{}".format(data_path))

@app.command()
def plots(report_path, save, title:str = None):
    data_confusion_matrix = pd.read_csv("data_experiments/raw_predictions/{}".format(report_path),index_col=0)
    data_boxplot = pd.read_csv("data_experiments/classification_reports/{}".format(report_path),index_col=0)
    # box and whisker plots
    statistics.boxplot(data_boxplot,save,title = title)
    # plot the confusion matrix
    statistics.plot_confusion_matrix(data_confusion_matrix,save,title = title)

@app.command()
def mwu(path1: str, path2: str):
    scores = ['precision','recall','fscore']
    data1 = pd.read_csv("data_experiments/classification_reports/{}".format(path1))
    data2 = pd.read_csv("data_experiments/classification_reports/{}".format(path2))
    for score in scores:
        mwu_results = pg.mwu(data1[score], data2[score], tail='two-sided')
        print("\n Result for {}".format(score))
        print(mwu_results)



    

