import reports
# file.write("The number of games in the file: {}\n".format(reports.count_games(file_name)))


def questions_to_txt(file_name, title, export_file='export_file.txt'):
    file = open(export_file, 'w')
    file.write("The most played game is: {}\n".format(reports.get_most_played(file_name)))
    file.write("The summary of copies: {}\n".fomrat(reports.sum_sold(file_name)))
    file.write("The avarge of sold copies: {}\n".format(reports.get_selling_avg(file_name)))
    file.write("The longest title has so many characters: {}\n".format(reports.count_longest_title(file_name)))
    file.write("The avarge of the year of publication: {}\n".format(reports.get_date_avg(file_name)))
    file.write("The properties of the given game name: {}\n".format(reports.get_game(file_name, title)))
    file.close()
    return export_file
# Export functions