"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
# from commitcanvas_models.train_model.tokenizers import dummy
# from commitcanvas_models.train_model.tokenizers import stem_tokenizer
from commitcanvas_models.data_handling import process
import pandas as pd
import joblib
import glob
import os

app = typer.Typer()

@app.callback()
def callback():
    """
    please see the documentation regarding acceptable command line options
    """


@app.command()
def train(data: str, save: str):
    """
    train random forest model.

    provide the directory that has training data files
    """
 
    raw_data = pd.concat(map(pd.read_feather, glob.glob('{}/*.ftr'.format(data))))
   
    data_processing = process.process(raw_data)
    features = data_processing.get_features()
    labels = data_processing.get_labels()

    train_model = md.model_helpers(features,labels)
    pipeline = train_model.train()
    print("training complete")

    train_model.save(pipeline,save)

@app.command()
def test(data: str = None, model: str = None):
    """
    test the saved model with specified data and get classification report
    """
    # if no model than each repo in the test set will be individually validated
    repos = os.listdir(data)

    for repo_name in repos:
        raw_data = pd.read_feather("{}/{}".format(data,repo_name))
        data_processing = process.process(raw_data)
        if model:
            features = data_processing.get_features()
            labels = data_processing.get_labels()

            pipeline = joblib.load(model)   
            predicted = pipeline.predict(features)
        # else:
        #     test,train = repo
        #     model.train(train)
        #     model.test(test)

        train_model = md.model_helpers(features,labels)
        train_model.report(pipeline,predicted)







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
