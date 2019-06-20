import unittest
import os
import bcollector.config


class TestArray(unittest.TestCase):
    def test_prod_env(self):
        os.environ["PYTHON_ENV"] = "production"
        bconfig = bcollector.config.FileConfig('tests/config.json')
        self.assertEqual(bconfig.is_prod, True)

    def test_dev_env(self):
        try:
            if os.environ["PYTHON_ENV"] == "production":
                os.environ.unsetenv["PYTHON_ENV"]
        except:
            pass

        bconfig = bcollector.config.FileConfig('tests/config.json')
        self.assertEqual(bconfig.is_prod, False)
