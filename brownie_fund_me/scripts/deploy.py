from tkinter.tix import Tree
from brownie import accounts, FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account

def deploy_fund_me():
    account = get_account()
    # if we are on a presistent network like rinkeby use the associated address, otherwise deploy mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
    else:
        print(f"the active network is {network.show_active()}")
        print(f"Deploying Mocks...")
        mock_v3_aggregator = MockV3Aggregator.deploy(18, 2000000000000000000, {"from":account })
        print(f"Mocks Deployed, address = {mock_v3_aggregator.address}.")
        price_feed_address = mock_v3_aggregator.address



    fund_me = FundMe.deploy(price_feed_address, {"from":account}, publish_source=True)
    print(f"our contract deployed to {fund_me.address}")


def main():
        deploy_fund_me()





