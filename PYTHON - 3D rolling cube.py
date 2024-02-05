import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D

# Function to generate the vertices of a cube
def cube_vertices(center, size):
    c = center
    s = size / 2
    return np.array([[c[0]-s, c[1]-s, c[2]-s],
                     [c[0]+s, c[1]-s, c[2]-s],
                     [c[0]+s, c[1]+s, c[2]-s],
                     [c[0]-s, c[1]+s, c[2]-s],
                     [c[0]-s, c[1]-s, c[2]+s],
                     [c[0]+s, c[1]-s, c[2]+s],
                     [c[0]+s, c[1]+s, c[2]+s],
                     [c[0]-s, c[1]+s, c[2]+s]])

# Function to draw a cube
def plot_cube(ax, vertices, color='blue'):
    edges = [(0, 1), (1, 2), (2, 3), (3, 0),
             (4, 5), (5, 6), (6, 7), (7, 4),
             (0, 4), (1, 5), (2, 6), (3, 7)]
    for edge in edges:
        start, end = vertices[edge[0]], vertices[edge[1]]
        ax.plot3D(*zip(start, end), color=color)

# Create figure and 3D axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_zlim(-2, 2)

# Initial cube properties
center = (0, 0, 0)
size = 1
vertices = cube_vertices(center, size)
plot_cube(ax, vertices)

# Animation update function
def update(frame):
    ax.cla()  # Clear the axis to redraw
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(-2, 2)
    
    # Rotate the cube
    angle = np.radians(frame)
    rot_matrix = np.array([[np.cos(angle), -np.sin(angle), 0],
                           [np.sin(angle), np.cos(angle), 0],
                           [0, 0, 1]])
    rotated_vertices = np.dot(vertices - center, rot_matrix) + center
    
    # Redraw the cube
    plot_cube(ax, rotated_vertices)

    return fig,

# Create animation
ani = animation.FuncAnimation(fig, update, frames=np.arange(0, 360, 2), blit=False, interval=50)

plt.show()
