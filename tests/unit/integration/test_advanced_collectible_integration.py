from scripts.helpful_scripts import (
    LOCAL_BLOCKCHAIN_ENVIRONMENT,
    get_account,
    get_contract,
)
from brownie import network
import pytest
import time
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_advanced_collectible_integration():
    # Arrange
    if network.show_active()  in LOCAL_BLOCKCHAIN_ENVIRONMENT:
        pytest.skip("Test en integration seulement")
    # Act
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(60)
    # Assert
    assert advanced_collectible.tokenCounter() == 1
 
