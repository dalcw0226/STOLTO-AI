# dataload code

from sklearn.datasets import load_diabetes
diabetes = load_diabetes()


data = diabetes['data']  # input data
target = diabetes['target']  # target data
