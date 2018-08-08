import sys
foo=[1,2,3,4,5,'rr']
fo=[]
for i in foo:
    try:
        x=1/i
        print(x)
    except:                                    #exept  (ZeroDivisionError, TypeError): //// finally: print('Hi')
        print('ERROR',sys.exc_info()[1]) #printinf specific info of the error
