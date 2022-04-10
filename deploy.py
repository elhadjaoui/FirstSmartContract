from solcx import compile_standard, install_solc
from web3 import  Web3
import  json

with open("./SimpleStorage.sol", "r") as file:
        simple_storage_file = file.read()

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
with open("./compiled_code.json", "w") as file:
        json.dump(compile_sol, file)

# get bytecode

# bytecode = compile_sol["contracts"]
