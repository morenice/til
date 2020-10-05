= sync vs async =
* get_api.py: sync using request
* get_async_api.py: async using aiohttp

```
python get_api.py  0.21s user 0.10s system 8% cpu 3.519 total
python get_async_api.py  0.28s user 0.08s system 45% cpu 0.792 total
```

= etc =
* async download with aiohttp
* async upload to aws s3 with aioboto3
