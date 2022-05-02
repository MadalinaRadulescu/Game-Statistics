# Export functions
import sys
from reports import count_by_genre, count_games, decide, get_genres, get_latest, when_was_top_sold_fps
from reports import sort_abc
from reports import get_line_number_by_title
with open(filename, 'w') as f:
    f.write(sort_abc(file_name))
    f.write(get_genres(file_name))
    f.write(when_was_top_sold_fps(file_name))
n = sys.argv[1]

file_name = input("Please enter file: ")
print(count_games(file_name))
year = int(input('Please enter year: '))
print(decide(file_name, year))
get_latest(file_name)
genre = input('Plese enter a genre: ')
print(count_by_genre(file_name,genre))
title = input('Please enter a title: ')
print(get_line_number_by_title(file_name, title))
sort_abc(file_name)
get_genres(file_name)
when_was_top_sold_fps(file_name)