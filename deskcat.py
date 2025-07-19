import sys
import os
import random
from PySide6.QtGui import QShortcut
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QPixmap, QGuiApplication, QTransform, QMouseEvent, QKeySequence
from PySide6.QtCore import Qt, QTimer, QPoint

# -------------------------------
# SETTINGS
# -------------------------------
target_size = 50  # size of the cat image
step_size = 5
mode_switch_interval_range = (10000, 20000)  # in milliseconds
modes = ["walking", "sleeping", "running", "happy"]
mode = "walking"
last_mode = mode
frame_index = 0

# -------------------------------
# Auto-detect base folder
# -------------------------------
if getattr(sys, 'frozen', False):
    base_folder = os.path.join(sys._MEIPASS, "cat_states")
else:
    base_folder = os.path.join(os.path.dirname(__file__), "cat_states")

# -------------------------------
# Load frames for given mode
# -------------------------------
def load_frames(mode_name):
    folder = os.path.join(base_folder, mode_name)
    if not os.path.exists(folder):
        print(f"❌ Folder not found: {folder}")
        return []
    return sorted([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if f.endswith(".png")
    ])

frames = load_frames(mode)

# -------------------------------
# Qt Setup
# -------------------------------
app = QApplication(sys.argv)
screen = QGuiApplication.primaryScreen()
screen_geometry = screen.geometry()
screen_width = screen_geometry.width()
screen_height = screen_geometry.height()

# -------------------------------
# Cat QLabel (draggable)
# -------------------------------
class CatLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.drag_pos = QPoint()
        self.is_dragging = False

    def mousePressEvent(self, event: QMouseEvent):
        global last_mode, mode, frames, frame_index
        if event.button() == Qt.LeftButton:
            self.is_dragging = True
            self.drag_pos = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
            if mode != "angry":
                last_mode = mode
                mode = "angry"
                frames = load_frames("angry")
                frame_index = 0
                update_timer_interval()
                print("😾 Cat is angry!")

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.is_dragging:
            new_pos = event.globalPosition().toPoint() - self.drag_pos
            self.move(new_pos)

    def mouseReleaseEvent(self, event: QMouseEvent):
        global mode, frames, frame_index
        if event.button() == Qt.LeftButton:
            self.is_dragging = False
            if mode == "angry":
                mode = last_mode
                frames = load_frames(mode)
                frame_index = 0
                update_timer_interval()
                print(f"😺 Cat calmed down, back to: {mode}")

# -------------------------------
# Setup and show label
# -------------------------------
label = CatLabel()
x = 0
vertical_offset = 9 # offset from the bottom of the screen
y = screen_height - target_size + vertical_offset
direction = 1  # 1 = right, -1 = left
label.setGeometry(x, y, target_size, target_size)
label.show()

# Ctrl+Q = quit app
exit_shortcut = QShortcut(QKeySequence("Ctrl+Q"), label)
exit_shortcut.setContext(Qt.ApplicationShortcut)
exit_shortcut.activated.connect(app.quit)


# -------------------------------
# Animation + Movement
# -------------------------------
def update_timer_interval():
    if mode in ["walking"]:
        frame_timer.setInterval(80)
    elif mode == "running":
        frame_timer.setInterval(130)
    elif mode == "sleeping":
        frame_timer.setInterval(800)
    elif mode == "happy":
        frame_timer.setInterval(800)


def update_frame():
    global frame_index, x, direction

    if not frames:
        return

    pixmap = QPixmap(frames[frame_index]).scaled(
        target_size, target_size, Qt.KeepAspectRatio, Qt.SmoothTransformation
    )

    if direction == -1 and mode in ["walking", "running"]:
        pixmap = pixmap.transformed(QTransform().scale(-1, 1))

    label.setPixmap(pixmap)
    frame_index = (frame_index + 1) % len(frames)

    if mode in ["walking", "running"] and not label.is_dragging:
        speed = step_size * (2 if mode == "running" else 1)
        x = label.x() + (speed * direction)

        if x + target_size >= screen_width:
            x = screen_width - target_size
            direction = -1
        elif x <= 0:
            x = 0
            direction = 1

        label.move(x, label.y())

# -------------------------------
# Random Mode Switcher
# -------------------------------
def switch_mode():
    global mode, frames, frame_index, last_mode
    if mode == "angry":
        return

    new_mode = random.choice(modes)
    while new_mode == mode:
        new_mode = random.choice(modes)

    last_mode = mode
    mode = new_mode
    frames = load_frames(mode)
    frame_index = 0
    update_timer_interval()
    print(f"🎭 Switched to mode: {mode}")
    mode_timer.start(random.randint(*mode_switch_interval_range))

# -------------------------------
# Timers
# -------------------------------
frame_timer = QTimer()
frame_timer.timeout.connect(update_frame)
update_timer_interval()
frame_timer.start()

mode_timer = QTimer()
mode_timer.timeout.connect(switch_mode)
mode_timer.start(random.randint(*mode_switch_interval_range))

# === Exit == Right-Click Double Tap ===
def mouseDoubleClickEvent(self, event):
    if event.button() == Qt.RightButton:
        print("Exiting via right-click double tap.")
        app.quit()


# -------------------------------
# Run App
# -------------------------------
print("🐱 DeskCat is running!")
sys.exit(app.exec())
