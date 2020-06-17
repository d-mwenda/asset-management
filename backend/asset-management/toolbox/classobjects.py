class ClassTest:
    ''' This is a simple class to test class objects'''

    i = 2

    def j(self):
        return 'This is a function'

#    m =j()

c = ClassTest()
print(ClassTest.i)
print(ClassTest().j())
print(c.j())
# print(ClassTest.m)
print(ClassTest.__doc__, ClassTest.__class__)
print(ClassTest.__dict__)


class InstantiatedClass:

    def __init__(self, **kwargs):
        self.r = kwargs['real']
        self.i = kwargs['imaginary']


n = InstantiatedClass(real=3, imaginary=-5)
print('The real part is %r while the imaginary part is %i', (n.r, n.i))
