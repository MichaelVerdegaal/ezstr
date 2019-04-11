from ezstr import tostr

@tostr
class Mango:
    def __init__(self, value_1, value_2):
        self.attribute_1 = value_1
        self.attribute_2 = value_2


m = Mango('Orange', 'Nice')
print(m)