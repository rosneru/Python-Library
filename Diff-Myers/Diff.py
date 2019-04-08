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
                numerated_lines = [line.rstrip('\n') for line in file]
                numerated_lines = list(enumerate(numerated_lines))

                lines = list()

                for nl in numerated_lines:
                    lines.append(Line(nl[0], nl[1]))

                return lines
        except:
            return list()
        


# Creating a Python variant of the Ruby take on Myers Diff algorithm 
# from here: https://blog.jcoglan.com/2017/02/15/the-myers-diff-algorithm-part-2/

class Myers:
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def shortest_edit(self):
        n, m = len(self._a), len(self._b)
        maximum = n + m

        # Creating a list of 0's with a distinct size
        v = [0] * (2 * maximum + 1)
        trace = list()

        # Now iterate d from 0 to maximum in the outer loop.. 
        for d in range(0, maximum):
            trace.append(v.copy())

            # ..and k from -d to d in steps of 2 in the inner loop
            for k in range(-d, d, 2):
                if k == -d or (k != d and v[k - 1] < v[k +1]):
                    x = v[k + 1]
                else:
                    x = v[k - 1] + 1
                
                y = x - k

                while x < n and y < m and self._a[x].text == self._b[y].text:
                    x, y = x + 1, y + 1
                
                v[k] = x

                if x >= n and y >= m:
                    return trace
    

    def backtrack(self):
        x, y = len(self._a), len(self._b)
        trace = self.shortest_edit()

        # Note: This is a kind of ugly adpation of the Ruby line
        #         trace.each_with_index.reverse_each do |v, d|
        for d,v in list(reversed(list(enumerate(trace)))):
            k = x - y

            if k == -d or (k != d and v[k - 1] < v[k + 1]):
                prev_k = k + 1
            else:
                prev_k = k - 1;
            
            prev_x = v[prev_k]
            prev_y = prev_x - prev_k

            



    def diff(self):
        if len(self._a) == 0:
            return
        
        if len(self._b) == 0:
            return

        self.backtrack()


class Diff:
    def diff(self, a, b):
        differ = Myers(Document(a).lines(), Document(b).lines())
        differ.diff()



if __name__ == "__main__":
    d = Diff()
    d.diff("Diff-Myers/testcase_15_FB101-02-Simple-Left.txt",
           "Diff-Myers/testcase_15_FB101-02-Simple-Right.txt")
