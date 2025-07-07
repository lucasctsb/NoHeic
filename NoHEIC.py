# Convert HEIC to TIFF

import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import pillow_heif
import threading

def convert_heic_to_tiff(source_folder, destination_folder, progress_callback):
    try:
        pillow_heif.register_heif_opener()
        files_to_convert = [f for f in os.listdir(source_folder) if f.lower().endswith('.heic')]
        total_files = len(files_to_convert)

        if total_files == 0:
            messagebox.showinfo("No Files Found", "No .heic files were found in the selected source folder.")
            return

        for i, filename in enumerate(files_to_convert):
            heic_filepath = os.path.join(source_folder, filename)
            base_filename = os.path.splitext(filename)[0]
            tiff_filepath = os.path.join(destination_folder, f"{base_filename}.tiff")

            try:
                image = Image.open(heic_filepath)
                image.save(tiff_filepath, format='TIFF', compression='tiff_lzw')
                progress_callback(i + 1, total_files, f"Converted: {filename}")
            except Exception as e:
                print(f"Could not convert file {filename}. Error: {e}")

        messagebox.showinfo("Success", f"Conversion complete! {total_files} files were converted.")

    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")
    finally:
        progress_callback(-1, -1, "Finished")

class ConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NoHEIC")
        self.root.minsize(550, 300)

        main_frame = ttk.Frame(root, padding="20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        self.source_path = tk.StringVar()
        self.dest_path = tk.StringVar()

        ttk.Label(main_frame, text="Source Folder (HEIC files):").pack(pady=(0, 5))
        source_frame = ttk.Frame(main_frame)
        source_frame.pack(pady=(0, 10))
        ttk.Entry(source_frame, textvariable=self.source_path, width=50).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(source_frame, text="Browse...", command=self.select_source_folder).pack(side=tk.LEFT)

        ttk.Label(main_frame, text="Destination Folder (to save TIFFs):").pack(pady=(10, 5))
        dest_frame = ttk.Frame(main_frame)
        dest_frame.pack(pady=(0, 10))
        ttk.Entry(dest_frame, textvariable=self.dest_path, width=50).pack(side=tk.LEFT, padx=(0, 5))
        ttk.Button(dest_frame, text="Browse...", command=self.select_dest_folder).pack(side=tk.LEFT)
        
        self.convert_button = ttk.Button(main_frame, text="Convert", command=self.start_conversion, style='Accent.TButton')
        self.convert_button.pack(pady=15)
        style = ttk.Style()
        style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'))

        self.progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=400, mode="determinate")
        self.progress_bar.pack(pady=5)
        self.status_label = ttk.Label(main_frame, text="Select folders and click Convert.")
        self.status_label.pack(pady=5)

    def select_source_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.source_path.set(folder_selected)

    def select_dest_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.dest_path.set(folder_selected)

    def update_progress(self, current, total, message):
        if current == -1:
            self.convert_button.config(state="normal")
            self.status_label.config(text="Process finished.")
            self.progress_bar['value'] = 0
        else:
            self.status_label.config(text=message)
            self.progress_bar['value'] = (current / total) * 100
        self.root.update_idletasks()

    def start_conversion(self):
        source = self.source_path.get()
        dest = self.dest_path.get()

        if not source or not dest:
            messagebox.showerror("Error", "Please select both source and destination folders.")
            return
        
        self.convert_button.config(state="disabled")
        
        conversion_thread = threading.Thread(
            target=convert_heic_to_tiff,
            args=(source, dest, self.update_progress)
        )
        conversion_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    app = ConverterApp(root)
    root.mainloop()