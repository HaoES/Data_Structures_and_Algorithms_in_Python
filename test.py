import re

class Poly():
    def __init__(self,s):
        self._derivative = {}
        self._poly = {}
        self._list = [i for i in re.findall(r'(?:-)?\d*(?:x(?:\^\d+)?)?', re.sub(r'([-])\s+', r'\1', s)) if i != ''] # regex to delimit polynomials
    # filling up the dictionary with degrees and coefficients
        for i in self._list:
            check_carrat = i.find('^')
            check_x = i.find('x')
            if check_carrat == -1:
                if check_x == -1:
                    self._poly[0] = int(i)
                else:
                    self._poly[1] = int(i[:check_x])
            else:
                if check_x == 0:
                    self._poly[int(i[check_carrat + 1:])] = 1
                else:
                    self._poly[int(i[check_carrat + 1:])] = int(i[:check_x])
    def print_derivative(self):
        """
           printing the polynomial 
        """
        self._print = []
        for i in self._derivative:
            if i == 0:
                self._print.append(str(self._derivative[i]))
                continue
            if int(self._derivative[i]) >= 0:
                if int(self._derivative[i]) == 1:
                    self._derivative[i] = ''
                self._print.append(f'+ {self._derivative[i]}x^{i} ')
            else:
                self._print.append(f'{self._derivative[i]}x^{i} ')
        if self._print[0][0] == '+':
            return(''.join(self._print)[1:])
        else:
            return(''.join(self._print))

    def derivative(self):
        """
            Derivate the polynomial
        """
        self._derivative = {}
        for key, value in self._poly.items():
            if key > 0:
                self._derivative[key - 1] = key * value

print(""" Welcome to the this small polynomial program! 
The goal of this program is to take a polynomial in the arithmetic form as an input
and outputs its derivative.
Note: Arithmetic form is "2x^3 + 3x^2 - 20x + 50"
""")
a = input("Type a polynomial in arithmetic form:  \n")
p = Poly(a)
p.derivative()
print(f" The derivative of {a} is: \n")
print(p.print_derivative())
