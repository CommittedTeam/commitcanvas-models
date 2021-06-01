
class process:
  def __init__(self, data):
    types = ["feat","chore","docs","refactor","test","fix"]
    data = data[data["commit_type"].isin(types)]
    # drop commits made by the bots
    data = data[data["isbot"] != True]
    # drop duplicate commits if any
    data = data.drop_duplicates("commit_hash")
    # drop nan rows with nan values
    data = data.dropna()
    self.data = data

  def get_features(self):
    # list of columns that will be used for training
    features = ['commit_subject',"num_files","test_files","test_files_ratio","unique_file_extensions","num_unique_file_extensions","num_lines_added","num_lines_removed","num_lines_total"]
    train = self.data[features]

    return train

  def get_labels(self):

    # separate commit_type coloumn as list of lables
    return self.data["commit_type"]