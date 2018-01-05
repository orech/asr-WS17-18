#/usr/bin/python3

# =================================================
# Your names:





# =================================================
# Automatic Speech Recognition WS-17-18
# Exercise 7, Task 7.2

# Please make use of the functions and the variables
# provided in this notebook when you write your answer codes.
import matplotlib.pyplot as plt
import numpy as np

def Read(filename):
    x_data = []
    y_data = []
    # Read function:
    #   Reads the 2D data from the file path
    #   Returns a list for each component of the data.
    with open(filename) as f:
        data_str = f.readlines()
        for i in range(0, len(data_str)):
            data_point = data_str[i].split()
            x_data.append(float(data_point[0]))
            y_data.append(float(data_point[1]))
        return x_data, y_data

# ==========================================================================
# This is another helper code cell which introduces
# the name of variables to be used in your solution
# as well as the data you will use.
# The task starts at the next cell.

# Download the data from L2P and put the path here:
data = "./observations_ex7.data"
data_x, data_y = Read(data)

# Visualize the data
print("Let's see how the data look like.")
plt.scatter(data_x, data_y)
plt.show()

print("We can see 3 or 4 groups of points, right?\n")
print("We will model this data with 4 densities (L=4).\n")

# Set the hyperparameters given in the text:
L = 4  # Maximum number of densities
R = 10  # Number of iterations
eps_u = [0.1, 0.1]  # Vector: epsilon * u

# Number of data points:
N = len(data_x)

# Compute the initial mean
init_mean = [0.,0.]
for i in range(0,N):
    init_mean[0] += float(data_x[i])
    init_mean[1] += float(data_y[i])
init_mean[0] *= 1./float(N)
init_mean[1] *= 1./float(N)

# Compute the initial variance
init_var = [0., 0.]
for i in range(0,N):
    init_var[0] += (data_x[i]-init_mean[0])*(data_x[i]-init_mean[0])
    init_var[1] += (data_y[i]-init_mean[1])*(data_y[i]-init_mean[1])
init_var[0] *= 1./float(N)
init_var[1] *= 1./float(N)

def Init():
    # Add the initial density to the list.
    global Mean
    Mean = []  # Mean is a list in which Mean[l] stores the mean vector for the density l.
    Mean.append(init_mean)
    
    global Var
    Var = init_var  # Pooled variance.
    
    global p_l
    p_l = []  # Array to store p(l) (cf. the notation given in the sheet).
    p_l.append(1)

    global N_l  # Array to store N_l (cf. the notation given in the sheet).
    N_l = np.zeros([L])  
    N_l = list(N_l)
    N_l[0] = N
    
    global A  # Array to store the membership of each point.
    A = np.zeros([N], dtype=np.int32)
    A = list(A)
    print('Initialization done.')

Init()
print('Initial density:')
print('Mean:', Mean[0])
print('Variance:', Var)

# ==============================================================================
#   Functions for (a)
# ==============================================================================
def Gaussian(x, mean, var):
    # Returns p(x|l) (cf. the notation given in the sheet)
    # You can use for example np.exp for the exponential
    # For the number 'pi', you can e.g. use 'np.pi'
    # TODO You code here
    return 0

def Assign(K):
    # Update the membership of each points
    # (list A introduced in the previous cell)
    # K: current number of densities
    # TODO You code here
    return 0

# ==============================================================================
# Function for (c)
# ==============================================================================
def EstimateParameters(K):
    # Re-estimate the means and variances for all densities
    # K: current number of densities
    # TODO You code here
    return 0

# ==============================================================================
# Functions for (d)
# ==============================================================================
def FindMinLogLike(K):
    # Return the index of the density with the lowest likelihood.
    # TODO You code here
    return 0

def SplitDensity(l):
    # Split the density l.
    # If needed: When you have a list L, you can use L.pop(n) to remove the
    # element in position n of the list L.
    # TODO You code here
    return 0

# ==============================================================================

Init()
# Apply the algorithm to the data.
# Report the mean, variance and membership for each split iteration.

# TODO You code here

# Checkpoint: after the first split, you should get the following:
# Mean: [[5.06, 5.33], [2.05, 1.90]]
# Var: [3.96, 3.33]
# Membership: [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


# ==============================================================================
# Visualization of the split you obtained
# ==============================================================================

# This cell is a helper to show you an example method to plot
# data points with different colors.

split_example = [1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
Colors = ['b', 'r', 'y', 'm']  # blue, red, yellow, magenta. No need to modify this list.

color = [Colors[split_example[i]] for i in range(0, N)]  # List of the color for each data point.
plt.scatter(data_x, data_y, c=color)  # 'c' argument to provide the color for each point as a list.
plt.show()

# You will plot your own results below.

# ==============================================================================
# Plots for the last question
# ==============================================================================
# Split 0
print("Split 0")
# TODO You code here
# Split 1
print("Split 1")
# TODO You code here
# Split 2
print("Split 2")
# TODO You code here
# For the Plot in the last question
# Split 3
print("Split 3")
# TODO You code here



# End of the Task 7.2
