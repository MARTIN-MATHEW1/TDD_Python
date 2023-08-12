import unittest

def custom_function(arg1, *args, kwarg1=None, **kwargs):
    result = f"arg1: {arg1}\n"
    
    if args:
        result += f"args: {args}\n"
    
    if kwarg1 is not None:
        result += f"kwarg1: {kwarg1}\n"
    
    if kwargs:
        result += "kwargs:\n"
        for key, value in kwargs.items():
            result += f"  {key}: {value}\n"
    
    return result

class TestCustomFunction(unittest.TestCase):

    def test_args_and_kwargs(self):
        expected_output = (
            "arg1: 1\n"
            "args: (2, 3)\n"
            "kwarg1: 4\n"
            "kwargs:\n"
            "  key1: value1\n"
            "  key2: value2\n"
        )
        result = custom_function(1, 2, 3, kwarg1=4, key1='value1', key2='value2')
        self.assertEqual(expected_output, result)

if __name__ == "__main__":
    unittest.main()
