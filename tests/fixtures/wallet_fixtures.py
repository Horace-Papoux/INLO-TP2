"""Necessary fixtures to test the wallet.py package"""
import pytest
from src.wallet import Wallet

# Wallet Fixtures
@pytest.fixture
def empty_wallet():
    """Returns a Wallet instance with a zero balance"""
    return Wallet()


@pytest.fixture
def wallet():
    """Returns a Wallet instance with a balance of 20"""
    return Wallet(20)


@pytest.fixture
def wallet_with_50_balance():
    """Returns a Wallet instance with a balance  of 50"""
    return Wallet(50)
