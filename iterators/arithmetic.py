from progression import Progression

class ArithmeticProgression(Progression):
    def __init__(self, increment=0, start=0):
        super(ArithmeticProgression,self).__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

if __name__ == "__main__":
    obj = ArithmeticProgression(2, 5)
    obj.print_progression(10)
