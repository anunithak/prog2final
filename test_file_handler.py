import pytest
from file_handler import FileHandler, AdvancedFileHandler, dice_generator


@pytest.fixture
def file1(tmp_path):
    f = tmp_path / "file1.txt"
    f.write_text("line1\nline2\n")
    return str(f)


@pytest.fixture
def file2(tmp_path):
    f = tmp_path / "file2.txt"
    f.write_text("line3\nline4\n")
    return str(f)


def test_read_lines(file1):
    f = FileHandler(file1)
    assert f.read_lines() == ["line1", "line2"]


def test_add_files(file1, file2):
    f1 = FileHandler(file1)
    f2 = FileHandler(file2)
    result = f1 + f2
    assert result.read_lines() == ["line1", "line2", "line3", "line4"]


def test_concat_multiple(file1, file2):
    adv = AdvancedFileHandler(file1)
    result = adv.concat_files(file1, file2)
    assert result.read_lines() == ["line1", "line2", "line3", "line4"]


def test_dice_gen():
    rolls = list(dice_generator(seed=40, n=5))
    assert rolls == [4, 5, 5, 1, 2]  # always same with seed=40
