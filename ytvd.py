from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox, filedialog
from pytube import YouTube

def Widgets():
    label1 = Label(window, text="Enter URL:", font=('arial', 15, 'underline'), background="#000137", foreground="white").pack(pady=10)
    url_entry = Entry(window, width=100, textvariable=url).pack(pady=10)
    
    label2 = Label(window, text="Download Destination:", font=('arial', 15, 'underline'), background="#000137", foreground="white").pack(pady=10)
    dest_entry = Entry(window, width=100, textvariable=dest_path).pack(pady=10)

    style = Style()
    style.configure('W.TButton', font=('arial', 15))

    browse = Button(window, text="Browse", width=10,style='W.TButton', command=Browse).pack(pady=10)

    #External link icon for the Go button:
    link_img = PhotoImage(file="cs50-final-project\link.png").subsample(60, 60)
    btn = Button(window, text="Go", style='W.TButton', image=link_img, compound='left', width=5, command=Download).pack(pady=10)

def Download():
    #Get input from the entry objects.
    link = url.get()
    dest = dest_path.get()
    #yt object for the video.
    yt = YouTube(link)
    yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download(dest)
    #Prompting the user about successful execution.
    messagebox.showinfo("SUCCESS","DOWNLOADED AND SAVED IN\n" + dest)

def Browse():
    #A classic browse button to browse and set the download destination. Default path set to C: drive.
    download_Directory = filedialog.askdirectory(
        initialdir="C:/", title="Save Video")
    #Sets the text in entry2 input field to the path received from the user.
    dest_path.set(download_Directory)

window = Tk()
window.geometry("700x300")
window.resizable(width=False, height=False)
window.title("YT Video Downloader")
window.configure(background='#000137')

dest_path = StringVar()
url = StringVar()

Widgets()

window.mainloop()