import pytest
import pandas as pd
import numpy as np
from numpy import nan

@pytest.fixture
def df():
  df = pd.read_excel(r'/content/sampledatafoodsales.xlsx')
  return df

# check if column exists
def test_column_check(df):
  name="ID"
  assert name in df.columns

# check for nulls
def test_null_check(df):
  assert df['Qty'].notnull().all()

# check values are unique
def test_unique_check(df):
  assert df['ID'].is_unique

# check data type 
def test_column_type_check(df):
  assert df['Qty'].dtype == 'int64'

# check values in range
def test_range_check(df):
  assert df['UnitPrice'].between(1,9).any()

# check values inrange
def test_string_in_column_check(df):
  assert df['City'].eq('Boston', 'New York').any()