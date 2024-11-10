import json

def store_data():
    f = open('SelectionSort.json')
    data = json.load(f)
    my_dict = {}

    for i in data:
        key = i['Title']
        value = i['Times Played']
        my_dict[key] = value

    f.close()
    return my_dict

def sort_data(unsorted_dict, sorted_dict):
    highest_val = 0
    lowest_key = ""

    for key in unsorted_dict:
        if int(unsorted_dict[key]) >= int(highest_val):
            highest_val = unsorted_dict[key]
            lowest_key = key

    if lowest_key != "":
        sorted_dict[lowest_key] = highest_val
        unsorted_dict.pop(lowest_key)

    return unsorted_dict, sorted_dict


if __name__ == '__main__':
    sorted_songs = {}
    unsorted_songs = store_data()

    print(f'Unsorted: {unsorted_songs}')

    while len(unsorted_songs) != 0:
        unsorted_songs, sorted_songs = sort_data(unsorted_songs, sorted_songs)



    print(f'Sorted: {sorted_songs}')
