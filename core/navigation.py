import tkinter as tk


class Navigation:
    def __init__(self, root, frames):
        self.root = root
        self.frames = frames

    def show_screen(self, screen_name):
        """Show the selected screen by packing its frame and hiding others"""
        for frame in self.frames.values():
            frame.pack_forget()

        frame = self.frames.get(screen_name)
        if frame:
            frame.pack(expand=True, fill="both")

    def toggle_sidebar(self, sidebar_frame, buttons):
        """Expands or collapses the sidebar"""
        if sidebar_frame.winfo_width() > 60:
            sidebar_frame.config(width=60)
            for btn in buttons:
                btn.pack_forget()  # Hide buttons
        else:
            sidebar_frame.config(width=200)
            for btn in buttons:
                btn.pack(pady=5, fill="x")
