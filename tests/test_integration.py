import unittest
from robber import expect
from util import must_fail

class TestIntegration(unittest.TestCase):
    def test_eq_success(self):
        expect(1).to.eq(1)
        expect([1, 2]).to.eq([1, 2])
        expect((1, 2)).to.eq((1, 2))
        expect(1).to == 1
        expect(1) == 1

    @must_fail
    def test_eq_failure(self):
        expect(1).to.eq(2)

    def test_ne_success(self):
        expect(1).to.ne(2)
        expect(1).to.not_eq(2)
        expect(1).to != 2
        expect(1) != 2

    @must_fail
    def test_ne_failure(self):
        expect(1).to.ne(1)

    def test_equal_success(self):
        expect(1).to.equal(1)
        expect('foo').to.equal('foo')
        dict = {0: 1}
        expect(dict).to.equal(dict)

    @must_fail
    def test_equal_failure(self):
        expect({0: 1}).to.equal({0: 1})

    def test_not_equal_success(self):
        expect(1).to.not_equal(2)

    @must_fail
    def test_equal_failure(self):
        expect(1).to.not_equal(1)

    def test_true_success(self):
        expect(True).to.be.true()

    @must_fail
    def test_true_failure(self):
        expect(False).to.be.true()

    def test_false_success(self):
        expect(False).to.be.false()

    @must_fail
    def test_false_failure(self):
        expect(True).to.be.false()

    def test_instancef(self):
        expect(expect(None)).to.be.instanceof(expect)

    @must_fail
    def test_instancef(self):
        expect(expect(None)).to.be.instanceof(unittest.TestCase)
