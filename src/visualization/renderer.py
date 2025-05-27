from matplotlib import pyplot as plt
import matplotlib.patches as patches

def render_floor_plan(ax, floor_plan):
    for wall in floor_plan['walls']:
        x, y, width, height = wall['x'], wall['y'], wall['width'], wall['height']
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='black', facecolor='none')
        ax.add_patch(rect)

    for window in floor_plan['windows']:
        x, y, width, height = window['x'], window['y'], window['width'], window['height']
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='blue', facecolor='lightblue')
        ax.add_patch(rect)

    ax.set_xlim(0, floor_plan['width'])
    ax.set_ylim(0, floor_plan['height'])
    ax.set_aspect('equal', adjustable='box')
    ax.axis('off')