# odd number
# for i in range(0, 100):
#     if i % 2 == 1:
#         print(i)

# function at python
def sum(x, y):
    return x*y
print(sum(2, 8))

# lambda function at python
def i_am_lambda(x, y): return x+y
print(i_am_lambda(2, 4))

# object oriented python
#class
class MyFirstClass:
    a= ""
    b=""

    def plus(self):
        return self.a + self.b

f_class = MyFirstClass()
f_class.a = 10
f_class.b =4
print(f_class.plus())

#class constructor method
class My_Magic:
    def __init__(self, name, do):
        self.name = name
        self.do = do

    def show_me(self):
        print("Name is " + self.name + " Do is " + self.do )

cons_one = My_Magic("Rahul", "Farmer")
cons_one.show_me()
