import math
import numpy as np
import matplotlib.pyplot as plt 

def obj(x):
    return x**2 + 4*math.cos(x)

def grad(x):
    return 2*x - 4*math.sin(x)

def grad2(x):
    return 2 - 4*math.cos(x)

def newton(x0):
    maxiter=1000
    xold=x0
    fold=obj(xold)
    
    x_all=[xold]
    f_all=[fold]
    
    fig1=plt.figure(figsize=(8,8))
    ax1=fig1.add_subplot()

    for i in range(maxiter):
        
        #========================
        g=grad(xold)
        g2=grad2(xold)
        
        
        if abs(g)<10**(-5):
            break
        
        d=g/g2
        
        
        if abs(g/g2)>10**4:
            print("Warning!!! Increment too large, maybe diverge!!!")  
            break
        
        xnew=xold-d    
        fnew=obj(xnew) 
        #========================
        
        
        ###########################(*)Uncomment these lines to see the approximated quadratic functions###############
        qua_plot=range(maxiter) # qua_plot is the iteration you want to plot the corresponding quadratic
        #qua_plot=[0]
        
        if i in qua_plot:
            a=g2/2
            b=g-g2*xold
            c=obj(xold)-a*xold**2-b*xold

            xuse=np.linspace(xnew-5*max(abs(xnew-xold),1),xnew+5*max(abs(xnew-xold),1),1000)
            if i==qua_plot[0]:
                ax1.plot(xuse,a*xuse**2+b*xuse+c,'-',color="gray", linewidth='2',label="Quadratic function (approximate)") 
            else:
                ax1.plot(xuse,a*xuse**2+b*xuse+c,'-',color="gray", linewidth='2') 
            ax1.plot([xnew,xnew],[-1000,+1000],'--',color="gray", linewidth='2')
            
        ###########################################################################################################
        
        xold=xnew
        
        x_all.append(xnew)
        f_all.append(fnew)
        
        

        
        
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
    xplot=np.linspace(min(x_all)-0.1*abs(max(x_all)-min(x_all)),max(x_all)+0.1*abs(max(x_all)-min(x_all)),plotdot)
    fplot=np.zeros(xplot.shape)
    for j in range(plotdot):
        fplot[j]=obj(xplot[j]) 


    ax1.plot(xplot,fplot,'k-', linewidth='3',label="Objective function")  
    ax1.plot(x_all,f_all,'ro-',linewidth='1',label="Newton's Method")
    plt.xlim(min(x_all)-0.1*abs(max(x_all)-min(x_all)),max(x_all)+0.1*abs(max(x_all)-min(x_all)))
    plt.ylim(min(f_all)-0.1*abs(max(f_all)-min(f_all)),max(f_all)+0.1*abs(max(f_all)-min(f_all)))
    plt.legend()

    fig2=plt.figure(figsize=(8,8))
    ax2=fig2.add_subplot()
    ax2.plot(np.linspace(0,iteration,iteration+1),np.array(f_all),'ko-', linewidth='3')  
    plt.ylabel("Function value")
    plt.xlabel("Iteration")
    plt.show()

#=====================Change the parameters here======================
# Try different x0
x0=1
#x0=-1
#x0=-10


newton(x0)
     
                
        