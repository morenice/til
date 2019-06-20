import asyncio
import time

from web3 import Web3
from web3 import WebsocketProvider, HTTPProvider
from web3.middleware import geth_poa_middleware


def connect_web3_provider(web3_url):
    if 'wss://' in web3_url:
        web3 = Web3(
            WebsocketProvider(web3_url, websocket_kwargs={'timeout': 60})
        )
    else:
        web3 = Web3(HTTPProvider(web3_url))

    if 'mainnet' in web3_url:
        print(f'ethereum mainnet {web3_url}')
    elif 'rinkeby' in web3_url:
        print(f'ehtereum testnet {web3_url}')
        web3.middleware_stack.inject(geth_poa_middleware, layer=0)
    else:
        print(f'ehtereum testnet {web3_url}')

    return web3


def handle_event(event):
    print(event)
    # and whatever


async def get_txns(web3, txn_hash_list, txn_list, poll_interval, idx):
    while len(txn_hash_list):
        txn_hash = txn_hash_list.pop()
        txn = await web3.eth.getTransaction(txn_hash)
        print('[{0}] get transaction {1}'.format(idx, txn['hash'].hex()))

        txn_list.append(txn)
        #await asyncio.sleep(0.0001)


def get_txns_block_range(web3, from_block, to_block):
    print(f'Get block from {from_block} to {to_block}')

    loop = asyncio.get_event_loop()

    try:
        for idx in range(from_block, to_block+1, 1):
            block = web3.eth.getBlock(idx)
            transactions = block['transactions']
            timestamp = block['timestamp']

            print(
                'block {}, parent {}, txn {} count, {} timestamp'.format(
                    idx,
                    block['parentHash'].hex(),
                    len(transactions),
                    timestamp
                )
            )

            txn_list = []

            loop.run_until_complete(
                asyncio.gather(
                    get_txns(web3, transactions, txn_list, 2, 1),
                    get_txns(web3, transactions, txn_list, 2, 2),
                    get_txns(web3, transactions, txn_list, 2, 3),
                    get_txns(web3, transactions, txn_list, 2, 4),
                    get_txns(web3, transactions, txn_list, 2, 5),
                )
            )

        print(len(txn_list))
        print(txn_list)

    finally:
        loop.close()


def get_txns_block_range2(web3, from_block, to_block):
    print(f'Get block from {from_block} to {to_block}')

    for idx in range(from_block, to_block+1, 1):
        block = web3.eth.getBlock(idx)
        transactions = block['transactions']
        timestamp = block['timestamp']

        print(
            'block {}, parent {}, txn {} count, {} timestamp'.format(
                idx,
                block['parentHash'].hex(),
                len(transactions),
                timestamp
            )
        )

        txn_list = []
        for txn_hash in transactions:
            txn = web3.eth.getTransaction(txn_hash)
            print('get transaction {0}'.format(txn['hash'].hex()))

            txn_list.append(txn)

        print(len(txn_list))
        print(txn_list)

    print(len(txn_list))
    print(txn_list)


def main():
    web3 = connect_web3_provider('wss://rinkeby.infura.io/_ws')

    from_block = 3509000
    #latest_block = web3.eth.blockNumber
    latest_block = 3509003

    get_txns_block_range(web3, from_block, latest_block)
    #get_txns_block_range2(web3, from_block, latest_block)


if __name__ == '__main__':
    main()
