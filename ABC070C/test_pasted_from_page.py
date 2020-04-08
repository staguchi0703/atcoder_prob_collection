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
    def test_入力例_1(self):
        input = """2
2
3"""
        output = """6"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """75
22
1968854689373829
87153
51936214827607
174306
89708007429503
37408239098102751
5282
89708007429503
57
417
28328844451422
311617288965642
822981260158260522
14164422225711
2
5920728490347198
103872429655214
28328844451422
7219133861037373
418
418
7219133861037373
29051
2960364245173599
411490630079130261
3058
7219133861037373
834
33
14164422225711
51936214827607
114
24938826065401834
139
4587
418
6
7219133861037373
15846
834
51936214827607
311617288965642
155808644482821
7923
14164422225711
179416014859006
155808644482821
139
3058
418
7219133861037373
1973576163449066
2960364245173599
139
418
33
14438267722074746
139
7219133861037373
38
538248044577018
1973576163449066
278
137163543359710087
1254
269124022288509
43314803166224238
417
274327086719420174
21657401583112119
656284896457943
5282
209
38"""
        output = """822981260158260522"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()