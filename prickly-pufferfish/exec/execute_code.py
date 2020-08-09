import codecs


path = 'arena/templates/battle/battle.html'
my_file = codecs.open(path, "r", "utf-8")
print(my_file.read())
