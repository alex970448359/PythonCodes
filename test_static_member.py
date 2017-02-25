class TestClassMethod(object):

    METHOD = 'method hoho'

    def __init__(self):
        self.name = 'leon'

    def test1(self):
        print 'test1'
        print self
        print self.METHOD
        print self.name
        print TestClassMethod.METHOD

    @classmethod
    def test2(cls):
        print 'test2'
        print cls
        print self.name
        print TestClassMethod.METHOD

    @staticmethod
    def test3():
        print 'test3'
        print self.name
        print TestClassMethod.METHOD

if __name__ == '__main__':
    a = TestClassMethod()
    a.test1()
    a.test2()
    a.test3()
    TestClassMethod.test3()
