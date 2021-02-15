import unittest
import Tarea

class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(Tarea.hist(), True)
        self.assertEqual(Tarea.pali(), True)
        
if __name__ == "__main__":
    unittest.main()