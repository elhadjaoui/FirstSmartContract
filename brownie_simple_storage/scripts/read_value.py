from brownie import SimpleStorage, accounts, config

def read_contract():
    simple_storage = SimpleStorage[-1] # [-1] go get the index thats one less then the length / get us the most recent deployment
    # ABI
    # Address

    print(simple_storage.retrieve())

def main():
    read_contract()