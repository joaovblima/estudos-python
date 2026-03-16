magicians = ["magnus valerion", "elderich sombraluzl",
             "zorath o arcano", "altherion myst",
             "merilian dunkswoord"]
great_magicians = []


def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())


def make_great(magicians, great_magicians):
    while magicians:
        magician = "The great"
        magician += " " + magicians.pop()
        great_magicians.append(magician)


def show_great_magicians(great_magicians):
    for g_magician in great_magicians:
        print(g_magician.title())


make_great(magicians[:], great_magicians)
show_great_magicians(great_magicians)
show_magicians(magicians)
