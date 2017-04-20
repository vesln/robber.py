[![Build Status](https://secure.travis-ci.org/taoenator/robber.py.png)](http://travis-ci.org/taoenator/robber.py)
[![Coverage Status](https://coveralls.io/repos/github/taoenator/robber.py/badge.svg?branch=master)](https://coveralls.io/github/taoenator/robber.py?branch=master)


# robber.py - BDD / TDD assertion library for Python.
## Supported python versions
- `robber.py` now supports python 2.6, 2.7, 3.4, 3.5 and python 3.6

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

#### ne/!=

Asserts that actual is not equal (!=) to expected:

```python
expect(1).to.ne(2)
expect(1).to != 2
expect(1) != 2
```

#### equal

Asserts that the target is identical (is) to the expected:

```python
expect(1).to.equal(1)
```

#### true

Asserts that the target is True:

```python
expect(True).to.be.true()
```

#### false

Asserts that the target is False:

```python
expect(False).to.be.false()
```

#### instanceof

Asserts that the target is an instance of expected:

```python
expect(obj).to.be.instanceof(Klass)
```

#### match

Asserts that the target can be matched by a regular expression:

```python
expect('foo').to.match(r'foo')
```

#### respond_to

Asserts that the target responds to a method:

```python
expect(obj).to.respond_to('method')
```

#### truthy

Asserts that the target is truthy:

```python
expect(['test']).to.be.truthy()
```

#### falsy

Asserts that the target is falsy:

```python
expect([]).to.be.falsy()
```

#### length

Asserts that the target has a length of expected:

```python
expect([1, 2]).to.have.length(2)
expect('str').to.have.length(3)
```

#### empty

Asserts that the target is empty:

```python
expect([]).to.be.empty()
expect('').to.be.empty()
```

#### string

Asserts that the target is a string:

```python
expect('str').to.be.a.string()
```

#### integer

Asserts that the target is an integer:

```python
expect('str').to.be.an.integer()
```

#### float

Asserts that the target is floating point number:

```python
expect(1.0).to.be.a.float()
```

#### list

Asserts that the target is a list:

```python
expect([1, 2]).to.be.a.list()
```

#### dict

Asserts that the target is a dictionary:

```python
expect({}).to.be.a.dict()
```

#### tuple

Asserts that the target is a tuple:

```python
expect((1, 2)).to.be.a.tuple()
```

#### none

Asserts that the target is None:

```python
expect(None).to.be.none()
```

#### above

Asserts that the target is above expected:

```python
expect(2).to.be.above(1)
```

#### below

Asserts that the target is below expected:

```python
expect(1).to.be.below(2)
```

#### within

Asserts that the target is within expected:

```python
expect(2).to.be.within(0, 2)
```

#### contain

Asserts that the target contains an element, or a key:
```python
expect([1,2,3]).to.contain(2)
expect({'foo': 'bar'}).to.contain('foo')
```

#### exclude

Asserts that the target does not contain an element, or a key:

```python
expect({'foo': 'bar'}).to.exclude('baz')
```

#### throw

Asserts that the target throws an exception

```python
expect(lambda: raise_exception(...)).to.throw(Exception)
expect(any_callable).to.throw(Exception)
```

#### called

Asserts that a mock has been called

```python
expect(mock).to.be.called()
```

#### called_once

Asserts that a mock has been called exactly one time

```python
expect(mock).to.be.called_once()
```

#### callable

Asserts that a object is callable 

```python
expect(object).to.be.callable()
```

#### called_with

Asserts that a mock has been called with params 

```python
expect(mock).to.be.called_with(*args, **kwargs)
```

#### called_once_with

Asserts that a mock has been called once with params 

```python
expect(mock).to.be.called_once_with(*args, **kwargs)
```

#### ever_called_with

Asserts that a mock has ever been called with params. 
The call is not necessary to be to latest one (the same as assert.any_call).

```python
expect(mock).to.have.been.ever_called_with(*args, **kwargs)
```

### Language chains

In order to write more readable assertions, there are a few
built-in language chains that you can use:

#### Positive chains
- to
- be
- been
- a
- an
- have

#### Negative chains
- not_to

For example, the following two lines are functionally equivalent:

```python
expect(1.0).to.be.a.float()
expect(1.0).float()
```

### Expectation chaining

In the spirit of more readable assertions, and to eliminate redundant
evaluations of the same expression, you can chain multiple expectations.

For example, the following two lines are functionally equivalent.
The first example evaluates the expression '1 + 1' only once:

```python
expect(1 + 1).to.be.an.integer().to.be.within(1, 3)

expect(1 + 1).to.be.an.integer()
expect(1 + 1).to.be within(1, 3)
```

### Custom assertions

Writing custom assertion is as easy as extending a base
matcher class and adding two methods - matches for matching
and failure_message for the error notice:

```python
class Chain(Base):
    def matches(self):
        expectation = self.actual(None)
        chain = getattr(expectation, self.expected)
        return expectation is chain

    def failure_message(self):
        return 'Expected "%s" to have chain "%s"' % (self.actual, self.expected)

expect.register('chain', Chain)
```

After you register the new matcher, you can use it as expected:

```python
expect(obj).to.have.chain('be')
```

### Custom error messages

If you want to have custom failure messages, for
assertion or group of assertions, you can simply do:

```python
from robber import failure_message

with failure_message('Something went wrong'):
    expect(1).to.eq(2)
```

## Installation

```bash
$ pip install robber
```

## Requirements

- Python 2.6, 2.7 or 3.5
- pip
- nose (for testing)

## Tests

```bash
$ nosetests tests/
```

## License

MIT License
