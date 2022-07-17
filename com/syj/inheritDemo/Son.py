from Father import Father


class Son(Father):

    def __init__(self, name, age, bir):
        super().__init__(name)
        self.age = age
        self.bir = bir
        print(f'this is son, name:{name}')

    def get_info(self):
        print(f'this is son, name :{self.name}, age:{self.age}')


if __name__ == '__main__':
    son = Son('nb', 18, '1990')
    son.get_info()