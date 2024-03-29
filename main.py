from ursina import *
from main_menu import MainMenu
from PyQt5.QtWidgets import *
import sys, os, pyautogui, ursina, pyqtgraph, PyQt5

window_size = pyautogui.size()

Text.default_resolution = 1080 * Text.size
app = [Ursina(), QApplication(sys.argv)]

window.title = "Etri_1.2"
window.borderless = False
window.fullscreen = False
window.show_ursina_splash = True
window.cog_button.disable()

width, height = window_size

window.size = (width/ 1.5, height/1.5)
window.position = Vec2(width/80, height/8)

main_menu = MainMenu()

app[0].run()


