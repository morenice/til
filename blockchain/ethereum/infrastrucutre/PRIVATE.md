# Ethereum private network
Container based ethereum private network

## Prepare
Download `client-go` container
```
$ docker pull ethereum/client-go
```

## Run private node
### First node
Run go-ethereum container(using volume)
* access to bash shell
```
$ docker run -it -v private-eth-volume1:/root/.ethereum -p 30303:30303 -p 8545:8545 --entrypoint /bin/sh ethereum/client-go
```

Create genesis config file: `/root/.ethereum/genesis.json`
```
{
  "config": {
    "chainId": 55387,
    "homesteadBlock": 0,
    "eip155Block": 0,
    "eip158Block": 0
  },
  "alloc": {},
  "coinbase"   : "0x0000000000000000000000000000000000000000",
  "difficulty" : "0x20000",
  "extraData"  : "",
  "gasLimit"   : "0x2fefd8",
  "nonce"      : "0x0000000000000042",
  "mixhash"    : "0x0000000000000000000000000000000000000000000000000000000000000000",
  "parentHash" : "0x0000000000000000000000000000000000000000000000000000000000000000",
  "timestamp"  : "0x00"
}
```
* config: blockchain configiuration(blockchain identity,..)
* difficulty: mining difficulty
* gasLimit: the limit of gas cost per block
* alloc: pre-funded address

Init ethereum by `genesis.json` file
```
$ geth init /root/.ethereum/genesis.json

WARN [01-09|08:47:01.249] Sanitizing cache to Go's GC limits       provided=1024 updated=498
INFO [01-09|08:47:01.261] Maximum peer count                       ETH=25 LES=0 total=25
INFO [01-09|08:47:01.271] Allocated cache and file handles         database=/root/.ethereum/geth/chaindata cache=16 handles=16
INFO [01-09|08:47:01.332] Writing custom genesis block
INFO [01-09|08:47:01.335] Persisted trie from memory database      nodes=1 size=150.00B time=214.458µs gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
INFO [01-09|08:47:01.336] Successfully wrote genesis state         database=chaindata                      hash=1a6247…cd39a3
INFO [01-09|08:47:01.337] Allocated cache and file handles         database=/root/.ethereum/geth/lightchaindata cache=16 handles=16
INFO [01-09|08:47:01.366] Writing custom genesis block
INFO [01-09|08:47:01.367] Persisted trie from memory database      nodes=1 size=150.00B time=93.132µs  gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
INFO [01-09|08:47:01.371] Successfully wrote genesis state         database=lightchaindata                      hash=1a6247…cd39a3
```

Create account
```
$ geth account new

Your new account is locked with a password. Please give a password. Do not forget this password.
Passphrase:
Repeat passphrase:
```

