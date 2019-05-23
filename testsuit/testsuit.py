import unittest
from case.test_login import Login_case
from case.test_task import test_Task
from commonfunction.driver import Driver
if __name__ == '__main__':


    suit=unittest.TestSuite()
    addsuit=[Login_case("test_001"),Login_case("test_002")]
    suit.addTests(addsuit)
    runner=unittest.TextTestRunner()
    runner.run(suit)