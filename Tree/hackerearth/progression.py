class Progression:
	"""Iterator producing generic progression.
	"""

	def __init__(self, start=0):
		"""Constructor, initialize current to first value
		Of the progression.
		"""
		# weak encapsulation is established by naming conventions
		# by adding _ to the protected variables.
		self._current = start	

	def _advance(self):
		"""Update self._current to a new value
        This should be overridden by a subclass to customize progression.	
		"""
		Self._current += 1

	def __next__(self):
		if self._current is None:
			raise StopIteration()
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        """By convention an iterator must return itself as an iterator"""
        return self

    def print_progression(self, n):
        print(" ".join(str(next(self)) for i in range(n)))


class GeometricProgression(Progression): # inherit from Progression
    def __init__(self, base=2, start=1):
        """Create a new geometric progression

        base    the fixed constant (defaults to 2)
        start   the first term of the progression (defaults to 1)
        """
        super().__init__(start)     #Initialize the base class
        self._base = base

    def _advance(self):             # Override inherited version
        self._current *= self._base


if __name__ == '__main__':
    print('Default progression: ')
    Progression().print_progression(10)

    """Result:
    Default progression:
    0 1 2 3 4 5 6 7 8 9
    """

    print('Geometric progression with default base:')
    GeometricProgression().print_progression(10)

    """Result:
    Geometric progression with default base:
    1 2 4 8 16 32 64 128 256 512
    """"

    print('Geometric progression with baase 3:')
    GeometricProgression(3).print_progression(10)

    """Result:
    Geometric progression with base 3:
    1 3 9 27 81 243 729 2187 6561 19683
    """
