"""
This file (test_app.py) contains the unit tests for the app.py file.
"""
from app import StockModel


def test_validate_stock_data_nominal():
    """
    GIVEN a helper class to validate the form data
    WHEN valid data is passed in
    THEN check that the validation is successful
    """
    stock_data = StockModel(
        stock_symbol='SBUX',
        number_of_shares='100',
        purchase_price='45.67'
    )
    assert stock_data.stock_symbol == 'SBUX'
    assert stock_data.number_of_shares == 100
    assert stock_data.purchase_price == 45.67