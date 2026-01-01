#problem: you need to generate a dataset of simulated data
#solution: scikit-learn	offers	many	methods	for	creating	simulated	data.	Of	those,	three
#methods	are	particularly	useful:	make_regression,
#make_classification,	and	make_blobs.
#When	we	want	a	dataset	designed	to	be	used	with	linear	regression,
#make_regression	is	a	good	choice:
#	Load	library
from sklearn.datasets import make_regression
#generete features matrix, target vector,and the true coefficients 
features,target,coefficients = make_regression(n_samples=100,
                                               n_features=3,
                                               n_informative=3,
                                               n_targets=1,
                                               noise=0.0,
                                               coef=True,
                                               random_state=1)
#View feature matrix and target vector
print('Feature Matrix\n',features[:3])
print('Target Vector\n', target[:3])