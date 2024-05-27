import tempfile
import tarfile
import os


def uncompressed_file(compressed_file):
    with tempfile.TemporaryDirectory() as temp_dir:
        tar_path = os.path.join(temp_dir, compressed_file.filename)
        compressed_file.save(tar_path)
        with tarfile.open(tar_path, "r:gz") as tar:
            tar.extractall(temp_dir)
    return tar_path


def parse_file_name(compressed_file):
    return "mock id"
