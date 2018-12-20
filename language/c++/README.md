Modern C++
* c++14, c++17, ...


# Docker
build image.
``` bash
docker image build -t morenice/cplusplus:lastest .
```

Run container.
``` bash
docker-compose up -d
```


# C++ compile
c++17 compile with debug option

``` bash
g++ -std=c++17 -g [SOURCE_FILE] -o [EXECUTE_FILE]
```

valgrind tools: prevent memory leak

``` bash
valgrind --leak-check=full ...
```

# TODO
* ZAPCC: Clang/LLVM based, Faster Builds
* cmake


# Referece
http://www.nuonsoft.com/blog/
