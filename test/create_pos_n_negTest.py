import pytest

from DeteccionArmasSTR import load_images_neg as lin
def test_something():
    #self.assertEqual(True, False)  # add assertion here
    assert(lin.create_pos_n_neg(), None)

