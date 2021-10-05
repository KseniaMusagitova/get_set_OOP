# Режим доступа, геттеры и сеттеры
class Student:
    def __init__(self, name='Ivan', age=18, groupNumber='10A'):
        self.__name = name
        self.__age = age
        self.__groupNumber = groupNumber

    def setName(self, name):
        self.__name = name

    def setAge(self, age):
        self.__age = age

    def setGroupNumber(self, groupNumber):
        self.__groupNumber = groupNumber

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getGroupNumber(self):
        return self.__groupNumber


s = Student()
s.setName('Slava')
print(s.getName())

s.setGroupNumber(11)
print(s.getGroupNumber())

# Создание свойств
class Student:
    def __init__(self, name='Ivan', age=18, groupNumber=10):
        self.__name = name
        self.__age = age

    def __valueISNumber(value):
        if isinstance(value, int):
            return True
        return False

    def __getName(self):
        return self.__name

    def __setStudentName(self, name):
        self.__name = name

    def __getAge(self):
        return self.__age

    def __setStudentAge(self, age):
        if Student.__valueISNumber(age):
            self.__age = age
        else:
            raise ValueError('Неправильный тип данных')

    name = property(__getName, __setStudentName)
    age = property(__getAge, __setStudentAge)


s = Student('VOVA', 20)


s.name = 'Vova'
s.age = 19
print(s.name, s.age)

s.name = 'Mike'
print(s.__dict__)
