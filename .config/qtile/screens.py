

# Multimonitor support

from libqtile.config import Screen
from libqtile import bar
from widgets import widgets
from colors import theme


def status_bar(widgets):

    bar_size = 30
    bar_opacity = 0.9
    return bar.Bar(widgets, background=theme["background"], size=bar_size, opacity=bar_opacity)

def _main_screen():
    return Screen(top=status_bar(widgets))


screens = [
        _main_screen()
        ]
