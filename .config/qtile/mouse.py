
from libqtile.config import Click, Drag
from libqtile.lazy import lazy
from keys import SpecialKeys

## Mouse ##
mouse = [
    Drag([SpecialKeys.META.value], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([SpecialKeys.META.value], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([SpecialKeys.META.value], "Button2", lazy.window.bring_to_front())
]
