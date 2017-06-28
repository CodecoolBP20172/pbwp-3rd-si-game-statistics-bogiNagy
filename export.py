import reports


def questions_to_txt(file_name, year, genre, title, export_file='export_file.txt'):
    file = open(export_file, 'w')
    file.write("The number of games in the file: {}\n".format(reports.count_games(file_name)))
    file.write("The answer of is there a game with a given year: {}\n".format(reports.decide(file_name, year)))
    file.write("The latest game was: {}\n".format(reports.get_latest(file_name)))
    file.write("From the given genre there are: {}\n".format(reports.count_by_genre(file_name, genre)))
    file.write("This is the line of the given game: {}\n".format(reports.get_line_number_by_title(file_name, title)))
    file.close()
    return export_file
# Export functions

questions_to_txt("game_stat.txt", 1995, "Simulation", "The Sims")