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
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:1337'))
chainid = 1337
my_address = "0x7d0fEE1f9a8D119C6A906667732675cC49cd49d9"
private_key = os.getenv("PRIVATE_KEY")
print(private_key)

# create the contract in python 
SimpleStorage  = w3.eth.contract(abi=abi, bytecode=bytecode)
# print(SimpleStorage)
nonce = w3.eth.getTransactionCount(my_address)
# print(nonce)

# Build Transaction -------------------------------------
transaction = SimpleStorage.constructor().buildTransaction({ "gasPrice": w3.eth.gas_price, "chainId": chainid, "from": my_address, "nonce": nonce})
# print(transaction)

# Sign Transaction---------------------------------------
signed_transaction = w3.eth.account.sign_transaction(transaction,private_key)
# print(signed_transaction)

# Send Transaction
transaction_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
print(transaction_hash)
