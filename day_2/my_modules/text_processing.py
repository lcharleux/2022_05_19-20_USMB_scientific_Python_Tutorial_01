# TEXT PROCESSING
# Learn about classes and text processing


class TextProcessor:

    c = 666

    def __init__(self, text = ""):
        self.text = text
        self.b = 22

    def show(self):
        return self.text            

    def count_words(self):
        words = self.text.split()
        return len(words)

    def __add__(self, other, reverse = False):
        if type(other) is str:
            out = [self.text, other]
        elif other.__class__  is self.__class__:
            out = [self.text, other.text]
        if reverse:
            out = out[::-1]
        return self.__class__(" ".join(out))    

    #__radd__ = __add__
    def __radd__(self, other):
        return self.__add__(other, reverse = True)


    def __repr__(self):
        return f"< {self.text} >"

if __name__ == "__main__":
    print("CREATING INSTANCES")
    text = "Hello I'm some text\nAnd I like new lines"

    tp = TextProcessor(text)
    tp2 = TextProcessor("Another text")