import unittest
from utils import get_time_until_timeout

class TestDeadManSwitch(unittest.TestCase):
    def test_time_until_timeout(self):
        last_activation_time = 1625670000  # Simulated timestamp
        timeout = 604800  # 1 week in seconds
        time_remaining = get_time_until_timeout(last_activation_time, timeout)
        self.assertIn("Time remaining", time_remaining)

if __name__ == '__main__':
    unittest.main()
