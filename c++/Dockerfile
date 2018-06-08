FROM ubuntu:18.04

# c++17 and boost library development.
RUN apt-get update && apt-get -y install build-essential cmake libboost-all-dev \
# clear apt cache files.
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

WORKDIR /usr/local/src

CMD [ "/bin/bash" ]