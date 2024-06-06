import os

import zstandard as zstd


def compress_file(input_file_path, output_file_path, compression_level=3):
    try:
        # 检查输入文件是否存在
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError(
                f"compress_file: \
                                    No file found at specified path: \
                                    {input_file_path}"
            )

        with open(input_file_path, "rb") as input_file:
            with open(output_file_path, "wb") as output_file:
                compressor = zstd.ZstdCompressor(level=compression_level)
                compressor.copy_stream(input_file, output_file)
                print(f"Compress, from {input_file} to {output_file}")
    except Exception as e:
        print(f"Compress, error: {e}")
        raise e


def decompress_file(input_file_path, output_file_path):
    try:
        # 检查输入文件是否存在
        if not os.path.isfile(input_file_path):
            raise FileNotFoundError(
                f"decompress_file: \
                                    No file found at specified path: \
                                        {input_file_path}"
            )

        with open(input_file_path, "rb") as input_file:
            with open(output_file_path, "wb") as output_file:
                compressor = zstd.ZstdDecompressor()
                compressor.copy_stream(input_file, output_file)
                print(f"Decompress, from {input_file} to {output_file}")
    except Exception as e:
        print(f"Decompress, error: {e}")
        raise e


"""
# 定义输入和输出文件路径
input_path = 'example.txt'
compressed_path = 'example.txt.zst'
decompressed_path = 'example_decompressed.txt'

# 压缩文件
compress_file(input_path, compressed_path)

# 解压文件
decompress_file(compressed_path, decompressed_path)
"""
