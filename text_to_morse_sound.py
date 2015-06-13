import subprocess

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

def play_mot_morse(mot):
	mot_length = len(mot)
	compteur = 0
	for lettre in mot.lower():
		play_lettre_morse(lettre_morse[lettre])
		compteur += 1
		if compteur < mot_length :
			play_sound("silence_letter")

def play_phrase_morse(phrase):
	mots = phrase.split()
	phrase_length = len(mots)
	compteur = 0
	for mot in mots:
		play_mot_morse(mot)
		compteur += 1
		if compteur < phrase_length :
			play_sound("silence_words")
		else:
			print()
			
def play_sound(file_name):
	audio_file = "Sound/%s.wav" % file_name
	print(audio_file)
	subprocess.call(["afplay", audio_file])
	
def play_lettre_morse(lettre):
	for caractere in lettre:
		if caractere == "." :
			play_sound("beep_dot")
		elif caractere == "-" :
			play_sound("beep_dash")
			
phrase = input("Que voulez-vous écrire en morse ? \n")	
play_phrase_morse(phrase)
