import pytest
import sys, os
sys.path.append(os.path.join(sys.path[0],'file_processing'))
from file_processing.file import File

variable_names = "path, text_length, encoding, num_rows, num_cols, num_cells, empty_cells"
values = [
   ('tests/resources/test_files/2021_Census_English.csv', 6084302, 'ISO-8859-1', 36835, 23, 847205, 253932),
   ('tests/resources/test_files/Approved_Schools_2023_10_01.csv', 1403268, 'UTF-8-SIG', 5385, 13, 70005, 73)
]


@pytest.mark.parametrize(variable_names, values)
def test_csv_metadata(path, text_length, encoding, num_rows, num_cols, num_cells, empty_cells):
    file_obj = File(path)
    assert len(file_obj.metadata['text']) == text_length
    assert file_obj.metadata['encoding'] == encoding
    assert file_obj.metadata['num_rows'] == num_rows
    assert file_obj.metadata['num_cols'] == num_cols
    assert file_obj.metadata['num_cells'] == num_cells
    assert file_obj.metadata['empty_cells'] == empty_cells


@pytest.mark.parametrize(variable_names, values)
def test_save_csv_metadata(copy_file, text_length, encoding, num_rows, num_cols, num_cells, empty_cells):
    test_csv_metadata(copy_file, text_length, encoding, num_rows, num_cols, num_cells, empty_cells)


@pytest.mark.parametrize("path", map(lambda x: x[0], values))
def test_csv_invalid_save_location(invalid_save_location):
    invalid_save_location


corrupted_files = [
    'tests/resources/test_files/2021_Census_English_corrupted.csv'
]

@pytest.mark.parametrize("path", corrupted_files)
def test_csv_corrupted_file_processing(corrupted_file_processing):
    corrupted_file_processing