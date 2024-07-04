from np_util import np_plus
import numpy as np

def test_np_plus():
	a = np.array([1,2,3])
	b = np.array([4,5,6])
	assert np.array_equal(np_plus(a, b), np.array([5,7,9]))

