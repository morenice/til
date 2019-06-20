import json
from collector.collector import Collector


class EventsCollector(Collector):
    def __init__(self, logger, web3, db, contract):
        super().__init__(logger, web3, db)
        self.contract_address = contract

    def pull(self):
        self.logger.info(
            'Start to collect transaction events of {}.'.format(self.contract_address)
        )
        # TODO...
