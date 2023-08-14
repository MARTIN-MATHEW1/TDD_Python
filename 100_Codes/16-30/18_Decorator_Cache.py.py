import unittest

def cache_result(func):
    cache = {}
    
    def wrapper(*args, **kwargs):
        key = (*args, *kwargs.items())
        
        if key in cache:
            print("Retrieving result from cache...")
            return cache[key]
        
        result = func(*args, **kwargs)
        cache[key] = result
        return result
    
    return wrapper

@cache_result
def calculate_multiply(x, y):
    return x * y

class TestCacheResultDecorator(unittest.TestCase):

    def capture_output(self, func, *args, **kwargs):
        from io import StringIO
        import sys
        original_stdout = sys.stdout
        sys.stdout = StringIO()
        
        result = func(*args, **kwargs)
        output = sys.stdout.getvalue().strip()
        
        sys.stdout = original_stdout
        return result, output

    def test_cache_hit(self):
        result1, output1 = self.capture_output(calculate_multiply, 4, 5)
        result2, output2 = self.capture_output(calculate_multiply, 4, 5)

        self.assertEqual(result1, result2)
        self.assertIn("Retrieving result from cache", output2) 

    def test_cache_miss(self):
        result1, output1 = self.capture_output(calculate_multiply, 4, 5)
        result2, output2 = self.capture_output(calculate_multiply, 5, 6)

        self.assertNotEqual(result1, result2)
        self.assertNotIn("Retrieving result from cache", output2) 

if __name__ == "__main__":
    unittest.main()
