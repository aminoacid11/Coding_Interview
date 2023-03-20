import numpy as np
import math
import matplotlib.pyplot as plt 

def obj(x):
    return x**2 + 4*math.cos(x)

def grad(x):
    return 2*x - 4*math.sin(x)

def bisection(a0,b0):
    if a0>b0:
        print("a0 should be smaller than b0, please choose the initial values again.")
    else:
        maxiter=1000
        a=a0
        b=b0
        #x0=(a0+b0)/2

        a_all=[]
        b_all=[]
        x_all=[]

        for i in range(maxiter):
            #==============core code===================
            x=(a+b)/2
            #==========================================

            a_all.append(a)
            b_all.append(b)
            x_all.append(x)

            #==============core code===================
            if grad(x)==0:
                break

            if grad(x)>0:
                b=x

            if grad(x)<0:
                a=x
            #==========================================



            if i==maxiter-1:
                print("Warning!!! Maximum iteration number reached!")

            if abs(a-b)<10**(-10):
                print("Warning!!! Stop because a and b are too close! The initial interval may need to be reconsidered! x^* may not inside it.")
                break
        iteration=len(x_all)
        
        print("The minimizer obtained by the algorithm is: ",x_all[-1])
        print("The minimum value obtained by the algorithm is: ",obj(x_all[-1]))
        print("The algorithm took ",iteration," iterations to reach the stopping criteria.")
        
        plotdot=200
        xplot=np.linspace(a_all[0]-0.1*abs(b_all[0]-a_all[0]),b_all[0]+0.1*abs(b_all[0]-a_all[0]),plotdot)
        fplot=np.zeros(xplot.shape)
        for j in range(plotdot):
            fplot[j]=obj(xplot[j]) 
            
        fa_all=[]
        fb_all=[]
        fx_all=[]
        
        for j in range(iteration):
            fa_all.append(obj(a_all[j]))
            fb_all.append(obj(b_all[j]))
            fx_all.append(obj(x_all[j]))
            

        fig1=plt.figure(figsize=(8,8))
        ax1=fig1.add_subplot()
        ax1.plot(xplot,fplot,'k-',linewidth='3',label="Objective function")

        for ja in range(len(a_all)):
            if ja==0:         
                ax1.plot([a_all[ja],b_all[ja]],[min(fplot)+(max(fplot)-min(fplot))*(0.2+0.6*((len(a_all)-ja)/len(a_all))),min(fplot)+(max(fplot)-min(fplot))*(0.2+0.6*((len(a_all)-ja)/len(a_all)))],'--',color="gray",linewidth='2',alpha=1,label="Interval")
            else:
                ax1.plot([a_all[ja],b_all[ja]],[min(fplot)+(max(fplot)-min(fplot))*(0.2+0.6*((len(a_all)-ja)/len(a_all))),min(fplot)+(max(fplot)-min(fplot))*(0.2+0.6*((len(a_all)-ja)/len(a_all)))],'--',color="gray",linewidth='2',alpha=1)
            
            ax1.plot([a_all[ja],a_all[ja]],[-1000,1000],'o-',color="gray",linewidth='2',alpha=0.3)
            ax1.plot([b_all[ja],b_all[ja]],[-1000,1000],'o-',color="gray",linewidth='2',alpha=0.3)
           

        # Comment the line below to see a and b better
        ax1.plot(x_all,fx_all,color="r",marker='o',markersize=5,linewidth='1',label="Bisection Method")
        plt.ylim(min(fplot)-0.1*(max(fplot)-min(fplot)),max(fplot)+0.1*(max(fplot)-min(fplot)))
        plt.legend() 
        
        if iteration>0:
            fig2=plt.figure(figsize=(8,8))
            ax2=fig2.add_subplot()
            ax2.plot(np.linspace(0,iteration-1,iteration),fx_all,'ko-', linewidth='3')  
            plt.ylabel("Function value")
            plt.xlabel("Iteration")
            plt.show()
    
    #return 0
    
#=====================Change the parameters here======================

a0,b0=[1,2] 

bisection(a0,b0)
