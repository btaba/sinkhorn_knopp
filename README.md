sinkhorn_knopp
--------

[![Build Status](https://travis-ci.org/btaba/sinkhorn_knopp.svg?branch=master)](https://travis-ci.org/btaba/sinkhorn_knopp)


To convert non-negative square matrices with total support into doubly stochastic matrices. 

```python
    >> import numpy as np
    >> from sinkhorn_knopp import sinkhorn_knopp as skp
    >> sk = skp.SinkhornKnopp()
    >> P = [[.011, .15], [1.71, .1]]
    >> P_ds = sk.fit(P)
    >> print P_ds
        [[ 0.06102561  0.93897439]
        [ 0.93809928  0.06190072]]
    >> print np.sum(P_ds, axis=0)
        [ 0.99912489  1.00087511]
    >> print np.sum(P_ds, axis=1)
        [ 1.,  1.]
```

See http://msp.org/pjm/1967/21-2/pjm-v21-n2-p14-s.pdf for reference.

## Install

Either:

```sh
pip install sinkhorn_knopp
```

or

```sh
git clone https://github.com/btaba/sinkhorn_knopp
cd sinkhorn_knopp
python setup.py install
```

## Uninstall

Depending on the above, either:

```sh
pip uninstall sinkhorn_knopp
```

or 

```sh
cd sinkhorn_knopp
python setup.py install --record files.txt
cat files.txt | xargs rm -rf
```