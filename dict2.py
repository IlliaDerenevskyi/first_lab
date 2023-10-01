dict = {
    "level of class" : "wolf",
    "kind" : "german shepard",
    "name" : "Jella",
    "color" : "brown",
    "color of eyes" : "brown",
    "age" : "2 years",
    "children": "False",
    "commands":["sit", "stand", "lie down", "pleace", "nearby", "tumbling"] 
}

x = []

dict2 = {
    "commands" : dict.get("commands")
}
for x in dict["commands"]:
    x + ""

print(dict2)
