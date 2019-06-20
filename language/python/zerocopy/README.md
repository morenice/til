== PEP 3118 ==
Buffer protocol

```
python -m memory_profiler copy.py
Content length: 10240000, content to write length 10238976
Filename: copy.py

Line #    Mem usage    Increment   Line Contents
================================================
     1   11.270 MiB   11.270 MiB   @profile
     2                             def read_random():
     3   11.270 MiB    0.000 MiB       with open("/dev/urandom", "rb") as source:
     4   21.039 MiB    9.770 MiB           content = source.read(1024 * 10000)
     5   30.805 MiB    9.766 MiB           content_to_write = content[1024:]
     6
     7   30.805 MiB    0.000 MiB       print("Content length: %d, content to write length %d" %
     8   30.812 MiB    0.008 MiB             (len(content), len(content_to_write)))
     9
    10   30.812 MiB    0.000 MiB       with open("/dev/null", "wb") as target:
    11   30.812 MiB    0.000 MiB           target.write(content_to_write)
```


```
python -m memory_profiler --pdb-mmem=1 copy.py

Current memory 11.32 MiB exceeded the maximum of 1.00 MiB
Stepping into the debugger
> /Users/morenice/Sources/open-source/til/language/python/zerocopy/copy.py(4)read_random()
-> content = source.read(1024 * 10000)
(Pdb)
```


```
python -m memory_profiler memoryview.py
Content length: 10240000, content to write length 10238976
Filename: memoryview.py

Line #    Mem usage    Increment   Line Contents
================================================
     1   11.312 MiB   11.312 MiB   @profile
     2                             def read_random():
     3   11.312 MiB    0.000 MiB       with open("/dev/urandom", "rb") as source:
     4   21.082 MiB    9.770 MiB           content = source.read(1024 * 10000)
     5   21.082 MiB    0.000 MiB           content_to_write = memoryview(content)[1024:]
     6
     7   21.082 MiB    0.000 MiB       print("Content length: %d, content to write length %d" %
     8   21.090 MiB    0.008 MiB             (len(content), len(content_to_write)))
     9
    10   21.090 MiB    0.000 MiB       with open("/dev/null", "wb") as target:
    11   21.090 MiB    0.000 MiB           target.write(content_to_write)
```


Reference
* https://julien.danjou.info/high-performance-in-python-with-zero-copy-and-the-buffer-protocol/
