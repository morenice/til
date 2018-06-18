Docker development environment

# Build source code

Download bitcoin source
``` bash
 $ git clone https://github.com/bitcoin/bitcoin
 $ git checkout -b [tag version]
```

```bash
docker compose up -d
```

Build source
``` bash
 $ cd /usr/local/src/bitcoin
 $ ./autogen.sh
 $ ./configure
 $ make
```

# Run
``` bash
 $ cd /usr/loca/src/bitcoin/src
 $ ./bitcoind -regtest -daemon
```

# Example
genereate block
```
 $ ./bitcoin-cli -regtest generate 101
.
.
.
  "4fce482fafb3ec199ff79f43e9e1754106591208dfaf7c9c71e7383218ff99fd",
  "6ef869e07fe29478ba9e345fabf150f1007e555671a044e0d8e5f11340e1d510",
  "61837b1451f65aba6d9fea10a0545d0fc52dc4077b3397770a1bab94e89067f9",
  "4fc12dfbb20b82f70fc1ed357e73701ed09545c01d81c203e0e21fff60ef9f7f"
]

 $ ./bitcoin-cli -regtest getbalance
50.00000000

```

create wallet
``` bash
 $ ./bitcoin-cli -regtest getnewaddres
2NFrithMHVrZ8pfAGMyjHhdozr4XXNaWoG4
 $ ./bitcoin-cli -regtest getnewaddres
2N4hqwSgP79AhGs1wLHVqc9o6JwxyEXqjnQ
```

# See also
* https://bitcoin.org/en/developer-examples
