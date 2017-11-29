class Progression(object):
    def __init__(self, start=0):
        self._current = start

    def __iter__(self):
        return self

    def next(self):
        if self._current is None:
            raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer
    
    def _advance(self):
        self._current += 1

    def print_progression(self, n):
        print (' '.join(str(self.next)) for j in range(n)))

if __name__ == "__main__":
    obj = Progression()
    obj.print_progression(10)
    