Run private blockchain with mining(–mine –minerthreads 1)
```
$ geth --rpc --rpcaddr 0.0.0.0 --networkid 55387 --mine --minerthreads 1

WARN [01-09|08:53:48.777] Sanitizing cache to Go's GC limits       provided=1024 updated=498
INFO [01-09|08:53:48.785] Maximum peer count                       ETH=25 LES=0 total=25
INFO [01-09|08:53:48.788] Starting peer-to-peer node               instance=Geth/v1.9.0-unstable-81f04fa6/linux-amd64/go1.11.4
INFO [01-09|08:53:48.789] Allocated cache and file handles         database=/root/.ethereum/geth/chaindata cache=249 handles=524288
INFO [01-09|08:53:48.854] Initialised chain configuration          config="{ChainID: 55387 Homestead: 0 DAO: <nil> DAOSupport: false EIP150: <nil> EIP155: 0 EIP158: 0 Byzantium: <nil> Constantinople: <nil> Engine: unknown}"
INFO [01-09|08:53:48.855] Disk storage enabled for ethash caches   dir=/root/.ethereum/geth/ethash count=3
INFO [01-09|08:53:48.856] Disk storage enabled for ethash DAGs     dir=/root/.ethash               count=2
INFO [01-09|08:53:48.858] Initialising Ethereum protocol           versions="[63 62]" network=55387
INFO [01-09|08:53:48.923] Loaded most recent local header          number=0 hash=1a6247…cd39a3 td=131072 age=49y8mo3w
INFO [01-09|08:53:48.925] Loaded most recent local full block      number=0 hash=1a6247…cd39a3 td=131072 age=49y8mo3w
INFO [01-09|08:53:48.926] Loaded most recent local fast block      number=0 hash=1a6247…cd39a3 td=131072 age=49y8mo3w
INFO [01-09|08:53:48.928] Regenerated local transaction journal    transactions=0 accounts=0
INFO [01-09|08:53:48.966] New local node record                    seq=1 id=3d54c12d623e0dfd ip=127.0.0.1 udp=30303 tcp=30303
INFO [01-09|08:53:48.985] IPC endpoint opened                      url=/root/.ethereum/geth.ipc
INFO [01-09|08:53:48.995] Started P2P networking                   self=enode://d1763baac70933e5281157d972c134638d99482c58fc4cb0fbb10918b3557cfdd113cb2303f91b1872d72f04d33624be797f2afd5a569c4137d77b28649c7fd6@127.0.0.1:30303
INFO [01-09|08:53:49.004] HTTP endpoint opened                     url=http://0.0.0.0:8545      cors= vhosts=localhost
.
.
.
INFO [01-09|09:43:17.322] Generating DAG in progress               epoch=1 percentage=29 elapsed=7m12.730s
INFO [01-09|09:43:18.035] Successfully sealed new block            number=39 sealhash=f30b64…97b292 hash=c7bb62…8327cc elapsed=3.780s
INFO [01-09|09:43:18.036] 🔗 block reached canonical chain          number=32 hash=c37186…4a20a3
INFO [01-09|09:43:18.038] 🔨 mined potential block
```

Use below command to attach geth console
```
$ geth attach

$ eth.getBalance(eth.accounts[0])
270000000000000000000
```

After run command
```
$ docker run -it -v private-eth-volume1:/root/.ethereum -p 30303:30303 -p 8545:8545 ethereum/client-go --rpc --rpcaddr 0.0.0.0 --networkid 55387 --mine --minerthreads 1
```

Command reference
* eth.accounts — Shows list of accounts which are registered on ethereum node
* eth.coinbase — Shows address of the main account which is used for mining
* eth.getBalance(eth.accounts[1]) — Shows the balance of account at 1st index in accounts array on node
* miner.start() — To start mining process on node
* miner.stop() — To stop mining process on node
* web3.sendTransaction( {from:eth.accounts[0], to:eth.accounts[1], value:web3.toWei(10,”ether”) })


### Peer node
Create new container for peer node
```
$ docker run -it -v private-eth-volume2:/root/.ethereum --entrypoint /bin/sh ethereum/client-go
```

Init (See first node)
```
$ geth init genesis.json
$ geth account new
```

Run with --botnodes options
```
geth --rpc --rpcaddr 0.0.0.0 --networkid 55387  --bootnodes <bootnode-enode-url-from-above>
```
* bootnodes
  * bootnode runs a bootstrap node for the Ethereum Discovery Protocol.
  * use enode of first node: `enode://xxxxx...@127.0.0.1:30303` to `enode://xxxxx...@PUBLIC_IP:30303`

After run command
```
$ docker run -it -v private-eth-volume2:/root/.ethereum -p 30304:30303 -p 8546:8545 ethereum/client-go --rpc --rpcaddr 0.0.0.0 --networkid 55387
```

# See also
* Reference
  * https://hub.docker.com/r/ethereum/client-go/
* Trouble shooting
  * check log message for --verbosity option of geth command
  * check genesis config file of first and peer node
  * use db clear command: `$ geth removedb`
