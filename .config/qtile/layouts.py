
from libqtile import layout
from libqtile.config import Match

## Layout Themes ##
layout_theme = {"border_width": 2,
                "margin": 6,
                "border_focus": "89bdc5",
                "border_normal": "d56d77",
                "margin_on_single": 6
                }

## Layouts ##
layouts = [
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Matrix(**layout_theme),
    #layout.Floating(**layout_theme),
    #layout.Tile(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

## Rules Floating Layouts ##
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry 
    ],
    border_focus = "#89bdc5"
)
