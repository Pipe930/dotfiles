
from keys import SpecialKeys
from libqtile.config import Group, Key
from libqtile.lazy import lazy
from keys import keys

## List the icons
list_icons = ["󰣇", "󰈹", "", "", "", "", "󰙯"]


groups = [Group(i) for i in list_icons]

## Groups ##
for i, group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [SpecialKeys.META.value],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [SpecialKeys.META.value, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),

        ]
    )
