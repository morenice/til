from web3.auto.infura import w3
import asyncio
import time


def handle_event(event):
    print(event)
    # and whatever


async def log_loop(event_filter, name, poll_interval):
    while True:
        print('Try {}'.format(name))
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)


def main():
    print(w3.isConnected())
    block_filter = w3.eth.filter('latest')
    tx_filter = w3.eth.filter('pending')
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
                log_loop(block_filter, 'block', 2),
                log_loop(tx_filter, 'txn', 2)))
    finally:
        loop.close()

if __name__ == '__main__':
    main()
