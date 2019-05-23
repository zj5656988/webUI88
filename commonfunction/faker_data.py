from faker import Faker
class Faker_data():
    faker = Faker(locale="ZH-cn")
    def __init__(self):
        faker = Faker(locale="ZH-cn")

    def faker_address(self):
        f=Faker_data.faker

        return f.address()

if __name__ == '__main__':
    f=Faker_data().faker_address()
    print(f)


