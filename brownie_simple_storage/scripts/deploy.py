import imp
from brownie import accounts, config, SimpleStorage, network
import os

def deploy_simple_storage():
    account = get_account()
    # account = accounts.load("simo-account")
    # account = accounts.add(os.getenv("PRIVATE_KEY"))
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    transaction = simple_storage.Store(15, {"from":account})
    transaction.wait(1)
    stored_value_updated = simple_storage.retrieve()
    print(stored_value_updated)

def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
        deploy_simple_storage()