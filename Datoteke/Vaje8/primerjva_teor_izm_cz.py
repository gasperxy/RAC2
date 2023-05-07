import time
import random
import heapq
import math
import matplotlib.pyplot as plt
from djikstra import djikstra

import time
import matplotlib.pyplot as plt
import time
import matplotlib.pyplot as plt

# Define the function djikstra here

# Define the range of input sizes to test
sizes = [100, 200, 300, 400, 500]

# Define lists to store the measured and theoretical times
measured_times = []
theoretical_times = []

# Loop over the input sizes and measure the running time
for n in sizes:
    # Generate a random graph with n vertices and m edges
    m = n * 10
    G = [[] for _ in range(n)]
    for i in range(m):
        u, v, w = random.randint(0, n-1), random.randint(0, n-1), random.randint(1, 10)
        G[u].append((v, w))
        G[v].append((u, w))
    
    # Measure the running time of the algorithm
    start_time = time.time()
    djikstra(G, 0)
    end_time = time.time()
    measured_times.append(end_time - start_time)
    
    # Calculate the theoretical running time of the algorithm
    theoretical_time = (n + m) * math.log(n, 2)
    theoretical_times.append(theoretical_time)
    
# Plot the measured and theoretical times on the same graph
plt.plot(sizes, measured_times, label='Measured time')
plt.plot(sizes, theoretical_times, label='Theoretical time')
plt.xlabel('Input size')
plt.ylabel('Running time (seconds)')
plt.legend()
plt.show()