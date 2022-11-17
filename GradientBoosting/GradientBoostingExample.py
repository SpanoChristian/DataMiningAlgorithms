import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import tree

def GenerateData():
    X = np.arange(0,50)
    # just random uniform distributions in differnt range

    y1 = np.random.uniform(10,15,10)
    y2 = np.random.uniform(20,25,10)
    y3 = np.random.uniform(0,5,10)
    y4 = np.random.uniform(30,32,10)
    y5 = np.random.uniform(13,17,10)

    y = np.concatenate((y1,y2,y3,y4,y5))
    y = y[:,None]

    X = X.reshape(-1, 1)
    y = y.reshape(-1, 1)
    return X, y

def PlotData(X,y,yp=[],label='',title='',fn=None):
    plt.scatter(X,y)
    plt.xlim([-1,51])
    plt.ylim([-1,35])
    plt.xlabel('x')
    plt.ylabel('y')
    if (title!=''):
        plt.title(title)
    if (fn!=None):
        plt.savefig(fn)
    #
    # if (yp!=[]):
    #     plt.plot(X,yp,color = 'red')
    #
    plt.show()

def PlotModel(X,y,yp,title='',fn=None):
    plt.scatter(X,y, color = 'blue')
    plt.plot(X,yp,color = 'red')
    plt.xlim([-1,51])
    plt.ylim([-1,35])
    plt.xlabel('x')
    plt.ylabel('y')
    if (title!=''):
        plt.title(title)
    if (fn!=None):
        plt.savefig(fn)
    plt.show()

def PlotResidual(X,y,label='',title='',fn=None):
    plt.scatter(X,y,color = 'green')
    plt.xlim([-1,51])
    plt.ylim([-25,25])
    plt.xlabel('x')
    plt.ylabel('y')
    if (title!=''):
        plt.title(title)
    if (fn!=None):
        plt.savefig(fn)
    plt.show()

def PlotLocalModel(X,y,yp,title='',fn=None):
    plt.scatter(X,y, color = 'greep')
    plt.plot(X,yp,color = 'red', ls='--',label='Partial Model')
    plt.xlim([-1,51])
    plt.ylim([-25,25])
    plt.xlabel('x')
    plt.ylabel('y')
    if (fn!=None):
        plt.savefig(fn)
    if (title!=''):
        plt.title(title)
    plt.show()

# set the font for plotting
# 'family' : 'normal',
font = {'size': 14}
plt.rc('font', **font)
plt.figure(figsize=(8,6))

# generate the data
X, y = GenerateData()

PlotData(X,y,title='Original Data', fn='GradientBoosting-000-data.png')

# initially the prediction is filled with zeros
prediction = np.zeros((50,1))

# initially the model is just the mean
yp = np.ones((50,1))*y.mean()
PlotModel(X,y,yp=yp,title='Iteration #0 - Mean',fn='GradientBoosting-001-model.png')

# update the prediction
prediction = np.add(prediction, yp)

# update the residual
y_residual = np.subtract(y, prediction)
PlotResidual(X,y_residual,title='Iteration #0 - Residual',fn='GradientBoosting-001-residual.png')

# second round let's compute a model for the residual
clf = tree.DecisionTreeRegressor(max_depth=1)
clf = clf.fit(X,y_residual)
yp = clf.predict(X)

# update the prediction
prediction = np.add(prediction, yp.reshape(-1,1))
PlotModel(X,y,yp=prediction,title='Iteration #2 - Model',fn='GradientBoosting-03-model.png')

y_residual = np.subtract(y, prediction)

PlotResidual(X,y_residual,title='Iteration #1 - Residual',fn='GradientBoosting-04-residual.png')



###
### Gradient Boosting Full Process
###

# arrays collecting the models and the residuals
model = []
residual = []

### Step 0 - use the mean as model
# initially the prediction is filled with zeros
prediction = np.zeros((50,1))

# initially the model is just the mean
yp = np.ones((50,1))*y.mean()
PlotModel(X,y,yp=yp,title='Iteration #1 - Mean',fn='GradientBoosting-001-model.png')

# update the prediction
prediction = np.add(prediction, yp)

# update the residual
y_residual = np.subtract(y, prediction)
PlotResidual(X,y_residual,title='Iteration #1 - Residual',fn='GradientBoosting-001-residual.png')

# model.append(prediction)
# residual.append(y_residual)

no_boosting_runs = 30

for i in range(no_boosting_runs):
    clf = tree.DecisionTreeRegressor(max_depth=1)
    clf = clf.fit(X, y_residual)
    yp = clf.predict(X)

    # update the prediction
    prediction = np.add(prediction, yp.reshape(-1, 1))
    PlotModel(X, y, yp=prediction, title=('Iteration #%d - Model'%(i+2)), fn=('GradientBoosting-%03d-model.png'%(i+2)))

    y_residual = np.subtract(y, prediction)

    PlotResidual(X, y_residual, title=('Iteration #%d - Residual'%(i+2)), fn='GradientBoosting-%03d-residual.png'%(i+2))

    # model.append(prediction)
    # residual.append(y_residual)
