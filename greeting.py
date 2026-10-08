import unittest
class TestBug2(unittest.Testcase):
     def test_greets_by_name(self):
         from gretting import greet
         self.assertEqual(greet("Sam), "Hello, Sam!")
     
     def test_greets_without_name(self):
         from gretting import greet
         self.assertEqual(greet(""), "Hello, there!")

if __name__ == "__main__":
    unittest.main()
