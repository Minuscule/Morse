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
lettre_francais= {}
for lettre, morse in lettre_morse.items() :
	lettre_francais[morse] = lettre


def ecrit_mot_francais(mot):
	lettres = mot.split(" / ")
	for lettre in lettres:
		print(lettre_francais[lettre], end="")
		
def ecrit_phrase_francais(phrase):
	mots = phrase.split(" // ")
	for mot in mots:
		ecrit_mot_francais(mot)
		print(" ", end="")
	print()
		

morse = input("Que voulez-vous écrire en français ? \n")	
ecrit_phrase_francais(morse)