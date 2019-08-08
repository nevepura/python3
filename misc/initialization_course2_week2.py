# ZERO INIT
parameters['W' + str(l)] = np.zeros((layers_dims[l], layers_dims[l-1]))
parameters['b' + str(l)] = np.zeros((layers_dims[l], 1))

# RANDOM INIT
np.random.randn(layers_dims[l], layers_dims[l-1]) * 10

# HE INIT
parameters['W' + str(l)] = np.random.randn(layers_dims[l], layers_dims[l-1]) * (np.sqrt(2/layers_dims[l-1]))
        parameters['b' + str(l)] = np.zeros((layers_dims[l], 1))