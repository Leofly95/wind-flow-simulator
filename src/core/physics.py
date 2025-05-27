def calculate_velocity(wind_speed, angle):
    import numpy as np
    # Convert angle from degrees to radians
    angle_rad = np.radians(angle)
    # Calculate velocity components
    vx = wind_speed * np.cos(angle_rad)
    vy = wind_speed * np.sin(angle_rad)
    return vx, vy

def apply_boundary_conditions(velocity, boundaries):
    # Adjust velocity based on boundary conditions
    for boundary in boundaries:
        if boundary['type'] == 'wall':
            # Reflect velocity if it hits a wall
            if boundary['direction'] == 'horizontal':
                velocity[1] = -velocity[1]
            elif boundary['direction'] == 'vertical':
                velocity[0] = -velocity[0]
    return velocity