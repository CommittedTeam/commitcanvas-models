"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.train_model import selection
# from commitcanvas_models.train_model.tokenizers import dummy
# from commitcanvas_models.train_model.tokenizers import stem_tokenizer
import pandas as pd

app = typer.Typer()

@app.callback()
def callback():
    """
    please see the documentation regarding acceptable command line options
    """


@app.command()
def train(cross: bool = False, project: bool = False, split: float = 25, labels: str = "fix,feat,chore,docs,refactor,test", min_label: int = 50, subset: bool = False, subset_size: float = 0.50):
    # raise error if crossvalidation and project validation are selected at the same time
    data = pd.read_feather("data/angular_data.ftr")
    
    filtered = selection.filter_projects_by_label(data,labels,min_label)

    if subset:
        name,language = selection.select_projects_subset(filtered,subset_size)
    else:
        mapped = selection.map_language_to_name(filtered)
        name,language = mapped.name, mapped.language

    print("\nSelected labels: ", labels)
    print("Minimum amount of commits required per label: ",min_label)
    if subset:
        print("ratio of subset: ", subset_size)
    print("\nTotal number of subset repositories",len(name))
    print(name)
    print("\nCount of programming languages")
    print(language.value_counts())

    # Use the selected repositories in experimentation
    data = data[data['name'].isin(name.tolist())]  
    # pre_process the data before training
    data = md.data_prep(data,labels)
    md.report(data,cross,project,split)

