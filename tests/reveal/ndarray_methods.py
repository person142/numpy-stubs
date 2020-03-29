import numpy as np

nd = np.array([[1, 2], [3, 4]], dtype=np.dtype(np.int64))
reveal_type(nd.dtype)  # E: numpy.Int64
