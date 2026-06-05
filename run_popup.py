import os
import tkinter as tk
from PIL import Image, ImageTk

# 1. Initialize the main pop-up window
root = tk.Tk()
root.title("Download Complete")
root.configure(bg="#F2F6FA") # Match our spreadsheet's clean look!

# 2. Position the pop-up right in the center of your screen
window_width = 450
window_height = 180
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width/2 - window_width/2)
center_y = int(screen_height/2 - window_height/2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

# 3. Pull your beautiful angel wing PNG from your Downloads folder
downloads_path = os.path.join(os.environ["USERPROFILE"], "Downloads")
png_path = os.path.join(downloads_path, "watermarked_img_5425409057254183864.png")

try:
    # Scale it to a nice, prominent size for the inside of the box
    pil_img = Image.open(png_path).resize((64, 64), resample=Image.Resampling.NEAREST)
    tk_icon = ImageTk.PhotoImage(pil_img)
    
    # Set the window bar icon too!
    root.iconphoto(True, tk_icon)
    
    # 4. Create the inner layout (Replacing the blue "!" with your wing!)
    icon_label = tk.Label(root, image=tk_icon, bg="#F2F6FA")
    icon_label.pack(side="left", padx=30)
except Exception as e:
    print(f"Could not load image inside the box: {e}")

# 5. Add your custom success message text next to the wing
message_text = "✨ Success!\n\nAll 1,450 global Angel variants have\nbeen compiled and saved to your drive!"
text_label = tk.Label(
    root, 
    text=message_text, 
    justify="left", 
    font=("Segoe UI", 10, "bold"), 
    fg="#1F4E78", 
    bg="#F2F6FA"
)
text_label.pack(side="left", pady=10)

# 6. Add a clean, styled Close Button at the bottom
close_button = tk.Button(
    root, 
    text="Awesome", 
    font=("Segoe UI", 9, "bold"),
    bg="#1F4E78", 
    fg="white", 
    width=12, 
    command=root.destroy
)
# Place the button neatly at the bottom center
close_button.place(relx=0.5, rely=0.85, anchor="center")

# 7. Keep the window alive and waiting on your screen
root.mainloop()