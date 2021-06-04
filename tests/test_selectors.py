import pytest
import pandas as pd
from commitcanvas_models.train_model import selection

data = {
    "num_lines_deleted": [0, 1, 47],
    "num_lines_added": [50, 40, 45],
    "num_lines_total": [50,41,48]
    }
df = pd.DataFrame(data)

def test_filter_columns():
    selected = selection.filter_columns(df,["num_lines_added"])
    assert len(selected.columns) == 1

def test_filter_rows_by_value():
    selected = selection.filter_rows_by_value(df,40)
    assert len(selected) == 1


def test_groupby_dummy_transformer():

    data = {
    "name": ["A","A","B","B","C","C"],
    "type": [1,2,3,1,4,2]
    }
    dt = pd.DataFrame(data)

    count = selection.groupby_dummy_transformer(dt,"type","name")
    assert len(count.columns) == 5


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
     ((0.50,["angular","lerna", "vue", "docusaurus"],["Javascript","TypeScript", "Javascript", "TypeScript"]),(2,2)),
    ],
)
def test_proportionate_subset_selection(input_data, expected_output):
    """Check ratio is maintained in the selected subset."""
    names, languages = selection.proportionate_subset_selection(input_data[0],input_data[1],input_data[2])   
    assert expected_output == (len(names),len(languages))