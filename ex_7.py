'''Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число»,
реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.'''

class Complex:

    def __init__(self, real, imadinary):
        self.real = real
        self.imadinary = imadinary

    def __add__(self, other):
        return Complex(self.real + other.real, self.imadinary + other.imadinary)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imadinary * other.imadinary,
                       self.real * other.imadinary + self.imadinary * other.real)

    def __str__(self):
        return f"{self.real} + {self.imadinary}j"

my_complex_number_1 = Complex(9, 5)
my_complex_number_2 = Complex(-5, 6)
print(f"Сумма: {my_complex_number_1 + my_complex_number_2}")
print(f"Произведение: {my_complex_number_1 * my_complex_number_2}")

my_number_1 = complex(9, 5)
my_number_2 = complex(-5, 6)
print(my_number_1 + my_number_2)
print(my_number_1 * my_number_2)