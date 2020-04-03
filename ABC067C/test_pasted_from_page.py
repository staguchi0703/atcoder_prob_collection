#
from resolve import resolve
####################################
####################################
# 以下にプラグインの内容をペーストする
#  
import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        print('-----------------')
        print(out)
        
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """6
1 2 3 4 5 6"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
10 -10"""
        output = """20"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()