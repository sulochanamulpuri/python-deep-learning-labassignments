def students():
    python=['vinay','snepi','mourya','karthik']
    webapplication=['vinay','snepi','santhosh']
    a=list(set(python).intersection(set(webapplication)))
    print('common students in both python and web application are %s'% a)
    b=list(set(python).union(set(webapplication)))
    c=list(set(b).difference(set(a)))
    print('the list of students who are not common in both the classes are %s' % c)
students()