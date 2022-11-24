from GACourse import *

###
### Hill Climbing
###

def Perturbation(x,p=.01):
    """
    :param x: individual
    :param p: probability of perturbation
    :return: new individual
    """

    nx = []
    i = 0
    while i<len(x):
        if (random.random()<p):
            nx.append(1-int(x[i]))
        else:
            nx.append(int(x[i]))
        i = i + 1

    return tuple(nx)

def main():

    # number of evaluations
    number_of_evaluations = 100000

    # number of variables
    arity = 10

    # function to be maximixed
    f = bf1

    # current evaluation
    e = 0
    x = RandomBinaryTuple(arity)
    v = f(x)
    print(v)
    best = v[0][0]
    while e<number_of_evaluations:
        x1 = Perturbation(x,0.1)
        v1 = f(x)
        best = v1[0][0]
        print (str(e)+"\t"+str(x)+"\t"+best)
        if (y1>best):
            best = y1
            x = x1
        e = e + 1

    print("BEST = "+str(x))


if __name__ == "__main__":
    main()