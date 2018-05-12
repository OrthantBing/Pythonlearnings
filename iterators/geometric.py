from __future__ import print_function
from progression import Progression


class GeometricProgression(Progression):
    def __init__(self, base=2, start=1):
        super(GeometricProgression, self).__init__(start)
        self._base = base
        print(self._base)

    def _advance(self):

        self._current *= self._base


if __name__ == "__main__":
    obj = GeometricProgression(81, 1 / 3)
    obj.print_progression(10)
