 
from libqtile import widget
from colors import theme

icon_separator = ""
icon_separator_2 = ""

# Create Separator Group
def separator_group(group_color1, group_color2):

    return widget.TextBox(
                text = icon_separator_2,
                padding = 0,
                fontsize = 30,                
                background = group_color1,
                foreground = group_color2
            )

# Create Separator
def separador():

    return widget.Sep(
            linewidth = 0,
            padding = 4,
            foreground = theme["foreground"],
            background = theme["background"]
            )

# Create Group Widget
def create_group(icon, color, size, padding):

    return widget.TextBox(
            text = icon,
            foreground = theme["foreground"],
            background = color,
            fontsize = size,
            padding = padding
            )

## Widgets ##
widgets = [

                # Desktops
                widget.GroupBox(
                    active = theme["green"],
                    font='UbuntuMono Nerd Font Mono',
                    fontsize = 40,
                    margin_y = 3,
                    padding_x = 6,
                    disable_drag = True,
                    #rounded = False,
                    highlight_method = "block",
                    inactive = theme["cyan"],
                    this_current_screen_border = theme["purple"],
                    this_screen_border = theme["purple"],
                    urgent_alert_method = "block",
                    urgent_border = theme["purple"],
                    borderwidth = 4
                    ),
                widget.Prompt(),
                widget.WindowName(
                    foreground = theme["foreground"],
                    background = theme["background"],
                    ),

                ## Group Check Updates
                separator_group(theme["background"], theme["magenta"]),
                create_group("", theme["magenta"], 20, 7), # Icon: nf-fa-download
                widget.CheckUpdates(
                    background = theme["magenta"],
                    colour_have_updates = theme["green"],
                    colour_no_updates = theme["red"],
                    no_update_string = '0',
                    display_format = '{updates}',
                    update_interval = 1800,
                    custom_command = 'arch_checkupdates',
                ),

                ## Group Net
                separator_group(theme["magenta"], theme["red"]),
                create_group("", theme["red"], 20, 5), # Icon: nf-fa-feed
                widget.Net(
                    foreground = theme["foreground"],
                    background = theme["red"],
                    interface = "wlp3s0",
                    format = "{down}  {up}",
                    use_bits = "true",
                    padding = 6
                ),

                ## Group Memory
                separator_group(theme["red"], theme["blue"]),
                create_group("󰍛", theme["blue"], 26, 3),
                widget.Memory(
                    foreground = theme["foreground"],
                    background = theme["blue"],
                    padding = 6
                    ),

                ## Group Clock
                separator_group(theme["blue"], theme["green"]),
                create_group("󰃰", theme["green"], 20, 5),
                widget.Clock(
                    format="%d/%m/%Y %I:%M",
                    background = theme["green"],
                    foreground = theme["foreground"]
                    ),

                ## Group Layouts
                separator_group(theme["green"], theme["orange"]),
                widget.CurrentLayoutIcon(
                    scale = 0.6,
                    padding = 0,
                    background = theme["orange"],
                    foreground = theme["foreground"]
                    ),
                widget.CurrentLayout(
                    padding = 6,
                    background = theme["orange"],
                    foreground = theme["foreground"]
                    ),
                
                ## Icons the programs second plane
                separator_group(theme["orange"], theme["background"]),
                widget.Systray(
                   icon_size = 20
                )
]

widget_defaults = dict(
    font="Hack Nerd Font",
    fontsize=12,
    padding=4
)

extension_defaults = widget_defaults.copy()
