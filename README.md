# 🎵 Spondify – Desktop Music Player (Python)

**Spondify** is a lightweight desktop music player built using **Python**, combining **Tkinter** for the graphical user interface and **Pygame** for audio playback.
The project focuses on demonstrating **GUI design**, **event-driven programming**, and **media handling** in Python.

---

## 🚀 Project Overview

Spondify allows users to:

* Select a local folder containing audio files
* Automatically load and list supported songs
* Play, pause, and navigate through tracks using intuitive controls

This project was built as a hands-on exploration of Python GUI frameworks and multimedia integration.

---

## ✨ Features

* 📂 **Folder-based music loading**
* 🎶 Supports `.mp3` and `.wav` files
* ▶️ Play / ⏸ Pause functionality
* ⏭ Next & ⏮ Previous track navigation
* 🔊 Adjustable volume (default set to 70%)
* 🖥 Simple and clean Tkinter-based UI
* 🎛 Menu-driven organization system

---

## 🛠 Tech Stack

* **Python**
* **Tkinter** – GUI framework
* **Pygame (Mixer)** – Audio playback engine
* **OS module** – File system interaction

---

## 🧩 Application Architecture

### Key Components

* **Tkinter Root Window**

  * Main application window
  * Menu bar and song list UI
* **Pygame Mixer**

  * Handles loading and playing audio
* **Listbox Widget**

  * Displays loaded songs
  * Tracks current selection
* **Control Buttons**

  * Play, Pause, Next, Previous (image-based buttons)

---

## 📂 File Structure

```
Spondify/
│
├── SpondifyMusicPlayer.py   # Main application code
├── play.png                 # Play button icon
├── pause.png                # Pause button icon
├── next.png                 # Next track icon
├── previous.png             # Previous track icon
└── README.md
```

---

## ▶️ How It Works

1. User selects a directory using **Select Folder**
2. All `.mp3` and `.wav` files are detected and loaded
3. Songs are displayed in a scrollable list
4. Controls allow playback and navigation
5. Pygame handles audio streaming in the background

Note: Pygame has some issues with playing `.mp3` files but no such issues with `.wav` or `.ogg` file format.

---

## 🧠 Key Programming Concepts Demonstrated

* Event-driven GUI programming
* State management (`paused`, `current_song`)
* File I/O and directory traversal
* Media playback integration
* Modular function design
* Exception handling for edge cases

---

## 📦 Installation & Usage

### Prerequisites

Make sure Python is installed, then install Pygame:

```bash
pip install pygame
```

### Run the Application

```bash
python SpondifyMusicPlayer.py
```

Ensure the image assets (`play.png`, `pause.png`, etc.) are present in the same directory.

---

## ⚠️ Known Limitations

* No playlist saving/loading
* No progress bar or time tracking
* Single-folder music loading only
* UI styling kept minimal by design

---

## 🔮 Future Improvements

* Add seek bar and time display
* Playlist management
* Shuffle and repeat modes
* Keyboard shortcuts
* Improved UI styling (custom themes)

---

## 👤 Author

**Spondan Bandyopadhyay**

**Interests:** Python Development · GUI Systems · Machine Learning

---
