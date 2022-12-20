from abc import ABC, abstractmethod

class Convertion(ABC):

    @abstractmethod
    def upper_case_conversion(self, *args):
        pass


class StringConversion(Convertion):

    def upper_case_conversion(self, *args):
        for data in args:
            print(data.upper())

if __name__ == '__main__':
    obj = StringConversion()
    obj.upper_case_conversion('Python', 'Programming')

str1 = "Hello"
str1.upper()

