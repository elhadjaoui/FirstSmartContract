from dis import Bytecode
import json
import os
from solcx import compile_standard, install_solc 
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

with open("./SimpleStorage.sol", "r") as file:
        simple_storage_file = file.read()

install_solc("0.8.0")
compile_sol = compile_standard(
    {
    "language" : "Solidity",
    "sources": {"SimpleStorage.sol": {"content": simple_storage_file}},
    "settings":
    {
        "outputSelection": {
            "*":{"*":["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
        }
    },
    },
    solc_version="0.8.0"
)
with open("compiled_code.json", "w") as file :
    json.dump(compile_sol,file)

# get bytecode 
bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]

# get abi 
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connect to ganache:
w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/60173e525c114ac29c11a01b56f080a4'))
chainid = 4
my_address = "0xB879168AEDfF80B89792398a0Ce73Dd0e0238E1F"
private_key = os.getenv("PRIVATE_KEY")
# print(private_key)

# create the contract in python 
SimpleStorage  = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)

# ---------------------------------------Build Transaction -------------------------------------
print("Deploying contract...")
transaction = SimpleStorage.constructor().buildTransaction({ "gasPrice": w3.eth.gas_price, "chainId": chainid, "from": my_address, "nonce": nonce})
# print(transaction)

# ---------------------------------------Sign Transaction---------------------------------------
signed_transaction = w3.eth.account.sign_transaction(transaction, private_key)
# print(signed_transaction)

# ---------------------------------------Send Transaction---------------------------------------
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
# print(transaction_hash)
transaction_receipt = w3.eth.wait_for_transaction_receipt(transaction_hash)
print("Deployed.")
# print(transaction_receipt)

# we interact with blockchain with a call or trasact
# call -> Simulate making the call and getting a return value without change the state of the blockchain
# transact -> Make a state change 
Simple_Storage = w3.eth.contract(address=transaction_receipt.contractAddress, abi=abi)
print(Simple_Storage.functions.retrieve().call())

# ---------------------------------------Build Transaction -------------------------------------
print("Updating contract...")
store_transaction = Simple_Storage.functions.Store(22).buildTransaction({ "gasPrice": w3.eth.gas_price, "chainId": chainid, "from": my_address, "nonce": nonce + 1})
# ---------------------------------------Sign Transaction---------------------------------------
signed_store_transaction =  w3.eth.account.sign_transaction(store_transaction, private_key)
# ---------------------------------------Send Transaction---------------------------------------
stored_transactions_hash = w3.eth.send_raw_transaction(signed_store_transaction.rawTransaction)
# ---------------------------------------Wait for Transaction---------------------------------------
stored_transaction_receipt =  w3.eth.wait_for_transaction_receipt(stored_transactions_hash)
print("Updated.")
print(Simple_Storage.functions.retrieve().call())
