import datetime
import os
import shutil
import utils
from collections import Counter
import pickle

"""
these can be inputs
"""
src = r'C:\dev\DataFlowParsing\source'
tgt = r'C:\dev\DataFlowParsing\target'
bad = r'C:\dev\DataFlowParsing\bad'

files = os.listdir(src)
toc = datetime.datetime.now()

reader = []
validation_values = []
file_count = 0

"""
1. get the file names and counts from the source and its subfolders
2. first level file validations
    2.2. Header ID = Tail ID
    2.3. row_count = tail row count value
    2.4. file name pattern check D[0-9][0-9][0-9][0-9][0-9][0-9][0-9]
3. create the dflow folder under target
3. move the files that passes the validations to the target folder
4. move the files that fail the validations to the bad folder
5. report back total counts. dflow group by counts
6. create a full report as a pickle file for later use in jupyter
"""
for src, dirs, files in os.walk(src, topdown=True):
    for name in files:
        filename = os.path.join(src, name)
        valid = utils.get_file_validation_values(filename)
        validation_values.append(utils.get_file_validation_values(filename))
        if valid['validation']:
            with open(os.path.join(src, name), 'r') as f:
                line = f.readline()
                filename = line.split('|')[2][:5]
                reader.append(filename)
                file_count += 1
                if not os.path.exists(tgt + '\\' + filename):
                    os.makedirs(tgt + '\\' + filename, mode=0o777, exist_ok=True)
            shutil.move((src + '\\' + name), (tgt + '\\' + filename))
        else:
            if not os.path.exists(bad + '\\'):
                os.makedirs(bad + '\\', mode=0o777, exist_ok=True)
            shutil.move((src + '\\' + name), (bad + '\\'))

print(Counter(reader), f'Total File Count:', file_count)

with open(tgt + '\\' + 'validation_values.pkl', 'wb') as f:
    pickle.dump(validation_values, f)

tic = datetime.datetime.now()

""" show run time """
print(f'Runtime: ' + str(tic - toc))
