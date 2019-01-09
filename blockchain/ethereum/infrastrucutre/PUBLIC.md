# Ethereum public network (mainnet)
Container based ethereum network

## Prepare
Download `client-go` container
```
$ docker pull ethereum/client-go
```

## Run public node
Run go-ethereum container
* json-prc 8545 port and allow rpcaddr 0.0.0.0(any)
* using volume
```
$ docker run -it -v public-eth-volume:/root/.ethereum -p 8545:8545 -p 30303:30303 ethereum/client-go --rpc --rpcaddr "0.0.0.0"

WARN [01-09|02:33:57.697] Sanitizing cache to Go's GC limits       provided=1024 updated=498
INFO [01-09|02:33:57.700] Maximum peer count                       ETH=25 LES=0 total=25
INFO [01-09|02:33:57.703] Starting peer-to-peer node               instance=Geth/v1.9.0-unstable-81f04fa6/linux-amd64/go1.11.4
INFO [01-09|02:33:57.704] Allocated cache and file handles         database=/root/.ethereum/geth/chaindata cache=249 handles=524288
INFO [01-09|02:33:57.736] Writing default main-net genesis block
INFO [01-09|02:33:58.958] Persisted trie from memory database      nodes=12356 size=1.88mB time=197.4458ms gcnodes=0 gcsize=0.00B gctime=0s livenodes=1 livesize=0.00B
INFO [01-09|02:33:58.963] Initialised chain configuration          config="{ChainID: 1 Homestead: 1150000 DAO: 1920000 DAOSupport: true EIP150: 2463000 EIP155: 2675000 EIP158: 2675000 Byzantium: 4370000 Constantinople: 7080000 Engine: ethash}"
INFO [01-09|02:33:58.966] Disk storage enabled for ethash caches   dir=/root/.ethereum/geth/ethash count=3
INFO [01-09|02:33:58.967] Disk storage enabled for ethash DAGs     dir=/root/.ethash               count=2
INFO [01-09|02:33:58.967] Initialising Ethereum protocol           versions="[63 62]" network=1
INFO [01-09|02:33:59.093] Loaded most recent local header          number=0 hash=d4e567…cb8fa3 td=17179869184 age=49y8mo3w
INFO [01-09|02:33:59.095] Loaded most recent local full block      number=0 hash=d4e567…cb8fa3 td=17179869184 age=49y8mo3w
INFO [01-09|02:33:59.097] Loaded most recent local fast block      number=0 hash=d4e567…cb8fa3 td=17179869184 age=49y8mo3w
INFO [01-09|02:33:59.099] Regenerated local transaction journal    transactions=0 accounts=0
INFO [01-09|02:33:59.123] New local node record                    seq=1 id=1928c411502c024c ip=127.0.0.1 udp=30303 tcp=30303
INFO [01-09|02:33:59.144] IPC endpoint opened                      url=/root/.ethereum/geth.ipc
INFO [01-09|02:33:59.196] Started P2P networking                   self=enode://844350116abc95df66a590e925ab07f452a76c9b2c53305bbcf589cc4e74c2bebc2f89ee1123a663158d3975c13dc056f960f6c03f53b0e895c393e9084eb0fe@127.0.0.1:30303
INFO [01-09|02:33:59.242] HTTP endpoint opened                     url=http://0.0.0.0:8545      cors= vhosts=localhost
INFO [01-09|02:34:49.165] Block synchronisation started
INFO [01-09|02:34:55.227] Imported new block headers               count=192 elapsed=1.044s number=192 hash=723899…123390 age=3y5mo4w
INFO [01-09|02:34:55.301] Imported new block receipts              count=2   elapsed=173.8µs number=2   hash=b495a1…4698c9 age=3y5mo4w  size=8.00B
INFO [01-09|02:34:55.505] Imported new block receipts              count=4   elapsed=267.7µs number=6   hash=1f1aed…6b326e age=3y5mo4w  size=1.10kB
INFO [01-09|02:34:58.385] Imported new state entries               count=1641 elapsed=915.9µs processed=1641 pending=20862 retry=0 duplicate=0 unexpected=0
INFO [01-09|02:35:00.324] Imported new state entries               count=1152 elapsed=13.759ms processed=2793 pending=19946 retry=0 duplicate=0 unexpected=0
INFO [01-09|02:35:02.520] Imported new state entries               count=1152 elapsed=8.535ms  processed=3945 pending=19978 retry=0 duplicate=0 unexpected=0
.
.
.
```

System resource information
```
~/.ethereum/geth # ps -ef
PID   USER     TIME  COMMAND
    1 root      1:59 geth --rpc --rpcaddr 0.0.0.0

~/.ethereum/geth # netstat -atnp
Active Internet connections (servers and established)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 172.17.0.2:57702        120.79.190.125:30603    TIME_WAIT   -
tcp        0      0 172.17.0.2:60770        139.59.69.168:30303     TIME_WAIT   -
tcp        0      1 172.17.0.2:36888        119.29.165.132:30303    SYN_SENT    1/geth
tcp        0      0 172.17.0.2:39522        209.250.255.70:30303    ESTABLISHED 1/geth
tcp        0      1 172.17.0.2:45556        18.217.227.228:30303    SYN_SENT    1/geth
tcp        0      1 172.17.0.2:41842        73.121.200.210:30303    SYN_SENT    1/geth
tcp        0      0 172.17.0.2:37844        52.74.57.123:30303      ESTABLISHED 1/geth
tcp        0      1 172.17.0.2:37314        47.74.137.216:30303     SYN_SENT    1/geth
tcp        0      0 172.17.0.2:46536        104.248.202.197:30303   TIME_WAIT   -
tcp        0      1 172.17.0.2:51092        35.225.95.112:30303     SYN_SENT    1/geth
tcp        0      1 172.17.0.2:50230        94.237.26.46:30305      SYN_SENT    1/geth
tcp        0      0 :::30303                :::*                    LISTEN      1/geth
tcp        0      0 :::8545                 :::*                    LISTEN      1/geth
```


# See also
* Reference
  * https://hub.docker.com/r/ethereum/client-go/
