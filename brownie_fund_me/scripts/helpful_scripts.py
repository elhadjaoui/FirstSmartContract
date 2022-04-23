from brownie import accounts, FundMe, network, config, MockV3Aggregator
from web3 import Web3

DECIMALS = 18 
STARTING_PRICE = 2000


def get_account():
    print(network.show_active())
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mock():
    print(f"the active network is {network.show_active()}")
    print(f"Deploying Mocks...")
    if len(MockV3Aggregator)  <=  0 :
        MockV3Aggregator.deploy(DECIMALS, Web3.toWei(STARTING_PRICE, "ether"), {"from":get_account()})
        print(f"Mocks Deployed, address = {MockV3Aggregator[-1].address}.")