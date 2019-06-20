import json
import time
from collector.collector import Collector


class TransactionCollector(Collector):
    def __init__(self, logger, web3, db):
        super().__init__(logger, web3, db)

    def __get_transaction(self, from_block, to_block):
        """
        TODO:
         parallel execute for performance or async/await
        """
        self.logger.info('Get block from {0} to {1}'.format(from_block, to_block))

        for idx in range(from_block, to_block, 1):
            block = self.web3.eth.getBlock(idx)
            transactions = block['transactions']
            timestamp = block['timestamp']

            self.logger.info(
                'block {}, parent {}, txn {} count, {} timestamp'.format(
                    idx,
                    block['parentHash'].hex(),
                    len(transactions),
                    timestamp
                )
            )

            txn_list = []
            for t in transactions:
                t_info = self.web3.eth.getTransaction(t)
                summary_txn = dict()
                summary_txn['blockNumber'] = t_info['blockNumber']
                summary_txn['hash'] = t_info['hash'].hex()
                summary_txn['from'] = t_info['from']
                summary_txn['to'] = t_info['to']
                summary_txn['gasPrice'] = t_info['gasPrice']
                summary_txn['value'] = t_info['value']
                summary_txn['timestamp'] = timestamp

                txn_list.append(summary_txn)

            self.db.insert_txns(txn_list)

    def _validate_last_transaction(self):
        pass

    def pull(self):
        self.logger.info('Start to collect all transactions.')

        latest_block = self.db.get_latest_block()
        if latest_block is None:
            latest_block = self.web3.eth.blockNumber
            self.logger.info('It is a first pull transaction.')
        else:
            latest_block += 1
            self.logger.info('Pulled lastest block: {0}'.format(latest_block))
            self._validate_last_transaction()

        while True:
            new_latest_block = self.web3.eth.blockNumber

            self.logger.info(
                "Ethereum lastest block: {0}".format(new_latest_block)
            )
            if latest_block == new_latest_block:
                time.sleep(2)
                continue

            self.__get_transaction(
                latest_block,
                new_latest_block,
            )
            latest_block = new_latest_block
            time.sleep(2)
