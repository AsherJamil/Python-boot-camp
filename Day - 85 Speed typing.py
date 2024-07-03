import tkinter as tk
from tkinter import messagebox
import time

# Sample text for typing test
sample_text = "The quick brown fox jumps over the lazy dog."


class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_label = tk.Label(
            root, text=sample_text, wraplength=400, font=("Helvetica", 14))
        self.sample_label.pack(pady=20)

        self.entry = tk.Text(root, height=5, width=50,
                             wrap='word', font=("Helvetica", 14))
        self.entry.pack(pady=10)
        self.entry.bind('<KeyPress>', self.start_test)

        self.result_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.result_label.pack(pady=20)

        self.start_time = None

    def start_test(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.entry.bind('<Return>', self.end_test)

    def end_test(self, event):
        if self.start_time is not None:
            end_time = time.time()
            elapsed_time = end_time - self.start_time

            typed_text = self.entry.get("1.0", "end-1c")
            word_count = len(typed_text.split())

            wpm = (word_count / elapsed_time) * 60
            self.result_label.config(
                text=f"Your typing speed is {wpm:.2f} WPM")

            self.entry.unbind('<Return>')
            self.start_time = None
        else:
            messagebox.showerror(
                "Error", "Test did not start correctly. Please try again.")


def main():
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
