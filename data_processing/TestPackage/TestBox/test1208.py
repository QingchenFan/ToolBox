
from sklearn.cross_decomposition import PLSCanonical

X = [[0., 0., 1.], [1.,0.,0.], [2.,2.,2.], [2.,5.,4.]]
Y = [[0.1, -0.2], [0.9, 1.1], [6.2, 5.9], [11.9, 12.3]]

print(X)
print(Y)

plsca = PLSCanonical(n_components=2)
plsca.fit(X, Y)
X_c, Y_c = plsca.transform(X, Y)

print(X_c)
print(Y_c)