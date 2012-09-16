# robber.py

## Description

BDD / TDD assertion library for Python.

## Synopsis

In order to use `robber`, you need to import `expect`
from the module:

```python
from robber import expect
```

That's all. You are good to go.

### Assertions

#### eq/==

Asserts that actual is equal (==) to expected:

```python
    expect(1).to.eq(1)
    expect([1, 2]).to.eq([1, 2])
```
Also:

```python
expect(1) == 1
```

### ne/not_eq/!=

### Custom assertions

### Custom error messages

## Installation

```
$ pip install robber
```

## Requirements

- Python 2.6+
- pip

## Tests

## License

MIT License
