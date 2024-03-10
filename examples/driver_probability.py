import numpy as np 
import matplotlib.pyplot as plt 
from goph420_lab01.integration import integrate_gauss

def main():
    lims = [1.5,4]
    I1,eps1,k1 =confidence_interval(0.5,1.5,lims)
    print(f"Probability of an event for an seismic event with a magnitude larger than 4.0: \n{0.5 - np.array(I1)}\n")

    #Probability Approx Error
    plt.loglog(k1,eps1,label="k")
    plt.ylabel('Approx Relative Error ('+r'$\epsilon$'+'a)')
    plt.xlabel('N points')
    plt.title('Seismic Event With P(M > 4.0)')
    plt.legend()
    plt.savefig('figures/probality_convergence.png')
    plt.close('all')
    
    lims1 = [10.25,10.35]
    I2,eps2,k2 =confidence_interval(0.05,10.28,lims1)
    print(f"Probability for a measured distance L is between 10.25m and 10.35m: \n{0.5 - np.array(I2)}\n")

    #Probability Approx Error
    plt.loglog(k2,eps2,label="k")
    plt.ylabel('Approx Relative Error ('+r'$\epsilon$'+'a)')
    plt.xlabel('N points')
    plt.title('Probability for a measured distance L is between 10.25m and 10.35m')
    plt.legend()
    plt.savefig('figures/probality_convergence2.png')
    plt.close('all')

def confidence_interval(_σ,_μ,_lims):
    k = [1,2,3,4,5]
    #Callable Function for standard normal probality 
    std_density_function = lambda x:  np.exp(-.5*((x-_μ)/_σ)**2)/np.sqrt(2*np.pi)
    I = [] 
    eps = []
    I_l = 0.0
    for i in k:
        I_n = integrate_gauss(std_density_function,_lims,k[i-1])
        eps_a = np.abs((I_n - I_l)/I_n)
        I.append(I_n)
        eps.append(eps_a)
        I_l = I_n
    return(I,eps,k)
if __name__ == "__main__":
    main()
