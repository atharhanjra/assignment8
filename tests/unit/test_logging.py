"""Tests that each operation writes the right log message."""

import logging

import pytest

from app.operations import add, subtract, multiply, divide


@pytest.mark.parametrize("operation, a, b, expected_message", [
    (add, 2, 3, "Add: 2 + 3 = 5"),
    (subtract, 5, 3, "Subtract: 5 - 3 = 2"),
    (multiply, 4, 5, "Multiply: 4 * 5 = 20"),
    (divide, 10, 2, "Divide: 10 / 2 = 5.0"),
])
def test_operation_logs_result(caplog, operation, a, b, expected_message):
    """Each successful operation logs its inputs and result at INFO level."""
    with caplog.at_level(logging.INFO):
        operation(a, b)
    assert expected_message in caplog.text


def test_divide_by_zero_logs_error(caplog):
    """Dividing by zero logs an ERROR before raising."""
    with caplog.at_level(logging.INFO):
        with pytest.raises(ValueError):
            divide(10, 0)
    assert "Divide: attempted to divide 10 by zero" in caplog.text
    assert caplog.records[-1].levelname == "ERROR"