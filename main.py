import random as r
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "XD": "se usa al hablar sarcasticamente a algo o que algo es random",
            "MOOD":"se refiere a la emocion que tienes o tiene algo",
            "VIBE":"la emocion, sensacion o cosa que transmite algo",
            "SUS":"se refiere a algo sospechoso",
            "GLOW-UP":"se refiere a la transformacion o mejora de alguien o algo",
            "SIMP":"alguien que siente admiracion u obsecion excesiva por alguien",
            "EVENTO CANONICO":"cosa que nos pasó a todos o que es importante en tu vida",
            "SHIP":"relacion que se desea entre 2 personas generalmente personajes ficticios"
}

print(meme_dict.keys())
word = input("escribe una palabra que no entiendas o escribe: sorprendeme")

if word in meme_dict.keys():
    print("el significado es:",meme_dict[word])
elif word == "sorprendeme":
    wordr = r.choice(list(meme_dict.keys()))
    print("la palabra es:", wordr, "el significado es:",meme_dict[wordr])
else:
    print("esta palabra no esta en el diccionario")
