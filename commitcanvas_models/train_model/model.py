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
  model = RandomForestClassifier(random_state=42)

  # set up the pipeline with transformer and model
  pipeline = Pipeline(steps=[('prep',col_transform), ('model', model)])

  return pipeline

def report(labels,predicted):

  # display classification report
  types = labels.unique()

  print(labels.tolist())
  print(predicted)

  print(
  classification_report(labels, predicted, target_names=types, zero_division=0)
  )  

def save(pipeline,path):

  print("saving the model")
  joblib.dump(pipeline, "{}/trained_model.pkl".format(path))
  print("saving model complete")


