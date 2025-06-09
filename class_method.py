class Employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the value of a is {cls.a}")

z = Employee()
z.a = 45

z.show()