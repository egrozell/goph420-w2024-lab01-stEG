import numpy as np 
import matplotlib.pyplot as plt 
from goph420_lab01.integration import integrate_newton

def main():
    
    t,v = np.loadtxt(fname="s_wave_data.txt",unpack=True)
    
    #determine upper annd lower bounds for t with last point being v 0.5% of initial v
    v_start = np.max(np.abs(v))
    i_start = np.argmax(np.abs(v))
    v_stop = v_start * 0.005
    i_stop:int = None 
    for i in range(i_start,len(v)):
        if np.abs(v[i]) > v_stop:
            i_stop = i
    if i_stop == None:
        raise ValueError("No value of v smaller than 0.5% of v max")
    
    #raw data 
    plt.plot(t,v, 'b-',label='S-Wave Arrivals')
    plt.vlines(x = t[0],ymin = -0.3,ymax= 0.3, color = 'g',linestyles=':', label = "event start")
    plt.vlines(x = t[i_start],ymin = -0.3,ymax= 0.3, color = 'r',linestyles=':', label = "Max v")
    plt.vlines(x = t[i_stop],ymin = -0.3,ymax= 0.3, color = 'g',linestyles=':', label = "event endpoint")
    plt.ylabel('velocity (mm/s)')
    plt.xlabel('time (s)')
    plt.title('Raw data')
    plt.legend()
    plt.savefig('figures/s_wave_data.png')
    plt.close('all')

    T = t[i_stop]
    t = t[:i_stop]
    v = v[:i_stop]
    simp,trap,eps_simp,eps_trap = integrate(t,v)
    N = [2,4,8,16,32]

    #give average squared veloctity
    print(f"Trapezoid Rule Integration: average squared velocity  \n{1/T*np.array(trap)}\n")
    print(f"Trapezoid Rule Integration: Relative Error  \n{eps_trap}\n")
    print(f"Simpson\'s Rule Integration: average squared velocity  \n{1/T*np.array(simp)}\n")
    print(f"Simpson\'s Rule Integration: Relative Error  \n{eps_simp}\n")

    #Integration Approx Error
    plt.loglog(N,eps_simp,label="N.C. Simpson\'s Rule")
    plt.loglog(N,eps_trap,label="N.C. Trapezoid Rule")
    plt.ylabel('Approx Relative Error ('+r'$\epsilon$'+'a)')
    plt.xlabel('Sampling Interval ('+r'$\Delta$'+'t)')
    plt.title('Error Convergence')
    plt.legend()
    plt.savefig('figures/Error_Convergence.png')
    plt.close('all')

    t = t[:i_stop:2]
    v = v[:i_stop:2]
    simp_ds,trap_ds,eps_simp_ds,eps_trap_ds = integrate(t,v)

    #give average squared veloctity downsampled
    print(f"Downsampled Trapezoid Rule Integration: average squared velocity  \n{1/T*np.array(trap_ds)}\n")
    print(f"Downsampled Trapezoid Rule Integration: Relative Error  \n{eps_trap_ds}\n")
    print(f"Downsampled Simpson\'s Rule Integration: average squared velocity  \n{1/T*np.array(simp_ds)}\n")
    print(f"Downsampled Simpson\'s Rule Integration: Relative Error  \n{eps_simp_ds}\n")
    
    #Integration Approx Error downsampled
    plt.loglog(N,eps_simp_ds,label="N.C. Simpson\'s Rule")
    plt.loglog(N,eps_trap_ds,label="N.C. Trapezoid Rule")
    plt.ylabel('Approx Relative Error ('+r'$\epsilon$'+'a)')
    plt.xlabel('Sampling Interval ('+r'$\Delta$'+'t)')
    plt.title('Error Convergence Downsampled')
    plt.legend()
    plt.savefig('figures/Error_Convergence_downsampled.png')
    plt.close('all')

def integrate(x,f):
    k = [1,2,4,8,16,32]
    _simp = []
    _trap = []
    for j in k:
        xj = x[::j]
        fj = f[::j]
        if xj[-1] != x[-1]:
            xj = np.array(xj[:-2])
            xj = np.array(np.append(xj,x[-1]))
            fj =np.array(fj[:-2])
            fj = np.array(np.append(fj,f[-1]))
        I_simp = integrate_newton(xj,fj,alg ="simp")
        _simp.append(I_simp)
        I_trap = integrate_newton(xj,fj,alg ="trap")
        _trap.append(I_trap)
    _eps_simp = np.abs(np.diff(_simp) / _simp[:-1])
    _eps_trap = np.abs(np.diff(_trap) / _trap[:-1])
    return(_simp,_trap,_eps_simp,_eps_trap)

if __name__ == "__main__":
    main()
