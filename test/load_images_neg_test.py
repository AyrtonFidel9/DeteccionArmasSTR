import pytest
from src.load_images_neg import find_uglies

@pytest.mark.parametrize(
    ["dir", "result"],
    [
        (r'/Users/edwinmanzano/Documents/Dev/Opencv/opencv-haar-classifier-training/negative_images', "[Errno 2] No such file or directory: 'uglies'"),
        (None, "Path not found")
    ]
)
def test_find_uglies(dir, result):
    assert find_uglies(dir) == result
