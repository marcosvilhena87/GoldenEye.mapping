import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from validate_catalog import validate

class CatalogTests(unittest.TestCase):
    def test_cross_references(self):
        validate()

if __name__ == "__main__":
    unittest.main()
