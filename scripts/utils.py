import re


def get_file_validation_values(filename):
    """
    :param filename: full path with filename as string i.e.: 'C:\dev\DataFlowParsing\target\D0004\V00018112.usr'
    :return: validation values as dictionary
    Notes: what if Header and Footer codes be come as dupes ?
    This code won't give an error (?)
    checks:
    1. Header ID = Tail ID
    2. row_count = tail row count value
    3. file name pattern check D[0-9][0-9][0-9][0-9][0-9][0-9][0-9]
    """

    with open(filename, 'r') as f:
        pattern = re.compile('D\d{7}')
        file_dict = {'ZHV': '', 'ZHD': '', 'ZHF': ''}
        line = f.readline()
        line_count = 0
        file_dict['dflow'] = line.split('|')[2][:8]
        file_dict['flow_name'] = line.split('|')[2][:5]
        # print(file_dict['dflow'])
        file_dict['file_creation_date'] = line.split('|')[7][:15]
        while line:
            if line[:3] in ('ZHV', 'ZHD', 'ZHF'):
                file_dict[line[:3]] = line.split('|')[1]
                # print(line[:3], ':', line.split('|')[1])
            if line[:3] == 'ZPT':
                file_dict[line[:3]] = line.split('|')[1]
                file_dict['tail_rowcount'] = line.split('|')[2]
                # print(line[:3], ':', line.split('|')[1])
            line = f.readline()
            line_count += 1
        file_dict['file_rowcount'] = line_count - 2
        if (file_dict['ZHV'] == file_dict['ZPT'] or file_dict['ZHD'] == file_dict['ZPT'] \
            or file_dict['ZHF'] == file_dict['ZPT']) \
                and int(file_dict['tail_rowcount']) == int(file_dict['file_rowcount']) \
                and re.match(pattern, file_dict['dflow']):
            file_dict['validation'] = True
        else:
            file_dict['validation'] = False
    return file_dict
