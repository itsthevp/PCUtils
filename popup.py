from tkinter import Tk, messagebox


def popup(title: str, message: str):
    """
    This will open popup Box with supplied details
    :param title: Title for you popup
    :param message: Message to display in popup
    :return: None
    """
    window = Tk()
    window.wm_withdraw()
    window.bind(messagebox.showinfo(title, message))
    window.destroy()
