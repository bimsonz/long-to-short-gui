import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from long_to_short_cli import process_video

class LongToShortApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Long to Short Video Converter")
        self.geometry("400x275")

        self.create_widgets()

    def create_widgets(self):
        input_label = ttk.Label(self, text="Input video file:")
        input_label.grid(row=0, column=0, padx=(20, 0), pady=(20, 0), sticky=tk.W)

        self.input_entry = ttk.Entry(self)
        self.input_entry.grid(row=0, column=1, padx=(0, 20), pady=(20, 0), sticky=tk.EW)

        output_label = ttk.Label(self, text="Output directory:")
        output_label.grid(row=1, column=0, padx=(20, 0), pady=10, sticky=tk.W)

        self.output_entry = ttk.Entry(self)
        self.output_entry.grid(row=1, column=1, padx=(0, 20), pady=10, sticky=tk.EW)

        output_filename_label = ttk.Label(self, text="Output filename:")
        output_filename_label.grid(row=2, column=0, padx=(20, 0), pady=10, sticky=tk.W)

        self.output_filename_entry = ttk.Entry(self)
        self.output_filename_entry.grid(row=2, column=1, padx=(0, 20), pady=10, sticky=tk.EW)

        start_time_label = ttk.Label(self, text="Start time (HH:MM:SS):")
        start_time_label.grid(row=3, column=0, padx=(20, 0), pady=10, sticky=tk.W)

        self.start_time_entry = ttk.Entry(self)
        self.start_time_entry.grid(row=3, column=1, padx=(0, 20), pady=10, sticky=tk.EW)

        end_time_label = ttk.Label(self, text="End time (HH:MM:SS):")
        end_time_label.grid(row=4, column=0, padx=(20, 0), pady=10, sticky=tk.W)

        self.end_time_entry = ttk.Entry(self)
        self.end_time_entry.grid(row=4, column=1, padx=(0, 20), pady=10, sticky=tk.EW)

        self.process_button = ttk.Button(self, text="Process", command=self.process)
        self.process_button.grid(row=5, column=0, columnspan=2, pady=10, padx=(20, 10), sticky=tk.W)

        self.input_button = ttk.Button(self, text="Browse", command=self.get_input_file)
        self.input_button.grid(row=0, column=2, padx=(0, 20), pady=(20, 0), sticky=tk.E)

        self.output_button = ttk.Button(self, text="Browse", command=self.get_output_directory)
        self.output_button.grid(row=1, column=2, padx=(0, 20), pady=10, sticky=tk.E)

        self.columnconfigure(1, weight=1)

    def get_input_file(self):
        filetypes = [
            ("Video files", "*.mp4;*.avi;*.mov;*.mkv;*.flv;*.wmv"),
            ("All files", "*.*"),
        ]
        input_file = filedialog.askopenfilename(title="Select input video file")
        if input_file:
            self.input_entry.delete(0, tk.END)
            self.input_entry.insert(0, input_file)

    def get_output_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory)

    def process(self):
        input_video = self.input_entry.get()
        output_directory = self.output_entry.get()
        output_filename = self.output_filename_entry.get()
        start_time = self.start_time_entry.get()
        end_time = self.end_time_entry.get()

        if not input_video or not output_directory or not output_filename or not start_time or not end_time:
            messagebox.showerror("Error", "Please fill out all fields")
            return

        output_video = f"{output_directory}/{output_filename}"

        try:
            process_video(input_video, output_video, start_time, end_time)
            messagebox.showinfo("Success", "Video processed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Error processing video: {e}")

if __name__ == "__main__":
    app = LongToShortApp()
    app.mainloop()
