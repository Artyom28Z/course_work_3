import pytest

from src.funcions import executed_transactions


def test_information():
    assert isinstance(executed_transactions(), list)
