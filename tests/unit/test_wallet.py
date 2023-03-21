"""
Unit tests for wallet.py package
"""
import pytest
from src.wallet import Wallet, InsufficientAmount
from tests.fixtures.wallet_fixtures import empty_wallet, wallet


def test_default_initial_amount(empty_wallet):
    """Tests that initial balance of empty_wallet is 0"""
    assert empty_wallet.balance == 0


def test_setting_initial_amount(wallet):
    """Tests that initial ballance of wallet is 20"""
    assert wallet.balance == 20


def test_wallet_add_cash(wallet):
    """Tests add_cash funciton"""
    wallet.add_cash(80)
    assert wallet.balance == 100


def test_wallet_spend_cash(wallet):
    """Tests spend_cash function"""
    wallet.spend_cash(10)
    assert wallet.balance == 10


def test_wallet_spend_cash_raises_exception_on_insufficient_amount(empty_wallet):
    """Tests that InsufficientAmount exception is raised when trying to spend more thant the wallet's balance"""
    with pytest.raises(InsufficientAmount):
        empty_wallet.spend_cash(100)
