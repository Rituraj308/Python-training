import unittest
from Unitester import do_stuff  # Adjust import statement according to your module structure


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'shkshs'
        result = do_stuff(test_param)
        self.assertIsInstance(result,ValueError)    #insted od assertTrue() we can use asserIsInstance

    def test_do_stuff3(self):
        test_param = None
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')

    def test_do_stuff4(self):
        test_param = ''
        result = do_stuff(test_param)
        self.assertEqual(result, 'please enter number')


if __name__ == '__main__':
      unittest.Unitester()      #we can aslo use unittest.main