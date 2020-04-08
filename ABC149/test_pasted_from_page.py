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
        print('---------->', out)
        self.assertEqual(out, output)
    def test_入力例_1(self):
        input = """5 2
8 7 6
rsrpr"""
        output = """27"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7 1
100 10 1
ssssppr"""
        output = """211"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """4 3
5172 4873 5936
rrpr"""
        output = """16745"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()