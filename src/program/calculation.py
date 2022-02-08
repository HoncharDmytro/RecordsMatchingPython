from datetime import datetime


def read(record: str) -> list:
    with open(record, "r", encoding="UTF-8") as input_stream:  # 'rb'
        data = pars(input_stream)
    input_stream.close()
    return data


def pars(file):
    _list = list()
    for value in file.read():
        if value.isdigit():
            _list.append(value)
    return _list


def matching_analysing(list_one, list_two):
    iterator = 0
    counter = 0
    matching = list()
    if len(list_one) == len(list_two):
        for i in range(len(list_one)):
            if list_one[i] == list_two[i]:
                matching.append(list_one[i])
                counter += 1
            iterator += 1
    return counter, matching


def matching_analysing_with_numeration(list_one, list_two):
    iterator = 0
    counter = 0
    matching = dict()
    fgf = ratio_check(list_one, list_two)
    for i in range(fgf):
        if list_one[i] == list_two[i]:
            matching[i] = list_one[i]
            counter += 1
        iterator += 1
    return counter, matching


def ratio_check(list_one, list_two):
    if len(list_one) <= len(list_two):
        return len(list_one)
    else:
        return len(list_two)


def save(data, counter, file):
    with open(file, "a", encoding="UTF-8") as writer:  # 'wb'
        writer.write(str(datetime.now().replace(microsecond=0))+'\n')
        if type(data) == list:
            for i in data:
                writer.write(f'{i}\n')
        elif type(data) == dict:
            for i, k in data.items():
                writer.write(f'Line:{i}, Value: {k}\n')
        else:
            pass
        writer.write(f'Number of coincidence: {counter}\n\n')
    writer.close()
    print("Data was saved.")
