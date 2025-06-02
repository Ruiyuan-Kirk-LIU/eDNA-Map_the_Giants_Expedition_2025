import geopandas as gpd
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Load the world shapefile
shapefile_path = r'D:\Python\matplotlib\ne_10m_admin_0_countries.shp'
world = gpd.read_file(shapefile_path)

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 10))  # Maintain overall figure size

# Plot the world map
world.plot(ax=ax, color='lightgray', edgecolor='black', linewidth=0.5)

# Highlight Maldives region with a red transparent rectangle
highlight = Rectangle((72, -1), 2.5, 9,
                      linewidth=0, facecolor='red', alpha=0.3)
ax.add_patch(highlight)

# North arrow placed at the bottom-right
ax.annotate('', xy=(88, -3), xytext=(88, -6),
            arrowprops=dict(facecolor='black', width=5, headwidth=10),
            ha='center')
ax.text(88, -7, 'N', ha='center', va='center', fontsize=12, fontweight='bold')

# Set new extended map limits
ax.set_xlim(30, 90)
ax.set_ylim(-10, 30)

# Labels and grid
ax.set_xlabel('Longitude', fontsize=12, fontweight='bold')
ax.set_ylabel('Latitude', fontsize=12, fontweight='bold')
ax.tick_params(axis='both', which='major', labelsize=10, width=1)
ax.grid(True, linestyle='--', linewidth=0.5)
ax.set_aspect('equal')

# Show the final map
plt.tight_layout()
plt.show()
