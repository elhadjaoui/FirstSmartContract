// SPDX-License-Identifier: GPL-3.0

pragma solidity ^0.8.0;

// Defining a contract
contract SimpleStorage {
    uint256 FavoriteNumber;
    struct People {
        uint256 favN;
        string name;
    }

    People[] public newPeople;
    mapping(string => uint256) public nameToFavN;

    function Store(uint256 _number) public {
        FavoriteNumber = _number;
    }

    function retrieve() public view returns (uint256) {
        return FavoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favN) public {
        newPeople.push(People(_favN, _name));
        nameToFavN[_name] = _favN;
    }
}
