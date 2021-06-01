
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

def train_test_split(data):

  length = len(data)

  test_count = int(round(((length*25)/100),0))
  print("test count", test_count)
  train,test =  data.head(length-test_count), data.tail(test_count)
 
  print(train)
  print(test)

  train_features,train_labels = feature_label_split(train)
  test_features,test_labels = feature_label_split(test)

  return (train_features,train_labels,test_features,test_labels)