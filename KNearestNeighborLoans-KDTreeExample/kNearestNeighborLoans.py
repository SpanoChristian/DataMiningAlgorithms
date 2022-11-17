import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets, neighbors
from sklearn import model_selection
from sklearn.model_selection import StratifiedKFold
import time

loans = pd.read_csv('LoansNumerical.csv')
target = 'safe_loans'
features = loans.columns[loans.columns!=target]

x = loans[features]
y = loans[target]

k = 15
knn = neighbors.KNeighborsClassifier(n_neighbors=k, algorithm='brute')
knn_kdtree = neighbors.KNeighborsClassifier(n_neighbors=k, algorithm='kd_tree')

#%%time
start_kdtree = time.process_time()
knn_eval_kd = model_selection.cross_val_score(knn_kdtree, x, y, cv=StratifiedKFold(n_splits=10,shuffle=True,random_state=1234))
end_kdtree = time.process_time()

time_taken_kdtree = end_kdtree-start_kdtree
print("%d-nearest-neighbor\tt=%.3f\tAccuracy=%.3f\tStd=%.3f"%(k,time_taken_kdtree,np.average(knn_eval_kd),np.std(knn_eval_kd)))

start_vanilla = time.process_time()
knn_eval = model_selection.cross_val_score(knn, x, y, cv=StratifiedKFold(n_splits=10,shuffle=True,random_state=1234))
end_vanilla = time.process_time()

time_taken_vanilla = end_vanilla-start_vanilla
print("%d-nearest-neighbor\tt=%.3f\tAccuracy=%.3f\tStd=%.3f"%(k,time_taken_vanilla,np.average(knn_eval),np.std(knn_eval)))

