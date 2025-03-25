import unittest


def sum(a,b):
    return a+b

class TestDemo(unittest.TestCase):
    def test_funcs(self):
        pass

    def test_funcs2(self):
        pass

    def test_sum_funcs(self):
        # Arange
        a=10
        b=20

        # Act
        result=sum(2,3)

        # Assert
        self.assertEqual(result,a+b)


class TestDemo2(unittest.TestCase):
    """
    When we use same method name in different classes still its treated each test method independently
    means if there is method test_funcs is in TestDemo class and same function has in TestDemo2 class 
    then total Ran test are 2 instead of 1
    """
    def test_demo(self):   
        pass

if __name__=="__main__":
    unittest.main()