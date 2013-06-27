class Foo(object):
    def __init__(self):
        self.some_attr = "foo"

    def __getattribute__(self, attr):
        attribute = object.__getattribute__(self, attr)
        object.__setattr__(self, attr, "you're too late!")
        return attribute


def go():
    f = Foo()
    word = self.some_attr
    print word
    print self.some_attr

if __name__ == '__main__':
    go()

# next to pursue
# GC, can we reference count and delete references
# inspect module, can we capture assignments and do something
