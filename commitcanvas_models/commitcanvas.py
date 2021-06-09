"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import helpers
import pandas as pd
from joblib import Parallel, delayed
import time
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
    collected_data = pd.read_feather("data/training_data/data_natural_language.ftr")
    print("collected_data")
    print(collected_data)

    # # take the selected repositories for training
    filtered_data = collected_data[collected_data['name'].isin(data.name.tolist())]
    print("filtered data")
    print(filtered_data)

    # NOTE: if you decide to run the classifier on raw data ensure to run the pre_processing steps
    labels = "fix,feat,chore,docs,refactor,test"
    # # commit_messages = filtered_data["commit_subject"]

    # # for i in commit_messages:
    # #     print(i)
    # #     print(helpers.detect_lang(i))

    filtered_data = md.data_prep(filtered_data,labels)
    # # # Store the processed data
    # filtered_data.reset_index(drop=True).to_feather("data/training_data/processed_angular_data_droped_non_eng.ftr")

    start = time.time()
    md.report(filtered_data,mode,split,save_report)
    end = time.time()

    print(end-start)
    

