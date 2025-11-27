from termcolor import colored, cprint

class stringHandler:
    def __init__(self):
        self.color = "red"

    def shout(words):
        cprint(words)

    def reverse(words):
        return words[::-1]

myString = stringHandler()

print(myString.color)

class StringMoods:
    def __init__(self):
        self.moods = {
            "happy": "green",
            "sad": "red",
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