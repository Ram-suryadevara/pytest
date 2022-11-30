import pytest
import os


class TestMyStuff():
    def test_type(self):
        assert type(1.3) == int

    def test_strs(self):
        assert str.upper('python') == "PYTHOn"
        assert "pytest".capitalize() == "Pytest"


if __name__ == '__main__':
    pytest.main(args=['-sv', os.path.abspath(__file__)])
