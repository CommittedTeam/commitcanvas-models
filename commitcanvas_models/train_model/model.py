from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt
from commitcanvas_models.train_model.tokenizers import stem_tokenizer
from commitcanvas_models.train_model.tokenizers import dummy
from sklearn.metrics import get_scorer
import joblib


def build_pipline():

  # steps for processing the commit subject
  subject = "commit_subject"
  subject_transformer = Pipeline(steps = [('vect', CountVectorizer(tokenizer=stem_tokenizer)),
                                          ('tfidf', TfidfTransformer()),
  ])

  # steps for processing file extensions
  extension = "unique_file_extensions"
  extension_transformer = Pipeline(steps = [('vect', CountVectorizer(tokenizer=dummy,preprocessor=dummy)),
                                          ('tfidf', TfidfTransformer()),
  ])

  # create transformer steps
  t = [('subject', subject_transformer, subject),
      ('extension', extension_transformer,extension)]

  # set remainder as passthrough so that the other columns don't get lost
  col_transform = ColumnTransformer(transformers=t,remainder="passthrough")
  model = RandomForestClassifier(random_state=42,n_jobs=-1)

  # set up the pipeline with transformer and model
  pipeline = Pipeline(steps=[('prep',col_transform), ('model', model)])

  return pipeline

def data_prep(data):
  types = ["feat","chore","docs","refactor","test","fix"]
  data = data[data["commit_type"].isin(types)]
  # drop commits made by the bots
  data = data[data["isbot"] != True]
  # drop duplicate commits if any
  data = data.drop_duplicates("commit_hash")
  # drop nan rows with nan values
  data = data.dropna()
  return data

def feature_label_split(data):
  feature_columns = ['commit_subject',"num_files","test_files","test_files_ratio","unique_file_extensions","num_unique_file_extensions","num_lines_added","num_lines_removed","num_lines_total"]
  features = data[feature_columns]
  labels = data["commit_type"]

  return (features,labels)

def cross_val_split(data,project):

  train = data[data.name != project]
  test = data[data.name == project]
  
  train_features,train_labels = feature_label_split(train)
  test_features,test_labels = feature_label_split(test)

  return (train_features,train_labels,test_features,test_labels)

def train_test_split(data,project,size):
  
  data = data[data.name == project]
  length = len(data)

  test_count = int(round(((length*size)/100),0))
  train,test =  data.head(length-test_count), data.tail(test_count)
 
  train_features,train_labels = feature_label_split(train)
  test_features,test_labels = feature_label_split(test)

  return (train_features,train_labels,test_features,test_labels)

def report(true,predicted,scorers):

  scores = [get_scorer(score)._score_func(true, predicted,average="weighted",zero_division=0) for score in scorers]

  return scores

def save(pipeline,path):

  print("saving the model")
  joblib.dump(pipeline, "{}/trained_model.pkl".format(path))
  print("saving model complete")


