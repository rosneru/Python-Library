class Line:
    def __init__(self, number : int, text : str):
        self._number = number
        self._text = text
    
    def getNumber(self) -> int:
        return self._number
    
    def setNumber(self, number: int):
        _number = number
    
    def getText(self) -> str:
        return self._text
    
    def setText(self, text: str):
        _text = text
    
    # Define read-only properties
    number = property(getNumber)
    text = property(getText)


class Document:
    def __init__(self, file_name: str):
        self.file_name = file_name

    def lines(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = [line.rstrip('\n') for line in file]
                lines = enumerate(lines)
                return list(lines)
        except:
            return list()
        


# Creating a Python variant of the Ruby take on Myers Diff algorithm 
# from here: https://blog.jcoglan.com/2017/02/15/the-myers-diff-algorithm-part-2/

class Myers:
    def __init__(self, a: list, b: list):
        self._a = a
        self._b = b

    def diff(self):
        if len(self._a) == 0:
            return
        
        if len(self._b) == 0:
            return


class Diff:
    def diff(self, a, b):
        differ = Myers(Document(a).lines(), Document(b).lines())
        differ.diff()


if __name__ == "__main__":
    d = Diff()
    d.diff("Diff-Myers/testcase_15_FB101-02-Simple-Left.txta",
           "Diff-Myers/testcase_15_FB101-02-Simple-Right.txt")
