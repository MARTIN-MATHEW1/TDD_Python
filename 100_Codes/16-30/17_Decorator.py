import unittest


def decorator(func):
    def wrap(*args, **kwargs):

        print(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")

        result = func(*args, **kwargs)
        return result
    return wrap

@decorator
def multiply_numbers(x, y):
    return x * y


@decorator
def add_numbers(x, y):
    return x + y

# Call the decorated function
# func_calls = multiply_numbers, add_numbers
# result = [i(10,20) for i in func_calls]
# print(result)


class Multiply_Addition(unittest.TestCase):
    def test_Decorator_Add_Mul(self):
        multiplication = multiply_numbers(10,2)
        addition = add_numbers(10,2)
        results = multiplication, addition
        expected = (20,12)
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()

