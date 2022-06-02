import pytest
import load_images_neg as load
@pytest.mark.parametrize(
    "dire",
    [
        (""),
        ("/mnt/d/Development"),
        ("/mnt/c/Positives")
    ]
)
def test_create_pos_n_neg(dire):
    #self.assertEqual(True, False)  # add assertion here
    path = dire
    assert load.create_pos_n_neg(path) == None


