import math


def file_to_list(file_name="game_stat.txt"):
    from_file = []
    file = open(file_name, 'r')
    for item in file:
        from_file.append(item.strip().split("\t"))
    file.close()
    return(from_file)
# Report functions


def get_most_played(file_name):
    prev_or_next = [0]
    for item in file_to_list(file_name):
        if float(item[1]) > prev_or_next[0]:
            prev_or_next.append(float(item[1]))
            prev_or_next.remove(prev_or_next[0])
            prev_or_next.append(str(item[0]))
        else:
            continue
    return(prev_or_next[1])


def sum_sold(file_name):
    copies = []
    for item in file_to_list(file_name):
        copies.append(item[1])
    return(sum(float(item) for item in copies))


def get_selling_avg(file_name):
    sold_list = []
    for item in file_to_list(file_name):
        sold_list.append(item[1])
    divisor = len(sold_list)
    avg_sold = (sum(float(item) for item in sold_list)) / divisor
    return abs(avg_sold)


def count_longest_title(file_name):
    name_list = []
    for item in file_to_list(file_name):
        name_list.append(item[0])
    longest_name = max(name_list, key=len)
    final = sum(len(longest_name) for longest_name in longest_name)
    return final


def get_date_avg(file_name):
    date_list = []
    for item in file_to_list(file_name):
        date_list.append(item[2])
    divisor = len(date_list)
    avg_date = (sum(int(item) for item in date_list)) / divisor
    return math.ceil(avg_date)


def get_game(file_name, title):
    line = []
    for item in file_to_list(file_name):
        if item[0] == title:
            line.append(str(item[0]))
            line.append(float(item[1]))
            line.append(int(item[2]))
            line.append(str(item[3]))
            line.append(str(item[4]))
    return line