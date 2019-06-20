from web3 import Web3


class Collector():
    def __init__(self, logger, web3, db):
        self.logger = logger
        self.web3 = web3
        self.db = db

    def get_lastest_block_number(self):
        return self.web3.eth.blockNumber

    def pull(self):
        pass
