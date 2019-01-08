pragma solidity ^0.5.0;


contract Storage {
    uint[] private _numberStorage;

    constructor() public {
    }

    event AddedNewNumber(uint position);

    function addNumber(uint newNumber) public returns (uint) {
        _numberStorage.push(newNumber);

        uint numberPosition = _numberStorage.length - 1;

        emit AddedNewNumber(numberPosition);
        return numberPosition;
    }

    function getNumber(uint position) public view returns (uint) {
        return _numberStorage[position];
    }

}
