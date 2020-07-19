#Import NumPy
import numpy as np
def crank_nicolson(yn, h, a):
    """
    Function for executing one time step of the Crank-Nicolson method.
                INPUT:
                    yn (float): Current numerical solution.
                    h (float): Time step size.
                    a (float): ODE parameter.
                OUTPUT:
                    (float): Next numerical solution.
    """
    return (1.+0.5*h*a)/(1.-0.5*h*a)*yn

def simulate_crank_nicolson(T, N, x0, a):
    """
                INPUT:
                    T (float): End time
                N (integer): Number of time steps
                    x0 (float): Initial condition
                    a (float): ODE parameter
                OUTPUT:
                    y (np.array): NumPy array of size N containing numerical solution at each time s
    """
    # Get time step size:
    h = T/N
    # Initialize solution array:
    y = np.zeros(N, dtype=float) # Set initial condition
    y[0] = x0
    for i in range(N-1):
        # Execute time step
        y[i+1] = crank_nicolson(y[i],h,a) # Return numerical solution
    return y

#Set some parameters:
T = 1. # End time
a = -100. # (We can change this if we want to, of course)
x0 = 1. # Initial condition
# Set up an array of N's:
N_arr = 2**np.arange(3,11)
# Initialize error array
err_arr = np.zeros(len(N_arr), dtype=float) # Go through each value of N
for i in range(len(N_arr)):
    N = N_arr[i]
    # Get numerical solution
    y = simulate_crank_nicolson(T, N, x0, a) # Get exact solution:
    t = np.linspace(0, T, N, endpoint=False)
    x_exact = np.exp(a*t)
    # Compute the maximum error
    err = np.abs(x_exact - y)
    err_arr[i] = np.max(err)

# Print the top row of the table
print("h\tE_h\tr")
print("----------------------") # Just a horizontal line

# Print each row:
for i in range(len(N_arr)): # Calculate h:
    N = N_arr[i]
    h = T/N
    # If we're on the finest grid, we can't calculate r:
    if (i < len(N_arr)-1):
        r = np.log(err_arr[i]/err_arr[i+1])/np.log(2.)
        print("{}\t{}\t{}".format(h, err_arr[i], r))
    else:
        print("{}\t{}\t***".format(h, err_arr[i]))
# Done with loop.
