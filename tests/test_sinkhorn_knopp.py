import unittest
import warnings
import numpy as np

from sinkhorn_knopp.sinkhorn_knopp import SinkhornKnopp


class TestSinkhornKnopp(unittest.TestCase):
    def test_init(self):
        sk = SinkhornKnopp()
        self.assertIsNotNone(sk)

        self.assertEqual(sk._max_iter, 1000)
        self.assertEqual(sk._epsilon, 1e-3)

        self.assertRaises(AssertionError, SinkhornKnopp, max_iter='1')
        self.assertRaises(AssertionError, SinkhornKnopp, epsilon='1')
        self.assertRaises(AssertionError, SinkhornKnopp, max_iter=-1)
        self.assertRaises(AssertionError, SinkhornKnopp, epsilon=1)
        self.assertRaises(AssertionError, SinkhornKnopp, epsilon=0)

    def test_fit_inputs(self):
        sk = SinkhornKnopp()
        self.assertRaises(AssertionError, sk.fit, 1)
        self.assertRaises(AssertionError, sk.fit, [[1, 2], [1, 2], [1, 2]])
        self.assertRaises(AssertionError, sk.fit, [[1, 2], [1, -1]])

    def test_stopping_condition(self):
        sk = SinkhornKnopp(max_iter=5)
        self.assertIsNone(sk._stopping_condition)

        P = np.eye(2)
        sk.fit(P)
        self.assertEqual(sk._stopping_condition, 'epsilon')

        P = np.array([[.011, .15], [1.71, .1]])
        sk.fit(P)
        self.assertEqual(sk._stopping_condition, 'max_iter')
        self.assertEqual(sk._iterations, 5)

    def test_support_warning(self):
        """
            A non-negative square is said to have total
            support if A =/= 0 and if every positive element of A
            lies on a positive diagonal. A diagonal of a matrix
            is defined, for any permutation of sigma = {1,...,N},
            as a[1,sigma(1)], ..., a[N,sigma(N)], where a[i, j]
            is an element of A at the ith row and jth column.
        """
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            sk = SinkhornKnopp()
            P = np.array([[0, 0], [1, 0]])
            sk.fit(P)
            self.assertEqual(w[0].category, UserWarning)

    def test_sinkhorn_knopp(self):
        # Epsilon = 1e-3
        sk = SinkhornKnopp()
        P = np.asarray([[1, 2], [3, 4]])
        Pt = sk.fit(P)
        self.assertFalse(np.all(P == Pt))

        # Make sure we stopped because of epsilon
        self.assertEqual(sk._stopping_condition, 'epsilon')
        col_sum = np.sum(Pt, axis=1)
        row_sum = np.sum(Pt, axis=0)

        self.assertTrue(np.all(1 + sk._epsilon > row_sum))
        self.assertTrue(np.all(1 - sk._epsilon < row_sum))
        self.assertTrue(np.all(1 + sk._epsilon > col_sum))
        self.assertTrue(np.all(1 - sk._epsilon < col_sum))

        # Epsilon = 1e-8
        sk = SinkhornKnopp(epsilon=1e-8)
        P = np.asarray([[1.4, .2, 4], [3, 4, .7], [.4, 6, 1]])
        Pt = sk.fit(P)
        self.assertFalse(np.all(P == Pt))

        # Make sure we stopped because of epsilon
        self.assertEqual(sk._stopping_condition, 'epsilon')

        col_sum = np.sum(Pt, axis=1)
        row_sum = np.sum(Pt, axis=0)

        self.assertTrue(np.all(1 + sk._epsilon > row_sum))
        self.assertTrue(np.all(1 - sk._epsilon < row_sum))
        self.assertTrue(np.all(1 + sk._epsilon > col_sum))
        self.assertTrue(np.all(1 - sk._epsilon < col_sum))

    def test_diagonal_matrices(self):
        sk = SinkhornKnopp()
        P = np.eye(2)
        Pt = sk.fit(P)
        self.assertTrue(np.all(P == Pt))
        self.assertEqual(sk._D1.ndim, 2)
        self.assertEqual(sk._D2.ndim, 2)
        self.assertTrue(np.all(sk._D1 == P))
        self.assertTrue(np.all(sk._D2 == P))
