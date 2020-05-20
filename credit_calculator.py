import math
import sys
if len(sys.argv)>5:
    print("Incorrect parameters.")     #that is if the length of the input argument is greater then the argument it will quit the program
else:
    type=None
    A=None
    P=None
    n=None
    i=None
    if '--type' not in ''.join(sys.argv):
        print("Incorrect parameters.")
        quit()
    else:
        for j in sys.argv:
            if '--type' in j:
                type=j.split('--type=')[1]
            if '--principal'in j:
                P=int(j.split('--principal=')[1])
            if '--periods' in j:
                n=int(j.split('--periods=')[1])
            if '--interest' in j:
                i=float(j.split('--interest=')[1])/(100*12)
            if '--payment' in j:
                A=int(j.split('--payment=')[1])
        componentlist=[A,P,n,i]
        for j in componentlist:
            if j==None:
                continue
            if j<0:
                print("Incorrect parameters.")      #conditions for the incorrect parameters.
                quit()

        
        if componentlist.count(None)>1 or componentlist.count(None)==0 or componentlist[-1]==None:
            print("Incorrect parameters.")    #condition for the incorrect parameters
            quit()

        else:
            thisis_None=-1
            for j in range(len(componentlist)):
                if componentlist[j] is None:
                    thisis_None=j
                    break
            if thisis_None==0:     #main logic applies from here.
                if type=='annuity':  
                    A=math.ceil(P * ((i * math.pow(1 + i, n)) / ((math.pow(1 + i, n) - 1))))
                    print("Your annuity payment =",str(A) + "!")
                    print("Overpayment =",A*n-P)
                elif type=='diff':
                    sum=0
                    for j in range(1,n+1):
                        Amonthi=math.ceil((P/n)+(i*(P-((P*(j-1))/n))))
                        print("Month "+str(j)+": paid out "+str(Amonthi))
                        sum+=Amonthi
                    print()
                    print("Overpayment =",sum-P)
                else:
                    print("Incorrect parameters.")
            elif thisis_None==1:
                if type=='annuity':
                    P=int(A // ((i * math.pow(1 + i, n)) / ((math.pow(1 + i, n) - 1))))
                    print("Your credit principal =",str(P) + "!")
                    print("Overpayment =",A*n-P)
                else:
                    print("Incorrect parameters.")
            else:
                if type=='annuity':
                    yrs = math.ceil(math.log(A / (A - (i * P)), (1 + i))) // 12
                    month = (math.ceil(math.log(A / (A - (i * P)), (1 + i)))) - 12 * yrs
                    n=yrs*12+month
                    if yrs != 0 and month != 0:
                        print("You need",yrs,"years and", month, "months to repay this credit!")
                    elif yrs == 0 and month != 0:
                        print("You need "+str(month)+" month to repay this credit!" if month == 1 else "You need "+str(month)+ " months to repay this credit!")
                    else:
                        print("You need "+str(yrs)+" year to repay this credit!" if yrs == 1 else "You need "+str(yrs)+" years to repay this credit!")
                    print("Overpayment =",A*n-P)
                else:
                    print("Incorrect parameters.")