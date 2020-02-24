import sys
from PIL import Image

img = Image.open(sys.argv[1])
img = img.resize((32, 32))
img = img.load()

h = '0123456789abcdef'
s = ''
for i in range(32):
    for j in range(32):
        for k in img[i, j]:
            s += h[k // 16] + h[k % 16]
ret = []
for i in range(0, len(s), 64):
    if i + 64 <= len(s):
        ret.append('0x' + s[i:i+64])
    else:
        ret.append('0x' + '0' * (len(s) - i + 64) + s[i:])

print('[' + ','.join(['"' + x + '"' for x in ret]) + ']')
