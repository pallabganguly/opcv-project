import numpy as np
import pandas as pd
from sklearn import neighbors, preprocessing, cross_validation
from matplotlib import pyplot as plt

df = pd.read_csv('breast-cancer-wisconsin.data')

df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['class'],  1))
y = np.array(df['class'])

ratios = [0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.450, 0.475, 0.5]
accuracy = []
for r in ratios:
	X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
	clf = neighbors.KNeighborsClassifier()
	clf.fit(X_train, y_train)
	acc = clf.score(X_test, y_test)
	accuracy.append(acc)

plt.plot(ratios, accuracy,)
plt.xlabel('Ratio test/training')
plt.ylabel('Classification accuracy')
plt.show()