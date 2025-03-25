import unittest

def sum_funcs(a,b):
    return a+b

class TestDemo(unittest.TestCase):
    """
    the setUp() method (note the camel case) is used to set up any state that 
    is shared across multiple tests in a class. It runs before each individual 
    test method is executed.
    """
    def setUp(self):
        print(f"Inside the setUp call")
        self.a=10
        self.b=30

    """
    The setUpClass() method is a class method, which means it runs once for the 
    entire test class, rather than before each individual test.
    """
    @classmethod
    def setUpClass(cls):
        print(f"Inside the setUpClass Method")
        cls.a=20
        cls.b=30

    """
    the tearDown() method is used to clean up after each test method. It runs after each test method,
    and is typically used for tasks like closing files, releasing resources, or resetting states 
    that were modified during the test.
    """
    def tearDown(self):
        print(f"tearDown method is called")
        print('-'*20)

    def test_sum_funcs(self):
        print(f"Inside the test_sum_funcs call")
        result=sum_funcs(self.a,self.b)
        print(f"values of classmethod variable  is:{TestDemo.a},{TestDemo.b}") #we can access variable using cls.variable_name or className.variable_name
        self.assertEqual(result,self.a+self.b)
       

    def test_sum_funcs2(self):
        print(f"Inside the test_sum_funcs2 call")
        result=sum_funcs(self.a,self.b)
        self.assertEqual(result,self.a+self.b)


if __name__=="__main__":
    unittest.main()

        