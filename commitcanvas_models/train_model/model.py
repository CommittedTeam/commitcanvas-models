from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestClassifier
from commitcanvas_models.train_model.tokenizers import stem_tokenizer
from commitcanvas_models.train_model.tokenizers import dummy
import joblib
import os

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

def data_prep(data,labels):
  # TODO use loc instead
  labels = labels.split(",")
  data = data[data["commit_type"].isin(labels)]
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

  return (train,test)


def train_test_split(data,size):
  length = len(data)
  test_count = int(round((length*size),0))
  # newest commits are at the top of the dataframe
  train,test =  data.tail(length-test_count), data.head(test_count)
  return (train,test)

def save(pipeline,path):

  print("saving the model")
  joblib.dump(pipeline, "{}/trained_model.pkl".format(path))
  print("saving model complete")


def save(test,predicted,path):
  """Save the experimentation output"""
  # save the project name, commit hash and commit type
  # TODO update filter by column and use that
  true_pred = test.loc[:, ('name','commit_hash','commit_type')]
  true_pred["predicted"] = predicted
  
  # if file does not exist write header 
  if not os.path.isfile(path):
    true_pred.to_csv(path, header='column_names', index=False)
  else: # otherwise append without writing the header
    true_pred.to_csv(path, mode='a', header=False, index=False)


def report(data,mode,split,path):
  
  projects = data.name.unique()
  
  for repo in projects:
      print(repo)
      if mode == 'cross_project':

        # Train test split for cross project validation
        train,test = cross_val_split(data,repo)

        train_features,train_labels = feature_label_split(train)
        test_features,test_labels = feature_label_split(test)

      elif mode == 'project':
        project_data = data[data.name == repo]
        # Train test split for one project
        train,test = train_test_split(project_data,split)
        train_features,train_labels = feature_label_split(train)
        test_features,test_labels = feature_label_split(test)


      pipeline = build_pipline()
      pipeline.fit(train_features,train_labels)
      predicted = pipeline.predict(test_features) 
      save(test,predicted,path)
