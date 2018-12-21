var PingPong = artifacts.require("PingPong");

module.exports = function(deployer) {
  deployer.deploy(PingPong);
};
