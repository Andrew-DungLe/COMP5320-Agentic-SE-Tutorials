import pytest

from demo_app.core import normalise_task_title


def test_collapses_whitespace():
    assert normalise_task_title("  Write   tests  ") == "Write tests"


@pytest.mark.parametrize("bad", ["", "   ", "\n\t"])
def test_rejects_empty_titles(bad):
    with pytest.raises(ValueError):
        normalise_task_title(bad)
