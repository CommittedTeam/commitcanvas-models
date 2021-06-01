"""Training and evaluating the classification model."""
import typer
from commitcanvas_models.train_model import model as md
# from commitcanvas_models.train_model.tokenizers import dummy
# from commitcanvas_models.train_model.tokenizers import stem_tokenizer
from commitcanvas_models.train_model import process
from sklearn.model_selection import train_test_split
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
    processed_data = process.data_prep(raw_data)
    features,labels = process.feature_label_split(processed_data)

    pipeline = md.build_pipline()
    pipeline.fit(features,labels)

    md.save(pipeline,save)

@app.command()
def test(data: str = None, model: str = None):
    """
    test the saved model with specified data and get classification report
    """
    # if no model than each repo in the test set will be individually validated
    repos = os.listdir(data)

    for repo_name in repos:

        raw_data = pd.read_feather("{}/{}".format(data,repo_name))
        processed_data = process.data_prep(raw_data)

        if model:
            test_features,test_labels = process.feature_label_split(processed_data)
            pipeline = joblib.load(model)   
            predicted = pipeline.predict(test_features)
        else:
            train_features,train_labels,test_features,test_labels = process.train_test_split(processed_data)
            pipeline = md.build_pipline()
            pipeline.fit(train_features,train_labels)
            predicted = pipeline.predict(test_features)

        md.report(test_labels,predicted)
            
        
        









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
