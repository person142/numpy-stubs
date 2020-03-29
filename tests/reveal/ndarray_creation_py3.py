import numpy as np

nd: 'np.ndarray[np.Int64]' = np.array([[1, 2], [3, 4]])
reveal_type(nd)  # E: numpy.ndarray[numpy.Int64]
