def convert(number):
    sentence = ""
    if number % 3 == 0:
        sentence = sentence + "Pling"
    if number % 5 == 0:
        sentence = sentence + "Plang"
    if number % 7 == 0:
        sentence = sentence + "Plong"
    if sentence == "": 
        return str(number)
    else: 
        return sentence
