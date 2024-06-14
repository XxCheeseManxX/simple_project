## Writing unit tests with pytest!

# Installing pytest

`pip install -U pytest`

# Setup.py

```
from setuptools import setup, find_packages

setup(
    name="foo",
    version="1.0",
    packages=find_packages(),
)
```

`pip install -e .`

# Turn array.py into function

```
def numpy_mean(array):
    array = np.array(array)
    mean_val = np.mean(array)
    return mean_val
```

# Move array.py into the `src` directory

1. `mkdir src`
2. `mv array.py src`

# Create the test file

1. `mkdir tests`
2. `cd tests`
3. `code numpy_test.py`
4. 
```
from src import array

def test_numpy_mean():
    assert array.numpy_mean([1,2,3]) == 2
```

# Running pytest!

`pytest`