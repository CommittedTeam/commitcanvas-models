"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import selection
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
    # TODO counting the commits per label needs to be refactored
    data = pd.read_feather("data/data/training_data/angular_data.ftr")
    print(data)
    # select repositories that use the given labels and have at least given amount of commits per label
    filtered = selection.filter_projects_by_label(data,labels,min_label)
    print(filtered)
    if subset:
        selected_set = selection.select_projects_subset(filtered,subset_size)
    else:
        selected_set = selection.map_language_to_name(filtered)

    # drop languages that have only one project
    filtered = selection.drop_by_language(selected_set,1).reset_index(drop=True)

    # save the repository names for training
    filtered.to_csv("data/data/training_data/training_repos.csv")

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

    data = pd.read_csv("data/data/training_data/training_repos.csv",index_col=0)

    # use processed data
    collected_data = pd.read_feather("data/data/training_data/processed_angular_data.ftr")

    filtered_data = collected_data[collected_data['name'].isin(data.name.tolist())]
    print(data)

    # pre_process the data before training
    # labels = "fix,feat,chore,docs,refactor,test"
    # filtered_data = md.data_prep(filtered_data,labels)
    # filtered_data.reset_index(drop=True).to_feather("data/training_data/processed_angular_data.ftr")

    md.report(filtered_data,mode,split,save_report)

