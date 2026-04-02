import pytest
import sys
import os
from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from src.main import hello, process_data


class TestHelloFunction:  
    def test_hello_returns_string(self):
        result = hello()
        assert isinstance(result, str)
    
    def test_hello_content(self):
        result = hello()
        assert "Hello" in result
        assert "Docker" in result


class TestDataProcessing:  
    def test_process_data_with_valid_input(self):
        data = {"value": 10, "multiplier": 2}
        result = process_data(data)
        assert result == 20
    
    def test_process_data_with_zero(self):
        data = {"value": 0, "multiplier": 5}
        result = process_data(data)
        assert result == 0
    
    def test_process_data_missing_key(self):
        data = {"multiplier": 2}
        with pytest.raises(KeyError):
            process_data(data)


class TestProjectStructure:
    def test_src_directory_exists(self):
        assert (ROOT_DIR / "src").exists()
    
    def test_tests_directory_exists(self):
        assert (ROOT_DIR / "tests").exists()
    
    def test_requirements_exists(self):
        assert (ROOT_DIR / "requirements.txt").exists()