from dis import Bytecode
import json
from solcx import compile_standard, install_solc 
from web3 import Web3

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
bytecode = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]

# get abi 
abi = compile_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]

# connect to ganache:
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
chainid = 1337
my_address = "0xE7E7BE4ebE7775BE17f5c1eef9b87db83a163A18"
private_key = "e46585f5e64790b6a61456fb0a2a3ec2a8ba1bc7a824e3714d94bfcf01190ee4"

# create the contract in python 
SimpleStorage  = w3.eth.contract(abi=abi, bytecode=bytecode)
print(SimpleStorage)
nonce = w3.eth.getTransactionCount(my_address)
