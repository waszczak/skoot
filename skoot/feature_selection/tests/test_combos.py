# -*- coding: utf-8 -*-
#
# Author: Taylor Smith <taylor.smith@alkaline-ml.com>

from __future__ import print_function

import numpy as np
import pandas as pd

from skoot.decomposition import QRDecomposition
from skoot.feature_selection import LinearCombinationFilter
from skoot.feature_selection.combos import _enum_lc
from skoot.utils.testing import (assert_raises, assert_transformer_asdf,
                                 assert_persistable)

from numpy.testing import assert_array_equal
from sklearn.datasets import load_iris

# Def data for testing
iris = load_iris()
X = pd.DataFrame.from_records(data=iris.data, columns=iris.feature_names)
y = np.array(
    [[0.41144380, 1, 2],
     [0.20002043, 1, 2],
     [1.77615427, 1, 2],
     [-0.88393494, 1, 2],
     [1.03053577, 1, 2],
     [0.10348028, 1, 2],
     [-2.63301012, 1, 2],
     [-0.09411449, 1, 2],
     [-0.37090572, 1, 2],
     [3.67912713, 1, 2],
     [-1.11889106, 1, 2],
     [-0.16339222, 1, 2],
     [-1.68642994, 1, 2],
     [0.01475935, 1, 2],
     [-0.71178462, 1, 2],
     [-0.07375506, 1, 2],
     [1.67680864, 1, 2],
     [1.08437155, 1, 2],
     [0.42135106, 1, 2],
     [0.23891404, 1, 2],
     [-0.67025244, 1, 2],
     [-0.74780315, 1, 2],
     [1.53795249, 1, 2],
     [2.24940846, 1, 2],
     [-1.33077619, 1, 2],
     [-1.23597935, 1, 2],
     [-1.10603714, 1, 2],
     [0.06115450, 1, 2],
     [2.33540909, 1, 2],
     [-0.20694138, 1, 2],
     [1.34077119, 1, 2],
     [1.19347871, 1, 2],
     [0.23480672, 1, 2],
     [-1.48948507, 1, 2],
     [1.00529241, 1, 2],
     [1.72366825, 1, 2],
     [4.14722011, 1, 2],
     [-0.66620106, 1, 2],
     [1.45597498, 1, 2],
     [-0.39631565, 1, 2],
     [0.80971318, 1, 2],
     [0.71547389, 1, 2],
     [-0.17342195, 1, 2],
     [-1.18399696, 1, 2],
     [1.77178761, 1, 2],
     [-0.94494203, 1, 2],
     [-1.47486102, 1, 2],
     [0.35748476, 1, 2],
     [-1.29096329, 1, 2],
     [0.61611613, 1, 2],
     [0.92048145, 1, 2],
     [0.56870638, 1, 2],
     [0.06455932, 1, 2],
     [0.20987525, 1, 2],
     [0.60659611, 1, 2],
     [0.43715853, 1, 2],
     [-0.06136566, 1, 2],
     [-1.75842912, 1, 2],
     [-1.03648110, 1, 2],
     [-2.72359130, 1, 2],
     [1.80935039, 1, 2],
     [1.27240976, 1, 2],
     [-2.74477429, 1, 2],
     [0.34654907, 1, 2],
     [-1.90913461, 1, 2],
     [-3.42357727, 1, 2],
     [-1.28010016, 1, 2],
     [3.17908952, 1, 2],
     [-1.54936824, 1, 2],
     [-1.37700148, 1, 2],
     [0.41881648, 1, 2],
     [0.22241198, 1, 2],
     [-0.78960214, 1, 2],
     [0.28105782, 1, 2],
     [2.58817288, 1, 2],
     [0.88948762, 1, 2],
     [1.25544532, 1, 2],
     [-0.50838470, 1, 2],
     [1.13062450, 1, 2],
     [2.41422771, 1, 2],
     [-0.86262900, 1, 2],
     [-2.16937438, 1, 2],
     [-0.57198596, 1, 2],
     [-0.07023331, 1, 2],
     [2.34332545, 1, 2],
     [-0.71221171, 1, 2],
     [-0.18585408, 1, 2],
     [-2.81586156, 1, 2],
     [-0.86356504, 1, 2],
     [-0.01727535, 1, 2],
     [-3.15966711, 1, 2],
     [-0.84387501, 1, 2],
     [-1.73471525, 1, 2],
     [2.74981014, 1, 2],
     [0.28114847, 1, 2],
     [-1.66076523, 1, 2],
     [-0.62953126, 1, 2],
     [-1.90627065, 1, 2],
     [-0.38711584, 1, 2],
     [0.84237942, 1, 2],
     [0.35066088, 1, 2],
     [-0.47789289, 1, 2],
     [-1.72405119, 1, 2],
     [0.78935913, 1, 2],
     [3.03339661, 1, 2],
     [-2.68912845, 1, 2],
     [0.22600963, 1, 2],
     [3.72403170, 1, 2],
     [0.25115682, 1, 2],
     [2.51450226, 1, 2],
     [-2.52882830, 1, 2],
     [-1.60614569, 1, 2],
     [-0.74095083, 1, 2],
     [0.78927670, 1, 2],
     [2.35876839, 1, 2],
     [0.84019398, 1, 2],
     [-2.49124992, 1, 2],
     [-1.36854708, 1, 2],
     [0.59393289, 1, 2],
     [-0.82345534, 1, 2],
     [1.16502458, 1, 2],
     [-0.28916165, 1, 2],
     [0.56981198, 1, 2],
     [1.26863563, 1, 2],
     [-2.88717380, 1, 2],
     [0.01525054, 1, 2],
     [-1.62951432, 1, 2],
     [0.45031432, 1, 2],
     [0.75238069, 1, 2],
     [0.73113016, 1, 2],
     [1.52144045, 1, 2],
     [0.54123604, 1, 2],
     [-3.18827503, 1, 2],
     [-0.31185831, 1, 2],
     [0.77786948, 1, 2],
     [0.96769255, 1, 2],
     [2.01435274, 1, 2],
     [-0.86995262, 1, 2],
     [1.63125106, 1, 2],
     [-0.49056004, 1, 2],
     [-0.17913921, 1, 2],
     [1.55363112, 1, 2],
     [-1.83564770, 1, 2],
     [-1.22079526, 1, 2],
     [-1.69420452, 1, 2],
     [0.54327665, 1, 2],
     [-2.07883607, 1, 2],
     [0.52608135, 1, 2],
     [-0.89157428, 1, 2],
     [-1.07971739, 1, 2]])

Z = pd.DataFrame.from_records(data=y, columns=['A', 'B', 'C'])


def test_linear_combos():
    lcf = LinearCombinationFilter().fit(Z)
    assert lcf.drop_ == ['C'], lcf.drop_

    z = lcf.transform(Z)
    assert_array_equal(z.columns.values, ['A', 'B'])
    assert (z.B == 1).all()

    # test on no linear combos
    lcf = LinearCombinationFilter(cols=['A', 'B']).fit(Z)
    assert not lcf.drop_
    assert Z.equals(lcf.transform(Z))

    # test too few features
    assert_raises(ValueError, LinearCombinationFilter(cols=['A']).fit, Z)


def test_enum_lc():
    z = np.array([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ])

    a, b = _enum_lc(QRDecomposition(z))[0], np.array([2, 0, 1])
    assert (a == b).all(), 'should be [2,0,1] but got %s' % a
    assert not _enum_lc(QRDecomposition(iris.data))

    assert_array_equal(_enum_lc(QRDecomposition(y))[0], np.array([2, 1]))


def test_combos_asdf():
    assert_transformer_asdf(LinearCombinationFilter(), X)


def test_combos_persistable():
    assert_persistable(LinearCombinationFilter(), location="loc.pkl", X=X)