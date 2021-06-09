import pytest
import pandas as pd
from spacy import language
from commitcanvas_models.data_handling import helpers

data = {
    "num_lines_deleted": [0, 1, 47],
    "num_lines_added": [50, 40, 45],
    "num_lines_total": [50,41,48]
    }
df = pd.DataFrame(data)

def test_filter_columns():
    selected = helpers.filter_columns(df,["num_lines_added"])
    assert len(selected.columns) == 1

def test_filter_rows_by_value():
    selected = helpers.filter_rows_by_value(df,40)
    assert len(selected) == 1


def test_groupby_dummy_transformer():

    data = {
    "name": ["A","A","B","B","C","C"],
    "type": [1,2,3,1,4,2]
    }
    dt = pd.DataFrame(data)

    count = helpers.groupby_dummy_transformer(dt,"type","name")
    assert len(count.columns) == 5


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
     ((pd.DataFrame({"name":["angular","lerna", "vue", "docusaurus"],"language":["Javascript","TypeScript", "Javascript", "TypeScript"]}),0.50),(2,["Javascript","TypeScript"])),
     ((pd.DataFrame({"name":["axe-core","RSSHub", "lerna", "vant", "stencil", "vee-validate", "jina"],"language":["Javascript","Javascript", "Javascript", "Javascript", "TypeScript", "TypeScript","Python"]}),0.50),(3,["Javascript","Javascript","TypeScript"])),
     ],
)

def test_proportionate_subset_selection(input_data, expected_output):
    """Check ratio is maintained in the selected subset."""
    names, languages = helpers.proportionate_subset_selection(input_data[0],input_data[1])  
    assert expected_output[0] == len(names)
    assert set(expected_output[1]) == set(languages)

# The numbers in this dictionary are not real and are for only testing purposes
commit_type_data = {
    "name": ["angular", "angular", "angular", "angular", "serverless", "serverless", "serverless", "serverless" ],
    "commit_type": ["fix", "fix", "chore", "fix", "chore", "chore", "fix", "chore"],
    }

commit_type_data_frame = pd.DataFrame(commit_type_data)

@pytest.mark.parametrize(
    "input_data,expected_dataframe",
    [
     ((commit_type_data_frame,"fix", 2),(pd.DataFrame({"name":["angular"],"fix":[3]}))),
     ((commit_type_data_frame,"chore", 1),(pd.DataFrame({"name":["angular","serverless"],"chore":[1,3]}))),
     ((commit_type_data_frame,"chore,fix", 1),(pd.DataFrame({"name":["angular","serverless"],"chore":[1,3],"fix":[3,1]})))
    ],
)  
def test_filter_projects_by_label(input_data,expected_dataframe):
    """Check that projects are selected correctly"""
    filtered = helpers.filter_projects_by_label(input_data[0],input_data[1],input_data[2])
    assert set(filtered.all()) == set(expected_dataframe.all())

# make sure to test for the unknowns
@pytest.mark.parametrize(
    "input_text,expected_lang",
    [
     #("feat: add support for language detection to commitcanvas_models",'en'),
     ("chore: 补全作者名",'en'),
     ("fix: ეს მესიჯი არის ინგლისურ ენაზე",'en'),
     ('feat: este mensaje está en inglés','en')
    ],
)
def test_lang_detector_foreign_languages(input_text,expected_lang):
    lang = helpers.detect_lang(input_text)
    assert lang["language"] != expected_lang