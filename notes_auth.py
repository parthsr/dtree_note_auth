import StringIO
import numpy as np
from sklearn import tree
import random
import pydotplus 
fname= "data.txt"  
X=[] 
Y=[]
Z=[]
with open(fname,'r') as f:
	contents = f.readlines()
	Z+= contents
random.shuffle(Z)

for i in Z:
	my_list = i.strip("\n").strip("\r").split(",")
	X.append(my_list[:4])
	Y.append(int(my_list[-1:][0]))


X = [[float(column) for column in row] for row in X]
	
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X[:1000], Y[:1000])
scores = clf.score(X[1000:],Y[1000:])
print "Accuracy: %f " % scores

dot_data = StringIO.StringIO()
tree.export_graphviz(clf, out_file=dot_data)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("TREE.pdf")
print "The Decision Tree was saved!"





   