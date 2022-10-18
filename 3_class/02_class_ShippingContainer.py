class ShippingContainer:

    def __init__(self, owner_code, contents):
        self.owner_code = owner_code
        self.contents = contents

c1 = ShippingContainer("MAE", 'clothes')
print(c1.owner_code)
print(c1.contents)

c2 = ShippingContainer("YML", 'Books')
print(c2.owner_code)
print(c2.contents)