import datetime
import os
import shutil
import utils
import pickle
import pandas

path = r'C:\dev\DataFlowParsing\target'
toc = datetime.datetime.now()
""" show run time """


tic = datetime.datetime.now()
print(f'Runtime: ' + str(tic - toc))
