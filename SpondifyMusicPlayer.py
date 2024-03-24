from tkinter import filedialog
from tkinter import *
import pygame
import os

root = Tk()
root.title('Spondify')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []
curr_song = ''
paused = False

def load_music():
    global curr_song
    root.directory = filedialog.askdirectory()
    
    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3' or ext =='.wav':
            songs.append(song)
    
    for song in songs:
        songlist.insert('end', song)
        
    songlist.selection_set(0)
    curr_song = songs[songlist.curselection()[0]]

def play_music():
    global curr_song, paused
    
    if not paused:
        pygame.mixer.music.load(os.path.join(root.directory, curr_song))
        pygame.mixer.music.set_volume(0.7)  # Set volume to 70%
        pygame.mixer.music.play()
        
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global curr_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(curr_song) + 1) 
        curr_song = songs[songlist.curselection()[0]]
        play_music()  
    except:
        pass

def prev_music():
    global curr_song, paused
    
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(curr_song) -1) 
        curr_song = songs[songlist.curselection()[0]]
        play_music()  
    except:
        pass

organize_menu = Menu(menubar, tearoff=False)
organize_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organize', menu=organize_menu)

songlist = Listbox(root, bg='black', fg='white', width=100, height=15)
songlist.pack()

play_btn_img = PhotoImage(file='play.png')
pause_btn_img = PhotoImage(file='pause.png')
next_btn_img = PhotoImage(file='next.png')
prev_btn_img = PhotoImage(file='previous.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_img, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_img, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_img, borderwidth=0, command=next_music)
prev_btn = Button(control_frame, image=prev_btn_img, borderwidth=0, command=prev_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
prev_btn.grid(row=0, column=0, padx=7, pady=10)



root.mainloop()