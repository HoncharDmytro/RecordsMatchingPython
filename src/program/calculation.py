from datetime import datetime
from typing import TextIO, Tuple, Iterable


def read(record: str) -> list:
    '''Takes  a file path, reads, validates and writes to the list.'''
    with open(record, "r", encoding="UTF-8") as input_stream:  # 'rb'
        data = __pars(input_stream)
    input_stream.close()
    return data


def __pars(file: TextIO) -> list:
    _list = list()
    for value in file.read():
        if value.isdigit():
            _list.append(value)
    return _list


def matching_analysing(list_one: list, list_two: list) -> Tuple[int, list]:
    '''Takes two lists, compares each element line by line, and returns a list of matching values and their count.'''
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


def matching_analysing_with_numeration(list_one: list, list_two: list) -> Tuple[int, dict]:
    '''Takes two lists, compares each element line by line, and returns a tuple of matching values(where key is line
    number and value is matched number) and their count.'''
    iterator = 0
    counter = 0
    matching = dict()
    fgf = __ratio_check(list_one, list_two)
    for i in range(fgf):
        if list_one[i] == list_two[i]:
            matching[i] = list_one[i]
            counter += 1
        iterator += 1
    return counter, matching


def __ratio_check(list_one: list, list_two: list) -> int:
    if len(list_one) <= len(list_two):
        return len(list_one)
    else:
        return len(list_two)


def save(data: Iterable[int], counter: int, file: str) -> None:
    '''Takes a data to write, matching counter, path to the file ant save data in it.'''
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
