import os
import tempfile
import pytest

from project import SmartFileSearch

def create_temp_file(content, suffix=".txt", binary=False):
    mode = "wb" if binary else "w"
    fd, path = tempfile.mkstemp(suffix=suffix)
    with os.fdopen(fd, mode) as f:
        if binary:
            f.write(content)
        else:
            f.write(content)
    return path



def test_initialization():
    search = SmartFileSearch(".", "test")
    assert search.target_word == "test"
    assert search.root_dir
    assert search.max_threads > 0
    assert search.pattern is not None



def test_binary_file_detection():
    binary_path = create_temp_file(b"\x00\x01\x02\x03", binary=True)
    text_path = create_temp_file("hello world")

    search = SmartFileSearch(".", "test")

    assert search.is_likely_binary(binary_path) is True
    assert search.is_likely_binary(text_path) is False

    os.remove(binary_path)
    os.remove(text_path)



def test_search_single_file_finds_matches():
    content = """hello world
this is a test
another test line
no match here
"""
    path = create_temp_file(content)

    search = SmartFileSearch(".", "test", case_sensitive=False)
    matches = search.search_single_file(path)

    assert len(matches) == 2
    assert matches[0][0] == 2
    assert "test" in matches[0][1].lower()

    os.remove(path)


def test_search_single_file_case_sensitive():
    content = """Test
test
TEST
"""
    path = create_temp_file(content)

    search = SmartFileSearch(".", "test", case_sensitive=True)
    matches = search.search_single_file(path)

    assert len(matches) == 1
    assert matches[0][0] == 2

    os.remove(path)


def test_search_single_file_no_matches():
    content = "hello world\nnothing here\n"
    path = create_temp_file(content)

    search = SmartFileSearch(".", "test")
    matches = search.search_single_file(path)

    assert matches == []

    os.remove(path)



def test_long_line_truncation():
    long_line = "a" * 300 + " test"
    path = create_temp_file(long_line)

    search = SmartFileSearch(".", "test")
    matches = search.search_single_file(path)

    assert len(matches) == 1
    assert len(matches[0][1]) <= 200

    os.remove(path)


def test_extension_filtering():
    search = SmartFileSearch(".", "test", extensions={".txt"})
    assert ".txt" in search.extensions
    assert ".exe" not in search.extensions
