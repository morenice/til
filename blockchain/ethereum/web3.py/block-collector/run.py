import os
import sys
import argparse
import time

from web3 import Web3
from web3 import WebsocketProvider, HTTPProvider
from web3.middleware import geth_poa_middleware

import collector.log
from collector.config import FileConfig
from collector.db import CollectDatabase
from collector.transaction_collector import TransactionCollector


def connect_web3_provider(web3_url, websocket, logger):
    logger.info('Init ethereum web3 {}'.format(web3_url))

    if websocket:
        web3 = Web3(
            WebsocketProvider(web3_url, websocket_kwargs={'timeout': 60})
        )
    else:
        web3 = Web3(HTTPProvider(web3_url))

    if 'mainnet' in web3_url:
        logger.info('ethereum mainnet')
    elif 'rinkeby' in web3_url:
        logger.info('ehtereum testnet')
        web3.middleware_stack.inject(geth_poa_middleware, layer=0)
    else:
        logger.info('ethereum testnet')

    return web3


if __name__ == "__main__":
    logger = collector.log.get_logger()

    parser = argparse.ArgumentParser(
        prog='collector',
        usage='%(prog)s [option]',
        description='Ethereum blockchain transaction collector'
        )

    parser.add_argument(
        '--events',
        help='Get events of smart contracts',
        action='store_true'
    )
    parser.add_argument(
        '--transactions',
        help='Get transaction of smart contracts',
        action='store_true'
    )

    if len(sys.argv) == 1:
        parser.print_help()
        exit(0)

    file_config = FileConfig()
    db_config = file_config.get_database()

    args = parser.parse_args()

    db = CollectDatabase(
        db_config['host'],
        db_config['port'],
        db_config['database'],
        db_config['user'],
        db_config['password']
    )
    db.set_logger(logger)
    db.connect()

    web3_config = file_config.get_web3()
    web3 = connect_web3_provider(
        web3_config['websocketProvider'], True, logger
    )

    if args.events or args.transactions:
        if args.events:
            logger.info('Process to get events')

        if args.transactions:
            logger.info('Process to get transactions')
            txn_collector = TransactionCollector(logger, web3, db)
            txn_collector.pull()

    exit(0)
