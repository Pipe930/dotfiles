#!/bin/sh


# Configuracion del teclado
setxkbmap latam &

picom &

nitrogen --restore &

# Iconos

udiskie -t &

nm-applet &

volctl &

cbatticon &
