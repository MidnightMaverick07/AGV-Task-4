import numpy as np

def is_collision_free(map_array, point1, point2):
    # Ensure points are integers
    x1, y1 = int(point1[0]), int(point1[1])
    x2, y2 = int(point2[0]), int(point2[1])
    
    # 1. Handle the zero-length path case
    if (x1, y1) == (x2, y2):
        return map_array[y1, x1] >= 128

    # 2. Robust sampling density (ensures every pixel is touched)
    num_points = max(abs(x2 - x1), abs(y2 - y1)) + 1
    
    x_coords = np.linspace(x1, x2, num_points).astype(int)
    y_coords = np.linspace(y1, y2, num_points).astype(int)
    
    # Get map boundaries
    h, w = map_array.shape
    
    for x, y in zip(x_coords, y_coords):
        # 3. Boundary check to prevent IndexError
        if not (0 <= x < w and 0 <= y < h):
            return False
            
        # 4. Check for obstacles (0 is wall, 255 is path)
        if map_array[y, x] < 128: 
            return False
            
    return True