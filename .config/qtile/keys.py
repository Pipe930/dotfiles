import enum

from libqtile.config import Key, Click, Drag
from libqtile.utils import guess_terminal
from libqtile.lazy import lazy

class Arrows(enum.Enum):
    LEFT = "h"
    UP = "u"
    DOWN = "j"
    RIGHT = "k"

class SpecialKeys(enum.Enum):
    META = "mod4"
    ALT = "mod1"
    CTRL = "control"
    SHIFT = "shift"

terminal = guess_terminal()

## Keys ##
_keys_focus_layouts = [

    ## Switch between windows
    Key(
        [SpecialKeys.META.value], 
        Arrows.LEFT.value, 
        lazy.layout.left(), 
        desc="Move focus to left"
    ),
    Key(
        [SpecialKeys.META.value], 
        Arrows.RIGHT.value, 
        lazy.layout.right(), 
        desc="Move focus to right"
    ),
    Key(
        [SpecialKeys.META.value], 
        Arrows.DOWN.value, 
        lazy.layout.down(), 
        desc="Move focus down"
    ),
    Key(
        [SpecialKeys.META.value], 
        Arrows.UP.value, 
        lazy.layout.up(), 
        desc="Move focus up"
    ),
    Key(
        [SpecialKeys.META.value], 
        "space", 
        lazy.layout.next(), 
        desc="Move window focus to other window"
    )
]

_keys_move_layouts = [

    ## Move windows between left/right columns or move up/down in current stack.
    ## Moving out of range in Columns layout will create new column.
    Key(
        [SpecialKeys.META.value, SpecialKeys.SHIFT.value], 
        Arrows.LEFT.value, 
        lazy.layout.shuffle_left(), 
        desc="Move window to the left"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.SHIFT.value], 
        Arrows.RIGHT.value, 
        lazy.layout.shuffle_right(), 
        desc="Move window to the right"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.SHIFT.value], 
        Arrows.DOWN.value, 
        lazy.layout.shuffle_down(), 
        desc="Move window down"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.SHIFT.value], 
        Arrows.UP.value, 
        lazy.layout.shuffle_up(), 
        desc="Move window up"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.SHIFT.value],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    )
]

_keys_resive_layouts = [

    ## Grow windows. If current window is on the edge of screen and direction
    ## will be to screen edge - window would shrink.
    Key(
        [SpecialKeys.META.value, SpecialKeys.CTRL.value], 
        Arrows.LEFT.value, 
        lazy.layout.grow_left(), 
        desc="Grow window to the left"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.CTRL.value], 
        Arrows.RIGHT.value, 
        lazy.layout.grow_right(), 
        desc="Grow window to the right"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.CTRL.value], 
        Arrows.DOWN.value, 
        lazy.layout.grow_down(), 
        desc="Grow window down"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.CTRL.value], 
        Arrows.UP.value, 
        lazy.layout.grow_up(), 
        desc="Grow window up"
    ),
    Key(
        [SpecialKeys.META.value], 
        "n", 
        lazy.layout.normalize(), 
        desc="Reset all window sizes"
    ), 

    ## Key change layouts
    Key(
        [SpecialKeys.META.value, SpecialKeys.ALT.value], 
        "Tab", 
        lazy.next_layout(), 
        desc="Toggle between layouts"
    )
]

_keys_shortcuts = [

    ## Open Terminal
    Key([SpecialKeys.META.value], "Return", lazy.spawn("alacritty"), desc="Launch terminal"),

    ## Open File Browsers
    Key([SpecialKeys.META.value], "t", lazy.spawn(terminal + " -e ranger"), desc="Launch the tui file manger(ranger) in the default terminal"),

    ## Open Browser
    Key([SpecialKeys.META.value], "f", lazy.spawn("firefox"), desc="Launch browser"),

    ## Open Rofi
    Key([SpecialKeys.META.value], "b", lazy.spawn("rofi -show drun"), desc="Launch rofi"),

    ## Open Discord
    Key([SpecialKeys.META.value], "d", lazy.spawn("discord"), desc="Launch Discord"),    

    ## Kill Window
    Key(
        [SpecialKeys.META.value], 
        "q", 
        lazy.window.kill(), 
        desc="Kill focused window"
    ),

    ## Restart Qtile
    Key(
        [SpecialKeys.META.value, SpecialKeys.CTRL.value], 
        "r", 
        lazy.reload_config(), 
        desc="Reload the config"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.CTRL.value], 
        "q", 
        lazy.shutdown(), 
        desc="Shutdown Qtile"
    ),
    Key(
        [SpecialKeys.META.value], 
        "r", 
        lazy.spawncmd(), 
        desc="Spawn a command using a prompt widget"
    )
]

_keys_media = [

    ## Volume up, down and mute key configuration
    Key(
        [], 
        "XF86AudioRaiseVolume", 
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")
    ),
    Key(
        [], 
        "XF86AudioLowerVolume", 
        lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")
    ),
    Key(
        [], 
        "XF86AudioMute", 
        lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")
    ),

    ## Media Keys
    Key(
        [],
        "XF86AudioPlay",
        lazy.spawn("playerctl play-pause"),
        desc="Play/Pause music",
    ),
    Key(
        [],
        "XF86AudioNext",
        lazy.spawn("playerctl next"),
        desc="Next music",
    ),
    Key(
        [],
        "XF86AudioPrev",
        lazy.spawn("playerctl previous"),
        desc="Previous music",
    ),

    ## Configuration of keys to raise and lower the brightness of the screen
    Key(
        [], 
        "XF86MonBrightnessUp", 
        lazy.spawn("brightnessctl set +10%")
    ), 
    Key(
        [], 
        "XF86MonBrightnessDown", 
        lazy.spawn("brightnessctl set 10%-")
    ),

    ## Screenshots
    Key(
        [SpecialKeys.META.value], 
        "s", lazy.spawn("scrot"), 
        desc="take a screenshot"
    ),
    Key(
        [SpecialKeys.META.value, SpecialKeys.SHIFT.value], 
        "s", 
        lazy.spawn("scrot -s"), 
        desc="take a screenshot"
    )
]

keys = _keys_focus_layouts + _keys_move_layouts + _keys_resive_layouts + _keys_shortcuts + _keys_media


