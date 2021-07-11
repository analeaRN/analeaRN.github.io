import math


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        
    def perimeter(self):
        return self.a + self.b + self.c
    
    def area(self):
        s = self.perimeter / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def scale(self, scale_factor):
        return Triangle(scale_factor * self.a, scale_factor * self.b, scale_factor * self.c)
    
    def is_valid(self):
        return self.a + self.b > self.c and \
               self.b + self.c > self.a and \
               self.c + self.a > self.b
               
    def is_right(self):
        return self.a ** 2 + self.b ** 2 == self.c ** 2
