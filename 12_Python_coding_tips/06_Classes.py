class MyClass:
    MyVar = 0

# creating an instance

# You have just created an instance of MyClass named MyInstance.
# Of course, you’ll want to verify that you really have created such an
# instance.
MyInstance = MyClass()

# The output of 0, as shown in Figure 14-1, demonstrates that MyInstance
# does indeed have a class variable named MyVar.
print(MyInstance.MyVar)

# The output tells you that this class is part of the __main__
# module, which means that you typed it directly into the shell.
print(MyInstance.__class__)

# Use the dir() function to determine which builtin
# attributes are present.
print(dir(MyInstance))

# This method doesn’t accept any arguments and doesn’t return any
# values. It simply prints a message as output.
# However, the method works just fine for demonstration purposes.
class MyClass2:
    def SayHello(): # The example class contains a single defined attribute, SayHello().
        print('Hello there!')

# There is no need to create an instance of the class: it is ready to use.
# NO - MyInstance = MyClass2()
print(MyClass2.SayHello())