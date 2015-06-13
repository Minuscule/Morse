lettre_morse = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "y": "-.--",
    "z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    "!": "-.-.--",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    '"': ".-..-.",
    "@": ".--.-.",
	"/": "-..-.",
	"(": "-.--.",
	")": "-.--.-",
	"&": ".-...",
	"_": "..--.-",
	"æ": ".-.-",
	"ä": ".-.-",
	"à": ".--.-",
	"å": ".--.-",
	"ç": "-.-..",
	"è": ".-..-",
	"é": "..-..",
	"ñ": "--.--",
	"ö": "---.",
	"ø": "---.",
	"ü": "..--",
    
}

def ecrit_mot_morse(mot):
	mot_length = len(mot)
	compteur = 0
	for lettre in mot.lower():
		print(lettre_morse[lettre], end="")
		compteur += 1
		if compteur < mot_length :
			print(" / ", end="")

def ecrit_phrase_morse(phrase):
	mots = phrase.split()
	phrase_length = len(mots)
	compteur = 0
	for mot in mots:
		ecrit_mot_morse(mot)
		compteur += 1
		if compteur < phrase_length :
			print(" // ", end="")
		else:
			print()

phrase = input("Que voulez-vous écrire en morse ? \n")	
ecrit_phrase_morse(phrase)