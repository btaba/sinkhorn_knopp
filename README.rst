Sinkhorn_Knopp
--------

To convert non-negative square matrices with total support into doubly stochastic matrices. 

    >>> from sinkhorn_knopp import SinkhornKnopp
    >>> sk = SinkhornKnopp()
    >>> P = np.array([[.011, .15], [1.71, .1]])
    >>> sk.fit(P)

See http://msp.org/pjm/1967/21-2/pjm-v21-n2-p14-s.pdf for reference.