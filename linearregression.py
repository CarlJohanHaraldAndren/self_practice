def trivial_regression(x1,y1,x2,y2,x):
    y=((y2-y1)/(x2-x1)*x)+(y1*x2-y2*x1)/(x2-x1)
    return y

trivial_regression(x1, y1, x2, y2, x)