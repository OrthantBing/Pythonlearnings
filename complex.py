from __future__ import division
import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, no):
        a = self.real + no.real
        b = self.imaginary + no.imaginary
        return Complex(a,b)

    def __sub__(self, no):
        a = self.real - no.real
        b = self.imaginary - no.imaginary
        return Complex(a,b)

    def __mul__(self, no):
        a, b = self.real * no.real - self.imaginary * no.imaginary, self.imaginary * no.real + no.imaginary * self.real
        return Complex(a,b)

    def mod(self):
        return Complex(math.sqrt(self.real * self.real + self.imaginary * self.imaginary),0)

    def __div__(self, no):
        denominator = no.real * no.real + no.imaginary * no.imaginary
        a, b = float(self.real * no.real - ( self.imaginary * (-no.imaginary))) / float(denominator), float(self.real * (-no.imaginary) + no.real * self.imaginary) / float(denominator)
        return Complex(a,b)


    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00%.2fi" % (self.imaginary)
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f%.2fi" % (self.real, self.imaginary)
        return result
