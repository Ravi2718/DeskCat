# 🐱 DeskCat:

Bring your desktop to life with your adorable animated cat companion! DeskCat is a playful app built in Python with PySide6, entertaining you with lively actions and moods as you work.

## ✨ Features

- 🎬 **Animated Cat**: Walks, runs, sleeps, and dances happily across your desktop.
- 🙀 **Angry Reaction**: Grab and drag the cat to see it get "angry" (but it forgives you quickly).
- 😴 **Mood Changes**: Cat switches style between walking, running, sleeping, and happy at random intervals.
- 🖱️ **Easy Interaction**:
  - Drag to move your cat around.
  - Double right-click the cat 🐾 to quickly close the app.
- ⌨️ **Keyboard Shortcuts**:
  - Press `Ctrl+Q` to quit instantly.
- 🖼️ **Always on Top**: Your DeskCat stays visible above other windows.

## 🖥️ Requirements

- Python 3.7 or newer
- PySide6

Install with:
```bash
pip install PySide6
```

## 📁 Project Structure

```
DeskCat/
  ├── cat_states/
  │     ├── walking/
  │     │     ├── 1.png
  │     │     ├── 2.png
  │     │     └── ...
  │     ├── running/
  │     ├── sleeping/
  │     ├── happy/
  │     └── angry/
  ├── main.py
```
- **cat_states/**: Subfolders for each mood, each containing PNG frames.
- **main.py**: Main application script.

## 🛠️ How to Run

### 🧪 Run from Source

```bash
pip install -r requirements.txt
```
```bash
python deskcat.py
```

### 🐧 Package to `.exe` (Windows)

1. Make sure you have `pyinstaller`:

   ```bash
   pip install pyinstaller
   ```

2. Then run:

   ```bash
   pyinstaller --onefile --noconsole --icon=icon.ico --add-data "cat_states;cat_states" deskcat.py
   ```

3. Find your `.exe` inside the `dist/` folder.

---

3. **Have Fun!**
   - Click and drag the cat 😾 — it gets "angry" while dragged.
   - Watch it randomly change moods 😺 throughout the day.
   - Double right-click 🖱️ or hit `Ctrl+Q` to quit.
   - Your DeskCat always floats on top of other windows for maximum cuteness.

## 🧩 Extra Tips & Customization 🌟

- ✨ **Add More Moods:**  
  Create new folders (e.g., `playful`, `curious`) and update the `modes` list in `main.py` to add fresh moods for your DeskCat.

- ⚡ **Adjust Animation Speed:**  
  Change `target_size`, `step_size`, and interval variables in the script to fine-tune how your DeskCat acts.

- 🖌️ **Use Custom Sprites:**  
  Personalize your cat with your own PNGs in each mode folder!

- 🔄 **Package for Friends:**  
  Use tools like PyInstaller to turn DeskCat into a standalone executable that you can share.


## 🧩 Customization

* 🐾 **Add New Moods**:
  Create new folders in `cat_states/` and update the `modes` list in `deskcat.py`.

* ⚡ **Animation Speed**:
  Modify `animation_interval` and `step_size` values in the script.

* 🎨 **Use Your Own Sprites**:
  Replace PNGs inside each folder to make a custom pet.

---

## 🐞 Troubleshooting

* **Images Not Showing?**
  Double-check that all mood folders have PNG files.

* **Exe Crashes?**
  Make sure you're using correct `--add-data` paths for Windows (`;`) or Linux/macOS (`:`).

* **Can't Quit the App?**
  Use double right-click or `Ctrl+Q`.

---

## 📄 License

[MIT License](LICENSE)

---

## 👨‍💻 Author

Created by  Ravi
Feel free to fork, customize, and share your version of DeskCat!



