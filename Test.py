from termcolor import colored, cprint

class stringHandler:
    def __init__(self):
        self.color = "red"
        self.mood = "happy"

    def shout(self, words):
        print(words.upper())

    def reverse(self, words):
        return words[::-1]

myString = stringHandler()

class StringMoods(stringHandler):
    def __init__(self):
        self.moods = {
            "happy": "green",
            "sad": myString.color,
            "angry": "yellow",
            "surprised": "blue"
        }

    def say(self, words, mood="happy" ):
        color = self.moods.get(mood, "white")
        cprint(words, color)

handler = StringMoods()
handler.say("hello", "happy")
handler.say("Noooooo!!!!", "angry")
handler.say("What??", "surprised")
handler.say("What??", myString.mood)

print(handler.shout('testing'))
