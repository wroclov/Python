import pytest
import os
import sys

def pytest_generate_tests(metafunc):
    listing = os.listdir()
    csv_files = [item for item in listing if item.endswith('.csv')]
    if 'csv_file' in metafunc.fixturenames:
        metafunc.parametrize('csv_file', csv_files)

#@pytest.fixture(params = ['address.csv', 'book.csv', 'customer.csv'])
# instead of explicit list of csv files, it's read from dir with pytest_generate_tests(metafunc)
@pytest.fixture()
def csv_data(csv_file, request):
    with open(csv_file) as f:
        data = f.read().split('\n')
    #very optional
    def final_print():
        print("Initiated data for csv file")
    request.addfinalizer(final_print)
    return data

@pytest.fixture()
def csv_header(csv_data):
    return csv_data[0]

@pytest.fixture()
def columns_names(csv_header):
    return csv_header.split(",")

@pytest.fixture()
def csv_records(csv_data):
    return csv_data[1:]

def test_header_is_uppercase(csv_header):
    """ Check if columns are uppercase"""
    #print(csv_header)
    assert csv_header == csv_header.upper()

def test_header_starts_with_id(columns_names):
    """Checks if first column in header is id"""
    first_column_name = columns_names[0]
    #print(first_column_name)
    assert first_column_name == 'ID'

@pytest.mark.parametrize('checked_name', ['UPDATED', 'CREATED'])
def test_header_contains_column(columns_names, checked_name ):
    """Checks if in header row we've got specific column names"""
    assert checked_name in columns_names


def test_if_all_rows_have_same_column_length(columns_names, csv_records):
    """Checks if data in each row contains same number of columns"""
    header_length = len(columns_names)
    errors =[]
    for row in csv_records:
        if len(row.split(',')) != header_length:
            errors.append(row)
    assert not errors

def test_record_first_field_is_number(csv_records):
    """Checks if first value in each record is number"""
    errors=[]
    for record in csv_records:
        values_in_record = record.split(",")
        first_value_in_record = values_in_record[0]
        if not first_value_in_record.isdigit():
            errors.append(record)
    assert not errors



linux = pytest.mark.skipif(sys.platform != 'linux', reason="requires linux")
@linux
def test_func_skipped():
    """Test the function"""
    assert 0

xfail = pytest.mark.xfail

@xfail
def test_func_xfailed():
    """Test the function"""
    assert 0

@xfail
def test_hello():
    assert 0

@xfail(run=False)
def test_hello2():
    assert 0

@xfail("hasattr(os, 'sep')")
def test_hello3():
    assert 0

@xfail(reason="bug 110")
def test_hello4():
    assert 0

@xfail('pytest.__version__[0] != "17"')
def test_hello5():
    assert 0

def test_hello6():
    pytest.xfail("reason")

@xfail(raises=IndexError)
def test_hello7():
    x = []
    x[1] = 1
