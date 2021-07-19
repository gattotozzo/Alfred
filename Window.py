from tkinter import *
from pystray import MenuItem as item
import pystray
from PIL import Image, ImageTk
from multiprocessing import Process
import os, sys

class AssistantWindow:

    def __init__(self):
        self.win = Tk()
        self.win.title("Alfred")
        self.win.geometry("700x350")
        self.win.resizable(False, False)

    def _quit_window(self):
        self.icon.stop()
        self.p.kill()
        self.win.destroy()

    def _show_window(self):
        self.icon.stop()
        self.win.after(0, self.win.deiconify())

    def _resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

    def _hide_window(self):
        self.win.withdraw()
        image = Image.open(self._resource_path("alfredIcon.ico"))
        menu = (item('Quit Assistant', self._quit_window), item('Show Window', self._show_window))
        self.icon = pystray.Icon("name", image, "Alfred", menu=menu)
        self.icon.run()

    def startWindow(self, backgroundProcess):
        self.win.protocol('WM_DELETE_WINDOW', self._hide_window)
        self.p = Process(target=backgroundProcess)
        self.p.start()
        self.win.mainloop()