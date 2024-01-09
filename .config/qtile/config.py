##############################################
### QTILE CONFIGURATION FILE OF FELIPE SANCHEZ ###
#
#     ██████     █████     ███  ████          
#   ███░░░░███  ░░███     ░░░  ░░███          
#  ███    ░░███ ███████   ████  ░███   ██████ 
# ░███     ░███░░░███░   ░░███  ░███  ███░░███
# ░███   ██░███  ░███     ░███  ░███ ░███████ 
# ░░███ ░░████   ░███ ███ ░███  ░███ ░███░░░  
#  ░░░██████░██  ░░█████  █████ █████░░██████ 
#    ░░░░░░ ░░    ░░░░░  ░░░░░ ░░░░░  ░░░░░░  
# ~/.config/qtile/config.py
 
import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, widget
from libqtile.config import Key, Group, Screen
from keys import keys, SpecialKeys
from layouts import layouts, floating_layout
from colors import theme
from groups import groups
from screens import screens
from mouse import mouse
from widgets import widgets, extension_defaults, widget_defaults


bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wl_input_rules = None

wmname = "LG3D"

## AUTOSTART
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
