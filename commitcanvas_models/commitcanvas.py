"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
from commitcanvas_models.data_handling import selection
# from commitcanvas_models.train_model.tokenizers import dummy
# from commitcanvas_models.train_model.tokenizers import stem_tokenizer
import pandas as pd

app = typer.Typer()

@app.callback()
def callback():
    """
    please see the documentation regarding acceptable command line options
    """
from sklearn.metrics import classification_report
@app.command()
def train(cross: bool = False, project: bool = False, split: int = 25, labels: str = "fix,feat,chore,docs,refactor,test", min: int = 50, subset: bool = False, size: float = 0.25):
    ""
    # NOTE: should i shuffle the training set?
    data = pd.read_feather("data/angular_data.ftr")
    count = selection.commit_count_per_label(data)

    selected = selection.filter_by_label(count, labels, min).reset_index()


    name, language = selection.subset_selection(selected,size)

    print(name)
    print(len(name))
    print(language.value_counts())



    data = data[data['name'].isin(name.tolist())]
    print(data)
    projects = data.name.unique()
    data = md.data_prep(data)

    scorers = ['precision','recall','f1']
    classification_scores = {}
    for project in projects:
        
        if cross:
            "run cross validation"
            train_features,train_labels,test_features,test_labels = md.cross_val_split(data,project)

        elif project:
            "test each project"
            train_features,train_labels,test_features,test_labels = md.train_test_split(data,project,split)
        
        pipeline = md.build_pipline()
        pipeline.fit(train_features,train_labels)
        predicted = pipeline.predict(test_features)
        
        score = md.report(test_labels,predicted,scorers)
        classification_scores.update({project:score})

    print(pd.DataFrame.from_dict(classification_scores, orient='index',columns=scorers))






            
        
        









# @app.command()
# def train(url: str = None, types: str = "chore,docs,feat,fix,refactor,test", report: str = None, save: str = None):
#     """
#     random forest model with specified data
#     """

#     new_train = model(url, types)
#     pipeline = new_train.train_model()

#     if save:
#         new_train.save_model(pipeline)

#     if report:
#         new_train.get_report(pipeline)
