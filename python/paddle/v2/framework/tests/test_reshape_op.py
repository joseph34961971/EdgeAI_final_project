import unittest
import numpy as np
from gradient_checker import GradientChecker, Operator
from op_test_util import OpTestMeta


class TestReshapeOp(unittest.TestCase):
    __metaclass__ = OpTestMeta

    def setUp(self):
        self.type = "reshape"
        self.inputs = {'X': np.random.random((37, 51)).astype("float32"), }
        self.attrs = {'shape': [51, 37]}
        self.outputs = {'Out': self.inputs['X'].reshape(self.attrs['shape'])}


class ReshapeGradOpTest(GradientChecker):
    def test_normal(self):
        op = Operator("reshape", X='X', Out='Out', shape=[5, 40])
        inputs = {"X": np.random.random((10, 20)).astype("float32")}
        self.check_grad(op, inputs, set("X"), "Out")


if __name__ == '__main__':
    unittest.main()
