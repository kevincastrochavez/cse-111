import tkinter as tk
from random import randint


def main():
    # The width and height of the scene window.
    width = 800
    height = 500

    # Create the Tk root object.
    root = tk.Tk()
    root.geometry(f"{width}x{height}")

    # Create a Frame object.
    frame = tk.Frame(root)
    frame.master.title("Scene")
    frame.pack(fill=tk.BOTH, expand=1)

    # Create a canvas object that will draw into the frame.
    canvas = tk.Canvas(frame)
    canvas.pack(fill=tk.BOTH, expand=1)

    # Call the draw_scene function.
    draw_scene(canvas, 0, 0, width-1, height-1)

    root.mainloop()


def draw_scene(canvas, scene_left, scene_top, scene_right, scene_bottom):
    """Draw a scene in the canvas. scene_left, scene_top,
    scene_right, and scene_bottom contain the extent in
    pixels of the region where the scene should be drawn.
    Parameters
        scene_left: left side of the region; less than scene_right
        scene_top: top of the region; less than scene_bottom
        scene_right: right side of the region
        scene_bottom: bottom of the region
    Return: nothing

    If needed, the width and height of the
    region can be calculated like this:
    scene_width = scene_right - scene_left + 1
    scene_height = scene_bottom - scene_top + 1
    """
    # Call your functions here, such as draw_sky, draw_ground,
    # draw_snowman, draw_tree, draw_shrub, etc.
    sun_initial_x = scene_left - 150
    sun_initial_y = scene_top - 150
    sun_final_x = scene_left + 150
    sun_final_y = scene_top + 150

    cloud_initial_x = 1
    cloud_initial_y = 1
    cloud_final_x = 1
    cloud_final_y = 1
    
    ground_initial_x = scene_left 
    ground_initial_y = (scene_bottom / 4) * 3 
    ground_final_x = scene_right
    ground_final_y = scene_bottom

    grass_initial_x = scene_left 
    grass_initial_y = (scene_bottom / 4) * 3
    grass_final_x = scene_right
    grass_final_y = (scene_bottom / 8) * 5

    draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom)
    for _ in range(6):
        draw_cloud(canvas, cloud_initial_x * randint(200, scene_right), cloud_initial_y * randint(scene_top, 200), cloud_final_x * randint(200, scene_right), cloud_final_y * randint(scene_top, 200))
    draw_sun(canvas, sun_initial_x, sun_initial_y, sun_final_x, sun_final_y)
    draw_ground(canvas, ground_initial_x, ground_initial_y, ground_final_x, ground_final_y)
    draw_grass(canvas, grass_initial_x, grass_initial_y, grass_final_x, grass_final_y)

    tree_center = scene_left + 30
    tree_top = (scene_top + 211)
    tree_height = 100
    for _ in range(1, 10):
        draw_pine_tree(canvas, tree_center * _, tree_top, tree_height)
    



# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky(canvas, scene_left, scene_top, scene_right, scene_bottom):
    canvas.create_rectangle(scene_left, scene_top, scene_right, scene_bottom, fill="#87ceeb")

def draw_sun(canvas, initial_x, initial_y, final_x, final_y):
    canvas.create_oval(initial_x, initial_y, final_x, final_y, fill="#FDB813")

def draw_ground(canvas, initial_x, initial_y, final_x, final_y):
    canvas.create_rectangle(initial_x, initial_y, final_x, final_y, fill="#684132")

def draw_grass(canvas, initial_x, initial_y, final_x, final_y):
    canvas.create_rectangle(initial_x, initial_y, final_x, final_y, fill="#69d500")

def draw_cloud(canvas, initial_x, initial_y, final_x, final_y):
    canvas.create_oval(initial_x, initial_y, final_x, final_y, fill='#ffffff')

def draw_pine_tree(canvas, peak_x, peak_y, height):
    trunk_width = height / 10
    trunk_height = height / 4
    trunk_left = peak_x - trunk_width / 2
    trunk_right = peak_x + trunk_width / 2
    trunk_bottom = peak_y + height

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = peak_x - skirt_width / 2
    skirt_right = peak_x + skirt_width / 2
    skirt_bottom = peak_y + skirt_height

    # Draw the trunk of the pine tree.
    canvas.create_rectangle(trunk_left, skirt_bottom,
            trunk_right, trunk_bottom,
            outline="gray20", width=1, fill="tan3")

    # Draw the crown (also called skirt) of the pine tree.
    canvas.create_polygon(peak_x, peak_y,
            skirt_right, skirt_bottom,
            skirt_left, skirt_bottom,
            outline="gray20", width=1, fill="dark green")

# Call the main function so that
# this program will start executing.
main()