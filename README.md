[![Build Status](https://secure.travis-ci.org/vesln/robber.py.png)](http://travis-ci.org/vesln/robber.py)

# robber.py - BDD / TDD assertion library for Python.

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

#### ne/not_eq/!=

Asserts that actual is not equal (!=) to expected:

```python
expect(1).to.ne(2)
expect(1).to.not_eq(2)
expect(1).to != 2
expect(1) != 2
```

#### equal

Asserts that the target is identical (is) to the expected:

```python
expect(1).to.equal(1)
```

#### not_equal

Asserts that the target is not identical (is) to the expected:

```python
expect({ 'test': 'robber' }).to.not_equal({ 'test': 'robber' })
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

#### not_match

Asserts that the target can not be matched by a regular expression:

```python
expect('bar').to.not_match(r'foo')
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

### Language chains

In order to write more readable assertions, there are a few
built-in language chains that you can use:

- to
- be
- a
- an
- have

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

```
$ pip install robber
```

## Requirements

- Python 2.6, 2.7 (3.2 not tested yet)
- pip

## Tests

```
$ nosetests tests/
```

## TODO

- close_to matcher
- use magic method to call the matchers
- Python 3.2?

## License

MIT License
