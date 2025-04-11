import os
import threading
import webbrowser
from tkinter import filedialog, Label, messagebox, ttk
from PIL import Image
from rembg import remove
from processor import remove_image_background
import platform

# Check the operating system
is_windows = platform.system() == 'Windows'


class BackgroundRemoverApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DeepErase")
        self.window_width = 900
        self.window_height = 480
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(True, True)

        self.center_window()
        self.setup_style()

        self.frame = ttk.Frame(root, padding="30")
        self.frame.pack(fill="both", expand=True)

        self.label = Label(self.frame,
                           text="Select a folder to remove image backgrounds",
                           font=("Segoe UI", 14, "bold"),
                           bg="#1e1e1e",
                           fg="white")
        self.label.pack(pady=(0, 30))

        self.select_button = ttk.Button(self.frame, text=f"{'📂' if not is_windows else ''} Select Folder", command=self.select_folder)
        self.select_button.pack(pady=10)

        self.remove_button = ttk.Button(self.frame, text=f"{'🪄' if not is_windows else ''} Remove Backgrounds", command=self.run_removal)
        self.remove_button.pack(pady=10)

        self.progress = ttk.Progressbar(self.frame, mode='determinate', length=400, style="TProgressbar")
        self.progress.pack(pady=(30, 10))

        self.folder_path_label = Label(self.frame, text="", font=("Segoe UI", 10),
                                       bg="#1e1e1e", fg="#cccccc", wraplength=600, justify="center")
        self.folder_path_label.pack(pady=(0, 20))

        self.image_paths = []
        self.selected_folder = ""

        # Copyright info
        self.add_footer()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        pos_top = int(screen_height / 2 - self.window_height / 2)
        pos_left = int(screen_width / 2 - self.window_width / 2)
        self.root.geometry(f"{self.window_width}x{self.window_height}+{pos_left}+{pos_top}")

    def setup_style(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TFrame", background="#1e1e1e")
        style.configure("TButton",
                        background="#4CAF50",
                        foreground="white",
                        font=("Segoe UI", 11, "bold"),
                        padding=10,
                        relief="flat")
        style.map("TButton",
                  background=[("active", "#45a049"), ("pressed", "#388e3c")],
                  foreground=[("active", "white"), ("pressed", "white")])
        style.configure("TProgressbar",
                        thickness=10,
                        troughcolor="#3a3a3a",
                        background="#4CAF50",
                        bordercolor="#1e1e1e")

    def select_folder(self):
        folder = filedialog.askdirectory(title="Select Folder")
        if folder:
            self.selected_folder = folder
            self.image_paths = [
                os.path.join(folder, f) for f in os.listdir(folder)
                if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.webp'))
            ]
            self.label.config(text=f"{len(self.image_paths)} image(s) selected")
            self.folder_path_label.config(text=f"{'📂' if not is_windows else ''} {self.selected_folder}")

    def run_removal(self):
        if not self.image_paths:
            messagebox.showwarning("No images", "Please select a folder with images first.")
            return
        threading.Thread(target=self.remove_backgrounds).start()

    def remove_backgrounds(self):
        output_folder = os.path.join(self.selected_folder, 'PNG Images')
        os.makedirs(output_folder, exist_ok=True)

        total = len(self.image_paths)
        self.progress["maximum"] = total

        for i, path in enumerate(self.image_paths):
            try:
                output_path = os.path.join(output_folder, os.path.splitext(os.path.basename(path))[0] + '.png')
                remove_image_background(path, output_path)
            except Exception as e:
                print(f"Error processing {path}: {e}")

            self.progress["value"] = i + 1
            self.root.update_idletasks()

        messagebox.showinfo("Done", f"{'✅' if not is_windows else ''} Background removed from {total} image(s).")
        self.label.config(text="Select a folder to remove image backgrounds")
        self.progress["value"] = 0

    def add_footer(self):
        # Text label
        copyright = Label(
            self.frame,
            text="Developed by ",
            font=("Segoe UI", 8),
            bg="#1e1e1e",
            fg="#aaaaaa"
        )
        copyright.place(relx=1.0, rely=1.0, anchor="se", x=-110, y=-10)

        # Link label
        link = Label(
            self.frame,
            text="Jisan Mahmud",
            font=("Segoe UI", 8, "underline"),
            bg="#1e1e1e",
            fg="#4CAF50",
            cursor="hand2"
        )
        link.place(relx=1.0, rely=1.0, anchor="se", x=-30, y=-10)
        link.bind("<Button-1>", lambda e: webbrowser.open("https://github.com/jisan-mahmud"))
