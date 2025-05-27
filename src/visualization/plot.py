def create_streamplot(wind_vectors, floor_plan):
    import matplotlib.pyplot as plt
    import numpy as np

    # Create a grid for the streamplot
    Y, X = np.mgrid[0:floor_plan.shape[0], 0:floor_plan.shape[1]]
    
    # Extract wind vectors
    U = wind_vectors[:, :, 0]
    V = wind_vectors[:, :, 1]

    # Create the streamplot
    plt.figure(figsize=(10, 10))
    plt.streamplot(X, Y, U, V, color='blue', linewidth=1, density=2)

    # Overlay the floor plan
    plt.imshow(floor_plan, extent=[0, floor_plan.shape[1], floor_plan.shape[0], 0], alpha=0.5)

    plt.title('2D Wind Flow Simulation')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.xlim(0, floor_plan.shape[1])
    plt.ylim(floor_plan.shape[0], 0)
    plt.grid()
    plt.show()