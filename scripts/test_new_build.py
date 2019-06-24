import os
import sys
import pytest
import selenium
sys.path.append(os.getcwd())



class Test01:
    def setup(self):
        pass
    def teardown(self):
        pass
    def test_new(self,name,tel):
        assert 1
