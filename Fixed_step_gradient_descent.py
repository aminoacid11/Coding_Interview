import numpy as np
import matplotlib.pyplot as plt 

def quad(x,Q,a,b):
    # For n-d case, define x as: x=np.array([x_1,x_2,...,x_n]). For 1-d case, x is a real number.
    # For n-d case, define Q as: Q=np.array([[Q_11,Q_12,...,Q_1n],[Q_21,Q_22,...,Q_2n],...,[Q_n1,Q_n2,...,Q_nn]]). For 1-d case, Q is a real number.
    # For n-d case, define a as: a=np.array([a_1,a_2,...,a_n]). For 1-d case, a is a real number.
    # b is a real number.
    return 1.5*(x**2 + Q**2) + a*(x*Q) - (x + Q) + b

def grad_quad(x,Q,a):
    return 3*(x) + (a*Q) - 1

def fixedstep_1d(x_0,Q,a,b,alpha):
    # We don't need b in steepest descent, here we take b as input only for visualization.
    # x_0 is the initial.
    # alpha is the stepsize.
    
    maxiter=1000

    xold=x_0
    fold=quad(xold,Q,a,b)
    
    x_all=[xold]
    f_all=[fold]
    
    for i in range(maxiter):
        #==============core code===================
        g=grad_quad(xold,Q,a)
        
        if np.linalg.norm(g)<10**(-5):
            break
        
        xnew=xold-alpha*g
        #==========================================
        fnew=quad(xnew,Q,a,b)
        
        x_all.append(xnew)
        f_all.append(fnew)

        xold=xnew
        
        if i==maxiter-1:
            print("Warning!!! Maximum iteration number reached!")
            
        if abs(fnew)>=10**4:
            print("Warning!!! Function value too large, maybe diverge!!!")
            break
    
    iteration=len(x_all)-1
    
    print("The minimizer obtained by the algorithm is: ",x_all[-1])
    print("The minimum value obtained by the algorithm is: ",f_all[-1])
    print("The algorithm took ",iteration," iterations to reach the stopping criteria.")
    
    plotdot=200
    xplot=np.linspace(x_all[-1]-1.1*max(0.01,abs(x_0-x_all[-1])),x_all[-1]+1.1*max(0.01,abs(x_0-x_all[-1])),plotdot)
    fplot=np.zeros(xplot.shape)
    for j in range(plotdot):
        fplot[j]=quad(xplot[j],Q,a,b) 
    
    fig1=plt.figure(figsize=(16,8))
    ax1=fig1.add_subplot(121)
    ax1.plot(xplot,fplot,'k-', linewidth='3',label="Objective function")  
    ax1.plot(x_all,f_all,'ro-',linewidth='1',label="Steepest_Descent")
    plt.legend()
    
    if iteration>0:    
        try:
            xstar=-a/Q
            fstar=quad(xstar,Q,a,b)
            #fig2=plt.figure(figsize=(8,8))
            ax2=fig1.add_subplot(122)
            ax2.semilogy(np.linspace(0,iteration,iteration+1),abs(np.array(f_all)-fstar),'ko-', linewidth='3')  
            plt.ylabel("||f-f*||")
            plt.xlabel("Iteration")
            plt.show()
        except:
            print("Q is inversible, in the second picture we plot function value w.r.t. iteration.")
            #fig2=plt.figure(figsize=(8,8))
            ax2=fig1.add_subplot(122)
            ax2.plot(np.linspace(0,iteration,iteration+1),np.array(f_all),'ko-', linewidth='3')  
            plt.ylabel("Function value")
            plt.xlabel("Iteration")
            plt.show()

    
    #return 0

    
#=====================Change the parameters here======================
x_0=1
Q=1
a=3
b=1
alpha=0.1
fixedstep_1d(x_0,Q,a,b,alpha)
    