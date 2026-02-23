import pytest

# Function-scoped fixture
@pytest.fixture(scope="function")
def sample_numbers():
    return (10, 5)

# Module-scoped fixture
@pytest.fixture(scope="module")
def calculator_resource():
    print("\n[SETUP] Calculator resource created")
    yield
    print("\n[TEARDOWN] Calculator resource destroyed")
