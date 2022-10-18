class MyClass:

    # Define class attributes in the class block
    my_class_attribute = "class attributes go here"
    MY_CONSTANT = "they are often class-specific container"

    def __init__(self):
        self.my_instance_attribute = 'instance attributes here'

### EXAMPLE WITH SHIPPING CONTAINER
class ShippingContainer:

    next_serial = 1337

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents
        self.serial = self.next_serial
        self.next_serial += 1