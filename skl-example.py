from sklearn import naive_bayes
# features: no. of hours before overheating, max op volts, min op volts
features = [
	[10, 230, 200], #ok
	[9, 220, 120], #ok
	[12, 200, 195], #problem
	[10, 240, 200], #ok
	[11, 205, 190], #problem
	[12, 210, 200], #problem
	[8, 230, 205], #ok
	[11, 210, 200], #problem
	[9, 215, 150], #problem
	[10, 200, 185] #problem
	]
labels = [0, 0, 1, 0, 1, 1, 0, 1, 1, 1]
classifier = naive_bayes.GaussianNB()
classifier = classifier.fit(features, labels)

hours, maxv, minv = list(map(int, input().split()))
output = classifier.predict([[hours, maxv, minv]])
if output == 0:
	print('OK')
else:
	print('Faulty')
