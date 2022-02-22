# if not os.path.exists(tgt + '\\' + f.readline().split('|')[2][:5]):
#     f.seek(0)
#     os.makedirs(tgt + '\\' + f.readline().split('|')[2][:5], mode=0o777, exist_ok=True)
#     f.seek(0)
#     filename = f.readline().split('|')[2][:5]
#     print(filename)
# shutil.move((src + '\\' + file), (tgt + '\\' + f.readline().split('|')[2][:5] + '\\' + file))
#
# """ clear the target folder """
# folders = os.listdir(tgt)
# for folder in folders:
#     shutil.rmtree(tgt + '\\' + folder)
#
# """ create the new target folders """
# files_set = set(reader)
# i = 0
#
# while i <= len(files_set) - 1:
#     os.mkdir(tgt + '\\' + list(files_set)[i])
#     # print(tgt + '\\' + list(files_set)[i])
#     i += 1
# #

import re

# file_dict = {'dflow':  'D0012001'}
#
# pattern = re.compile(r'D\d{7}')
# if re.findall(pattern, file_dict['dflow']):
#     print(True)
#
# regex = re.findall(pattern, file_dict['dflow'])
# print(regex)

with open(r'C:\dev\DataFlowParsing\source\V00005612.usr', 'r', encoding='utf8') as f:
    pattern = re.compile('D\d{7}')
    line = f.readline()
    line_count = 0
    dflow = line.split('|')[2][:8]
    print(dflow)
    match = re.search(pattern, dflow)
    if match:
        print(match.group())
    result = re.findall(pattern, dflow)
    print(result)


    # if re.findall(pattern, dflow):
    #     print(True)






# for v in file_dict:
#     if re.fullmatch(r'D[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]', file_dict['dflow']):
#         print('Yes')
#         print(file_dict['dflow'])
#     else:
#         print('No')
