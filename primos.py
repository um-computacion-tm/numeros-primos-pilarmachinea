import unittest

def is_primo(value):
    div = 2
    while div<value:
        if value % div == 0:
            return False
        div += 1
    return True

class testprimos(unittest.TestCase):
    def test1(self):
        result = is_primo(1)
        self.assertEqual(result , True)

    def test2(self):
        result = is_primo(2)
        self.assertEqual(result , True)

    def test4(self):
        result = is_primo(4)
        self.assertEqual(result , False)

unittest.main()
