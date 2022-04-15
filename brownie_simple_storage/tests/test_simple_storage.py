from brownie import SimpleStorage, accounts, network,config

def test_deploy():
    # Arrange
    account = get_account()
    #Act
    simple_storage = SimpleStorage.deploy({"from":account})
    # starting_value = simple_storage.retrieve()
    # expected = 0
    # Assert
    # assert starting_value == expected
    simple_storage.Store(15, {"from":account})
    expected = 15
    assert simple_storage.retrieve() == expected

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
