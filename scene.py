import tkinter as tk


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
    #tree_center = scene_left + 500
    #tree_top = scene_top + 100
    #tree_height = 150
    #draw_pine_tree(canvas, tree_center, tree_top, tree_height)



# Define more functions here, like draw_sky, draw_ground,
# draw_cloud, draw_tree, draw_kite, draw_snowflake, etc.

def draw_sky():

def draw_cloud():
    self.master.title("Shapes")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        canvas.create_oval(10, 10, 80, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_oval(110, 10, 210, 80, outline="#f11",
            fill="#1f1", width=2)
        canvas.create_rectangle(230, 10, 290, 60,
            outline="#f11", fill="#1f1", width=2)
        canvas.create_arc(30, 200, 90, 100, start=0,
            extent=210, outline="#f11", fill="#1f1", width=2)

        points = [150, 100, 200, 120, 240, 180, 210,
            200, 150, 150, 100, 200]
        canvas.create_polygon(points, outline='#f11',
            fill='#1f1', width=2)

        canvas.pack(fill=BOTH, expand=1)


def draw_ground():


main()