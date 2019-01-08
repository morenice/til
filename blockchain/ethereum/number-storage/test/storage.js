const BigNumber = require('bignumber.js')
const Storage = artifacts.require('Storage');

contract('Storage', function(accounts) {
  before(async function () {
    this.storage = await Storage.new();
  });

  it('should add number 10', async function() {
    await this.storage.addNumber(10);
    let num1 = await this.storage.getNumber(0);
    assert(num1.toNumber() === 10, 'Failed addNumber')
  });
});
