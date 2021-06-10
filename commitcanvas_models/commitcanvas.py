"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import helpers
from commitcanvas_models.data_handling import statistics
import pandas as pd
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

    data = pd.read_csv("data/training_data/training_repos.csv",index_col=0)

    # use processed data
    collected_data = pd.read_feather("data/training_data/angular_data.ftr")
    print("collected_data")
    print(collected_data)

    # # take the selected repositories for training
    filtered_data = collected_data[collected_data['name'].isin(data.name.tolist())]
    print("filtered data")
    print(filtered_data)

    # # NOTE: if you decide to run the classifier on raw data ensure to run the pre_processing steps
    labels = "fix,feat,chore,docs,refactor,test"

    filtered_data = md.data_prep(filtered_data,labels)

    print(filtered_data)

    md.report(filtered_data,mode,split,save_report)

# data/classification_reports/project/{}.csv
# data/classification_reports/cross_project/prediction_output.csv

@app.command()
def stats(data_path, save_report:str=None, save_plots:str=None):

    data = pd.read_csv(data_path)

    projects = data.name.unique()

    report = []
    test_label_count = []

    for project in projects:

        project_data = data[data["name"]==project]

        report.append(statistics.classification_report(project_data,project))

        test_label_count.append(project_data.commit_type.value_counts().to_dict())
        # save confusion matrix for each project
        statistics.plot_confusion_matrix(project_data,save_plots,project)


    # classification report for each project
    reports = pd.DataFrame(report)
    test_counts = pd.DataFrame(test_label_count)
    combined = pd.concat([reports,test_counts],axis=1)
    combined.to_csv(save_report)

    

