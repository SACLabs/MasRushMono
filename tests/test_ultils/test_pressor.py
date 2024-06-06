import os
import pytest
from masr.ultils.pressor import (
    compress_file,
    decompress_file,
)  # 确保替换为正确的模块名

# 测试用的文件路径
TEST_INPUT_FILE = "./tests/test_ultils/test_input.txt"
TEST_COMPRESSED_FILE = "./tests/test_ultils/test_ultilstest_output.zst"
TEST_DECOMPRESSED_FILE = "./tests/test_ultils/test_ultilstest_decompressed.txt"


def setup_module(module):
    """开始测试 创建一个测试txt文件"""
    with open(TEST_INPUT_FILE, "w") as f:
        f.write("This is a test file with sample text.")


def teardown_module(module):
    """测试结束 删除相关文件"""
    os.remove(TEST_INPUT_FILE)
    if os.path.exists(TEST_COMPRESSED_FILE):
        os.remove(TEST_COMPRESSED_FILE)
    if os.path.exists(TEST_DECOMPRESSED_FILE):
        os.remove(TEST_DECOMPRESSED_FILE)


def test_file_compression():
    """压缩测试"""
    compress_file(TEST_INPUT_FILE, TEST_COMPRESSED_FILE)
    assert os.path.exists(
        TEST_COMPRESSED_FILE
    ), "Compressed file does not exist."


def test_file_decompression():
    """解压 并比较文件内容"""
    # Ensure the file is compressed for this test
    compress_file(TEST_INPUT_FILE, TEST_COMPRESSED_FILE)
    decompress_file(TEST_COMPRESSED_FILE, TEST_DECOMPRESSED_FILE)
    assert os.path.exists(
        TEST_DECOMPRESSED_FILE
    ), "Decompressed file does not exist."
    with open(TEST_DECOMPRESSED_FILE, "r") as f:
        content = f.read()
    assert (
        content == "This is a test file with sample text."
    ), "Decompressed file content does not match."


def test_missing_input_file():
    """input path error"""
    with pytest.raises(FileNotFoundError):
        compress_file("non_existent_file.txt", TEST_COMPRESSED_FILE)

    with pytest.raises(FileNotFoundError):
        decompress_file("non_existent_file.zst", TEST_DECOMPRESSED_FILE)
