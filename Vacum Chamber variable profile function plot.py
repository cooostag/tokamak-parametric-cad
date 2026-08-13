import matplotlib.pyplot as plt
import numpy as np

# Set up theta domain (0 to 2*pi)
theta = np.linspace(0, 2 * np.pi, 500)

# Parameters from prompt (mapping 'inner' -> inboard = 8, 'outer' -> outboard = 3)
thickness_inboard = 8
thickness_outboard = 3

thickness_theta = (thickness_outboard + thickness_inboard) / 2 + (thickness_outboard - thickness_inboard) / 2 * np.cos(theta)

plt.figure(figsize=(8, 5))
plt.plot(theta, thickness_theta, label=r'$\text{thickness}(\theta)$', color='#1f77b4', linewidth=2)
plt.axhline(thickness_inboard, color='red', linestyle='--', label=f'Inboard = {thickness_inboard} (at $\\theta = \\pi$)')
plt.axhline(thickness_outboard, color='green', linestyle='--', label=f'Outboard = {thickness_outboard} (at $\\theta = 0, 2\\pi$)')

plt.title('Thickness as a Function of Poloidal Angle $\\theta$', fontsize=14)
plt.xlabel('$\\theta$ (radians)', fontsize=12)
plt.ylabel('Thickness', fontsize=12)
plt.xticks(
    [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi],
    ['0', '$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']
)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(loc='upper right')

plt.show()