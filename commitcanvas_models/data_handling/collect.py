from reporover import reporover





  plot_confusion_matrix(labels,predicted, display_labels=types,cmap='Blues',normalize="true")
  plt.show()  


# list_ = pd.read_csv("data/new_repos.csv")
# urls = list_.url.tolist()

# print(urls)

# for url in urls:
#     commit_data = pd.DataFrame(parse.get_commit_data(url))   
#     print(commit_data)
#     commit_data.to_feather("data/repos/{}.ftr".format(commit_data.name[0]))

# def get_repo_path(url):
#     """Get full repository name from the url"""
#     parsed = giturlparse.parse(url)
#     path = parsed.pathname[1:]
#     return path

# @pytest.mark.parametrize(
#     "input_url,expected_path",
#     [
#       ("https://github.com/GatorEducator/gatorgrader", "GatorEducator/gatorgrader"),
#       ("https://github.com/CommittedTeam/CommitCanvas","CommittedTeam/CommitCanvas"),
#       ("https://github.com/rust-lang/rust", "rust-lang/rust")
#     ]
# )
# def test_get_repo_path(input_url, expected_path):
#     path = get_convention.get_repo_path(input_url)
#     assert path == expected_path 