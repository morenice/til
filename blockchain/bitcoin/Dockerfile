FROM ubuntu:16.04

# Reference
# https://github.com/bitcoin/bitcoin/blob/master/doc/build-unix.md

# Install C++ build and Boost library
RUN apt-get update && apt-get install -y build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils python3 \
libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev

# Install BerkeleyDB for the wallet
RUN apt-get install -y software-properties-common && add-apt-repository ppa:bitcoin/bitcoin && apt-get update \
 && apt-get install -y libdb4.8-dev libdb4.8++-dev

# Optional (see --with-miniupnpc and --enable-upnp-default):
# ZMQ dependencies (provides ZMQ API 4.x)
# Git and vim
RUN apt-get install -y libminiupnpc-dev libzmq3-dev git vim

# Non GUI

WORKDIR /usr/local/src

CMD ["/bin/bash"]

EXPOSE 12000
EXPOSE 12001
