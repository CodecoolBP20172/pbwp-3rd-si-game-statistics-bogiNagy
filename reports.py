def file_to_list(file_name="game_stat.txt"):
    from_file = []
    file = open(file_name, 'r')
    for item in file:
        from_file.append(item.strip().split("\t"))
    file.close()
    return(from_file)
# Report functions


def count_games(file_name):
    file_to_list()
    a = open(file_name, 'r')
    l = a.read()
    counter = l.splitlines()
    count = len(counter)
    return(count)


def decide(file_name, year):
    for item in file_to_list():
        if year == int(item[2]):
            result = True
            break
        else:
            result = False
            continue
    return(result)


def get_latest(file_name):
    year_variable = ""
    name_variable = ""
    for item in file_to_list():
        if item[2] > year_variable:
            year_variable = item[2]
            name_variable = item[0]
        elif item[2] == year_variable:
            year_variable.append = item[0]
        else:
            continue
    return name_variable


def count_by_genre(file_name, genre):
    count_genre = 0
    for item in file_to_list():
        if genre == item[3]:
            count_genre += 1
        else:
            continue
    return count_genre


def get_line_number_by_title(file_name, title):
    count_lines = 1
    decide = False
    for item in file_to_list():
        if title != item[0]:
            count_lines += 1
        else:
            decide = True
            break
    if decide is False:
        raise ValueError
    return count_lines