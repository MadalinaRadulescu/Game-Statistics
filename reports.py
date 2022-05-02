from turtle import title


def get_file(file_name):
    file = open(file_name)
    lines = file.readlines()
    list_dicts = []
    for elem in lines:
        y = elem.rstrip("\n").split("\t")
        x = ("title", "copies sold", "year", "genre", "publisher")
        gameDict = dict(zip(x, y))
        list_dicts.append(gameDict)
    return list_dicts
#print(get_file("game_stat.txt"))

def convert_int(file_name):
    list_dicts = get_file(file_name)
    for item in list_dicts:
        for key, value in item.items():
            try:
                item[key] = int(value)
            except ValueError:
                item[key] = str(value)
    return list_dicts

#print(convert_int("game_stat.txt"))

def convert_float(file_name):
    list_dicts = get_file(file_name)
    for item in list_dicts:
        for key, value in item.items():
            try:
                item[key] = float(value)
            except ValueError:
                item[key] = str(value)
    return list_dicts

def count_games(file_name):
    return len(get_file(file_name))

#print(count_games("game_stat.txt"))
    
def decide(file_name, year):
    valueslist = []
    for i in convert_int(file_name):
        for val in i.values():
            valueslist.append(val)
    if year in valueslist:
        return True
    else:
        return False
    
#print(decide("game_stat.txt", 2004))

def get_latest(file_name):
    a = sorted(get_file(file_name), key=lambda x: x['year'])
    print(a[len(a)-1]["title"])
    
#get_latest("game_stat.txt")

def count_by_genre(file_name, genre):
    valueslist = []
    for i in get_file(file_name):
        for val in i.values():
            valueslist.append(val)
    count = 0
    for item in valueslist:
        if genre == item:
            count +=1
    return count
    

#print(count_by_genre("game_stat.txt", "First-person shooter"))


def get_line_number_by_title(file_name, title):
    list_dicts = get_file(file_name)
    line_number = 0
    for index in range(len(list_dicts)-1):
        if title in list_dicts[index].values():
            line_number = index + 1
            return line_number
    return "This title does not exist in file!"
            

#print(get_line_number_by_title("game_stat.txt", "dhf" ))

def sort_abc(file_name):
    a = sorted(get_file(file_name), key=lambda x: x['title'])
    titles = []
    for index in range(len(a)):
        titles.append(a[index]["title"])
    print(titles)
    


#sort_abc("game_stat.txt")

def get_genres(file_name):
    a = sorted(get_file(file_name), key=lambda x: x['genre'])
    genre = []
    for index in range(len(a)):
        genre.append(a[index]["genre"])
    print(sorted(set(genre)))
    

#get_genres("game_stat.txt")

def when_was_top_sold_fps(file_name):
    fpsDict = []
    for i in convert_float(file_name):
        for val in i.values():
                if val == "First-person shooter":
                    fpsDict.append(i)
    if len(fpsDict)>0:
        a = sorted(fpsDict, key=lambda x: x['copies sold'])
        print(a[len(a)-1]["year"])
    else:
        print("This genre does not exist in the file!")
    
    
#when_was_top_sold_fps('game_stat_nofpstest.txt')
