var storage = artifacts.require("./Storage.sol");

module.exports = function(deployer) {
  // Use deployer to state migration tasks.
    deployer.deploy(storage);
};
