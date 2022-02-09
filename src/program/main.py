from src.program.calculation import *

if __name__ == '__main__':
    sender_record = '../source/sender_record.txt'
    consumer_record = '../source/consumer_record.txt'
    data_holder = '../source/holder.txt'
    sender_data = read(sender_record)
    consumer_data = read(consumer_record)
    coincidences_count, coincidences = matching_analysing(sender_data, consumer_data)
    print(coincidences)
    print("Coincidences count:  " + str(coincidences_count))
    coincidences_count_two, coincidences_two = matching_analysing_with_numeration(sender_data, consumer_data)
    print(coincidences_two)
    print("Coincidences count:  " + str(coincidences_count_two))
    save(coincidences, coincidences_count, data_holder)
    save(coincidences_two, coincidences_count_two, data_holder)