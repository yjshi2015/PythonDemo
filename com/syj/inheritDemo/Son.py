from Father import Father


class Son(Father):

    def __init__(self, name, age, bir):
        super().__init__(name)
        self.age = age
        self.bir = bir
        print(f'this is son init, name:{name}, age:{self.age}, bir:{self.bir}')

    def get_info(self):
        print(f'this is son get_info, name :{self.name}, age:{self.age}, bir:{self.bir}')


if __name__ == '__main__':
    son = Son('nb', 18, '1990')
    son.get_info()