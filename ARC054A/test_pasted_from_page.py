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
        print('------------')
        print(out)
        print('------------')
        self.assertEqual(out, output)
    def test_入力例1(self):
        input = """6 2 3 1 5"""
        output = """0.8000000000"""
        self.assertIO(input, output)
    def test_入力例2(self):
        input = """6 2 10 1 5"""
        output = """0.2500000000"""
        self.assertIO(input, output)
    def test_入力例3(self):
        input = """6 3 1 5 3"""
        output = """1.0000000000"""
        self.assertIO(input, output)
    def test_入力例4(self):
        input = """10 7 7 6 0"""
        output = """0.2857142857"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()