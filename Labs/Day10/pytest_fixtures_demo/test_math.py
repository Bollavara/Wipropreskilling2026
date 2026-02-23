from calculator import add, subtract

# xUnit-style methods
def setup_module(module):
    print("\n[SETUP MODULE] test_math_operations")

def teardown_module(module):
    print("\n[TEARDOWN MODULE] test_math_operations")

def setup_function(function):
    print("\n[SETUP FUNCTION]")

def teardown_function(function):
    print("\n[TEARDOWN FUNCTION]")


# -------------------------------
# Tests using fixtures
# -------------------------------

def test_addition(sample_numbers, calculator_resource):
    a, b = sample_numbers
    assert add(a, b) == 15

def test_subtraction(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5
