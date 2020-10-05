import tasks


result = tasks.add.delay(3,4)
print(result)

result.get(timeout=3)
