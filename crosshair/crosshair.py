from tkinter import Tk, Label, Canvas
from tkvideo import tkvideo
import win32gui
import win32con
import win32api
import time

# Define the paths to your video files
video_paths = ["video1.mp4", "video2.mp4", "video3.mp4", "video4.mp4"]

# Create the main window
root = Tk()
root.title("Crosshair Videos")
root.geometry("220x220")  # Set this to your preferred window size
root.attributes("-topmost", True)  # Always on top
root.overrideredirect(True)  # Remove window decorations (borderless)
root.wm_attributes("-transparentcolor", "black")
canvas = Canvas(root, width=220, height=220, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Create four labels for the videos
label1 = Label(canvas)
label1.place(relx=0.5, rely=0.0, anchor="n")
label2 = Label(canvas)
label2.place(relx=1.0, rely=0.5, anchor="e")
label3 = Label(canvas)
label3.place(relx=0.5, rely=1.0, anchor="s")
label4 = Label(canvas)
label4.place(relx=0.0, rely=0.5, anchor="w")

# Load the videos into the labels
player1 = tkvideo(video_paths[0], label1, loop=1, size=(10, 100))
player1.play()
player2 = tkvideo(video_paths[1], label2, loop=1, size=(100, 10))
player2.play()
player3 = tkvideo(video_paths[2], label3, loop=1, size=(10, 100))
player3.play()
player4 = tkvideo(video_paths[3], label4, loop=1, size=(100, 10))
player4.play()

# Wait for the window to be created and obtain the window handle
root.update_idletasks()
time.sleep(0.1)  # Small delay to ensure window creation

hwnd = win32gui.FindWindow(None, "Crosshair Videos")
if hwnd:
    # Get screen dimensions
    screen_width = win32api.GetSystemMetrics(win32con.SM_CXSCREEN)
    screen_height = win32api.GetSystemMetrics(win32con.SM_CYSCREEN)
    
    # Calculate position to center the window
    window_width = 220
    window_height = 220
    position_right = int(screen_width/2 - window_width/2)
    position_down = int(screen_height/2 - window_height/2)
    
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, position_right, position_down, 0, 0,
                          win32con.SWP_NOSIZE)
    
    # Set the window as a layered window with WS_EX_TRANSPARENT style
    ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
    ex_style |= win32con.WS_EX_LAYERED | win32con.WS_EX_TRANSPARENT
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style)
else:
    print("Window not found!")

root.mainloop()
