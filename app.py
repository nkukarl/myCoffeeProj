from random import choice


class Person:
    def __init__(self, name):
        self.greeting = '<div>Hello {name}<div>'
        self.name = name

    def __str__(self):
        return self.make_greeting()

    def make_greeting(self):
        return self.greeting.format(name = self.name)


def main():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    people = [Person(c) for c in alphabet]

    person = choice(people)
    print person

if __name__ == '__main__':
    for i in range(10):
        print i,
        main()
