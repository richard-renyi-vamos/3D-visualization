import pygame
import math

# Initialize Pygame
pygame.init()

# Create a display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 3D cube points
cube_points = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1),
               (-1, -1, 1), (1, -1, 1), (1, 1, 1), (-1, 1, 1)]

# Function to rotate points in space
def rotate_point(point, angle):
    x, y, z = point
    # Rotate around Y axis
    x, z = x * math.cos(angle) - z * math.sin(angle), x * math.sin(angle) + z * math.cos(angle)
    return x, y, z

# Function to project 3D points to 2D
def project_point(point):
    x, y, z = point
    # Simple perspective projection
    distance = 5
    f = 200 / (z + distance)
    x, y = x * f, y * f
    return int(width / 2 + x), int(height / 2 - y)

# Main loop
running = True
angle = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear screen
    screen.fill(BLACK)

    # Update rotation angle
    angle += 0.01

    # Draw cube
    for i, point in enumerate(cube_points):
        rotated_point = rotate_point(point, angle)
        projected_point = project_point(rotated_point)
        pygame.draw.circle(screen, WHITE, projected_point, 5)

        # Draw lines between points to form edges of the cube
        for j in range(i, len(cube_points)):
            if sum(abs(a - b) for a, b in zip(point, cube_points[j])) == 2:
                rotated_point_2 = rotate_point(cube_points[j], angle)
                projected_point_2 = project_point(rotated_point_2)
                pygame.draw.line(screen, WHITE, projected_point, projected_point_2, 1)

    # Update display
    pygame.display.flip()
    pygame.time.wait(10)

pygame.quit()
