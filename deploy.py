from solcx import compile_standard

with open("./SimpleStorage.sol", "r") as file:
        simple_storage_file = file.read()
        print(simple_storage_file)

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
print(compile_sol)