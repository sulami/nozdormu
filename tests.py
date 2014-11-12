from unittest import TestCase, main

from timer import Timer

def a():
    pass

def b():
    pass

class TimingTestCase(TestCase):
    def test_single_function(self):
        t = Timer(a)
        t.run()
        self.assertIn('0.00', t.output()) # This should run fast

    def test_multiple_functions(self):
        t = Timer([a, b])
        t.run()
        self.assertIn('0.00', t.output()) # This should run fast

if __name__ == '__main__':
    main()

