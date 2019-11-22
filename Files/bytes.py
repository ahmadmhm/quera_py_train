a = b'\x02\xA1\x80'
print(a[1])
b = b'ab_*'
b = list(b)
print(b)
c = bytes([1, 129, 231])
print(c)
with open('a.jpg', 'rb') as a:
    data = a.read()
    with open('b.jpg', 'wb') as b:
        b.write(data)

import json
d = json.loads('[12, 2, {"a":2}]')
e = json.loads('[12, 2, {"a":2, "b": ["c", 2]}]')
g = json.loads('{"a":2, "b": ["c", 2]}')
h = json.loads('[2, 5, 8, 7, 3]')
i = json.loads('1')
print(d)
print(e)
print(g['a'])
print(h)
print(i)
f = json.dumps({"key": 2, "list": [12, 'ali']})
print(f)