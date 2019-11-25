import unittest


class TestLoan(unittest.TestCase):
    def test_NextMonthBalance(self):
        self.assertEqual(Loan(), False)


if __name__ == '__main__':
    unittest.main()
