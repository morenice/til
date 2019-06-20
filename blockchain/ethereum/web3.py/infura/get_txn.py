from web3.auto.infura import w3
import time


def get_transaction(from_block, to_block):
    print('get block from {0} to {1}'.format(from_block, to_block))
    for i in range(from_block, to_block, 1):
        print('block: {}'.format(i))
        block = w3.eth.getBlock(from_block)
        print(block)
        transactions = block['transactions']
        for txn in transactions:
            print(w3.eth.getTransaction(txn))


def main():
    print(w3.isConnected())

    latest_block = w3.eth.blockNumber
    print('latest block: {}'.format(latest_block))
    time.sleep(2)

    while True:
        new_latest_block = w3.eth.blockNumber
        get_transaction(latest_block, new_latest_block)

        latest_block = new_latest_block
        time.sleep(2)


if __name__ == '__main__':
    main()
