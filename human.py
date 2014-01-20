class Human:
    age = 30
    height = 180
    name = "Zero"

    def get_older(self):
        self.age += 1


def main():
    h = Human()
    print('Age: %d' % h.age)
    h.get_older()
    print('Age: %d' % h.age)
    print('Name is: %s' % h.name)

main()
