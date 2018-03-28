import unittest
from problem1 import *
from problem2 import *


class TestGoldenCrown(unittest.TestCase):

    def setUp(self):
        self.test_list1 = ['dsf', 'df']
        self.test_msg_format = 'FEW, "345SDFSFV"'

    def test_inputformat(self):
        self.assertEqual(input_format('test_input.txt'), ["hi", "bye", ""])

    def test_check_for_min_msg(self):
        self.assertEqual(check_for_min_msg(self.test_list1), False)

    def test_check_msg_format(self):
        self.assertEqual(check_msg_format(self.test_msg_format),
                                         ('FEW', '345SDFSFV'))

    def test_decrypt_secret_msg(self):
        self.assertFalse(decrypt_secret_msg('ICE', 'sadgffsd'))

    def test_golden_crown(self):
        self.assertTrue(golden_crown('input.txt'))


class TestBreakerOfChains(unittest.TestCase):

    def setUp(self):
        self.sender = "ICE"
        self.reciever = "FIRE"
        self.ballot = [['ICE', 'FIRE', 'sgerbe'], ['ICE', 'WATER', 'sdFgsg']]

    def test_add_to_ballot(self):
        self.assertEqual(type(add_to_ballot(self.sender, self.reciever,
                                            self.ballot)), list)

    def test_pick_random(self):
        self.assertNotEqual(pick_random(1, self.ballot), [])

    def test_find_alliance(self):
        self.assertEqual(find_alliance(self.ballot), [])

    def test_breaker_of_chains(self):
        self.assertNotEqual(breaker_of_chains(['ICE', 'SPACE']), ['ICE'])


if __name__ == '__main__':
    unittest.main()
