import numpy as np

reveal_type(np.array([[1, 2], [3, 4]], dtype=np.dtype(np.int64)))  # E: numpy.ndarray[numpy.Int64*]
reveal_type(np.zeros((3, 3)))  # E: numpy.ndarray[numpy.Float64]
reveal_type(np.zeros((3, 3), dtype=np.dtype(np.int64)))  # E: numpy.ndarray[numpy.Int64*]
reveal_type(np.zeros((3, 3), order='F'))  # E: numpy.ndarray[numpy.Float64]
reveal_type(np.ones((3, 3)))  # E: numpy.ndarray[numpy.Float64]
reveal_type(np.ones((3, 3), dtype=np.dtype(np.int64)))  # E: numpy.ndarray[numpy.Int64*]
reveal_type(np.ones((3, 3), order='F'))  # E: numpy.ndarray[numpy.Float64]
