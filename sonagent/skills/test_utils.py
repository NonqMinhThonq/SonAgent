import unittest
from unittest.mock import patch
from pytest.utils import read_text_from_file, hash_str, hash_md5_str 

class TestFileFunctions(unittest.TestCase):
    
    def test_read_text_from_file(self):
        with patch("builtins.open", create=True) as mock_open:
            mock_open.return_value.read.return_value = "Test content"
            file_path = "test_file.txt"
            content = read_text_from_file(file_path)
            mock_open.assert_called_once_with(file_path, "r")
            self.assertEqual(content, "Test content")
    
    def test_hash_str(self):
        string_to_hash = "Hello, world!"
        expected_hash = "315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3"
        self.assertEqual(hash_str(string_to_hash), expected_hash)
    
    def test_hash_md5_str(self):
        string_to_hash = "Hello, world!"
        expected_md5_hash = "6cd3556deb0da54bca060b4c39479839"
        self.assertEqual(hash_md5_str(string_to_hash), expected_md5_hash)

if __name__ == '__main__':
    unittest.main()
