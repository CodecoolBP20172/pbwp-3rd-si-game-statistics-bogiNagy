from decimal import Decimal
import math


def file_to_list(file_name="game_stat.txt"):
    from_file = []
    file = open(file_name, 'r')
    for item in file:
        from_file.append(item.strip().split("\t"))
    file.close()
    return(from_file)
# Report functions

# 1


def get_most_played(file_name):
    copies = []
    names = []
    for item in file_to_list(file_name):
        copies.append(item[1])
        names.append(item[0])
    max_copies = max(Decimal(item) for item in copies)
    return(max_copies)

# 2


def sum_sold(file_name):
    copies = []
    for item in file_to_list(file_name):
        copies.append(item[1])
    return(sum(Decimal(item) for item in copies))

# 3


def get_selling_avg(file_name):
    sold_list = []
    for item in file_to_list(file_name):
        sold_list.append(item[1])
    divisor = len(sold_list)
    avg_sold = (sum(Decimal(item) for item in sold_list)) / divisor
    return avg_sold

# 4


def count_longest_title(file_name):
    pass

# 5


def get_date_avg(file_name):
    date_list = []
    for item in file_to_list(file_name):
        date_list.append(item[2])
    divisor = len(date_list)
    avg_date = (sum(Decimal(item) for item in date_list)) / divisor
    return math.ceil(avg_date)

# 6


def get_game(file_name, title):
    pass