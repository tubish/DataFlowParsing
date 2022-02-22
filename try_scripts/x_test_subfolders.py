import datetime
import os

src = r'C:\dev\DataFlowParsing\source'
tgt = r'C:\dev\DataFlowParsing\target'

files = os.listdir(src)

for src, dirs, files in os.walk(src, topdown=True):
    for name in files:
        print(os.path.join(src, name))

a = 10
b = 20
c = 30

if a > 5 \
        and b > 10 \
        and c > 20:
    print('yes')

