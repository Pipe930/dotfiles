## Dotfiles & Config

# Descripción

Este es un repositorio de mi configuración y entorno de escritorio de Arch Linux. Utiliza un gestor de ventanas tipo tiling, que es qtile y está escrito en Python. Supongo que, si quieres instalarte este entorno de escritorio, sabes manejarte con sistemas operativos basados en GNU/Linux y su línea de comandos (BASH). También asumiré que sabes cómo funcionan los gestores de ventanas tipo tiling. Dicho esto, ahora vamos a proceder a instalar el entorno de escritorio.

# Instalación de Arch Linux

Para poder empezar con la instalación del entorno debe ser justo después de que hayas instalado el sistema operativo Arch Linux, en su wiki oficial **[Wiki Arch Linux](https://wiki.archlinux.org/title/Installation_guide)**, te índica como tienes que instalar este sistema operativo, pero no te índica qué hacer después de haber ingresado una constraseña al superusuario, donde tendrías que instalar un gestor de arranque del sistema, pero antes de eso debemos comprobar si tenemos internet, instalando y activando el siguiente paquete:

```bash
sudo pacman -S networkmanager
systemctl enable NetworkManager
```

Después de haber instalado y habilitado el paquete de `networkmanager`, instalaremos el gestor de arranque del sistema **[Grub](https://wiki.archlinux.org/title/GRUB)**, así es como se instalaría en hardware actual:

```bash
sudo pacman -S grub efibootmgr
grub-install --efi-directory=/boot/efi --bootloader-id=GRUB --target=x86_x64-efi --removable
grub-mkconfig -o /boot/grub/grub.cfg
```

> [!NOTE]
> En el comando `grub-install`, el último argumento indica que si tienes un gestor de arranque ya instalado, lo eliminará, si es la primera vez, quita el argumento `--removable`.

Ahora create un usuario:

```bash
useradd -m -s /bin/bash (username)
passwd (username)
usermod -aG wheel (username)
```

Para poder tener privilegios de superusuario, debemos configurar un archivo que está en la ruta `/etc/sudoers` con un editor de texto, en este caso, con nano, descomentando la siguiente línea:

```bash
sudo nano /etc/sudoers

## Uncomment to allow members of group wheel to execute any command
# %wheel ALL=(ALL) ALL
```

Ahora reinicia el equipo:

```bash
exit
umount -R /mnt
reboot
```

Ya que se haya reiniciado el PC, inicia sesión con el usuario y contraseña que creaste. Ahora tienes instalado Arch Linux, si es tu primera vez, ¡felicidades!. El internet debería funcionar correctamente, pero esto solo sucede si estás conectado por cable a través de Ethernet. Si estás en un portátil o tienes una tarjeta de red inalámbrica, utilizaremos el comando **[nmcli](https://wiki.archlinux.org/title/NetworkManager#Usage)** para poder conectarnos a una red de manera inalámbrica, para poder conectarse a una red wifi debes utilizar los siguientes comandos:

```bash
# Lista todas las redes disponibles
nmcli device wifi list
# Para conectarse a una red wifi
nmcli device wifi connect SSID_or_BSSID password PASSWORD
```

Listo ahora que tenemos el sistema operativo limpio y con internet, ahora procederemos a instalar el entorno de escritorio, lo ultimo que tenemos que hacer antes de instalar el entorno es actualizar el sistema e instalar **[Xorg](https://wiki.archlinux.org/title/Xorg)**

```bash
sudo pacman -Syu
sudo pacman -S xorg
```

# Instalación de Alacritty

El terminal que yo utilizo es **[Alacritty](https://github.com/alacritty/alacritty)**, para poder instalar Alacritty, primero debemos tener el compilador de rust, que es el lenguaje que esta creado Alacritty, ingresando el siguiente comando:

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Después de haberlo instalado debes tener una variable de entorno para poder utilizar los comandos de rust, para hacerlo ingresa la siguiente línea:

```bash
$HOME/.cargo/env
```

Ahora comprobamos si tenemos rust instalado con el siguiente comando:

```bash
rustup update stable
```

Ahora que tenemos el compilador de rust instalado, procederemos a clonar el repositorio de alacritty con el siguiente comando:

```bash
mkdir -p ~/Desktop/repos
cd ~/Desktop/repos

git clone https://github.com/alacritty/alacritty.git -b v0.12.3 --single-branch
```

Ahora que tenemos el repositorio clonado en el equipo, necesitamos instalar algunas dependencias que necesita el terminal para que pueda ser compilado, las cuales son las siguientes:

```bash
sudo pacman -S cmake freetype2 fontconfig pkg-config make libxcb libxkbcommon python
```

Ahora que tenemos las dependencias instaladas vamos a compilar el proyecto, primero debes estar dentro de la carpeta del proyecto donde lo hayas clonado, posteriormente tienes que ingresar el siguiente comando:

```bash
cargo build --release
```

Comenzará a compilar el programa e instalarlo. Una vez que haya finalizado el proceso de compilación e instalación de Alacritty correctamente, ejecutamos el siguiente comando para verificar si todo salió bien. Si aparece un texto extenso, significa que se instaló correctamente:

```bash
infocmp alacritty
```

Ahora que tenemos Alacritty instalado debemos añadir algunas configuraciones, con los siguientes comandos configuraremos la entrada de escritorio para Alacritty para que podamos ejecutarlo sin ningun problema:

```bash
sudo cp target/release/alacritty /usr/local/bin
sudo cp extra/logo/alacritty-term.svg /usr/share/pixmaps/Alacritty.svg
sudo desktop-file-install extra/linux/Alacritty.desktop
sudo update-desktop-database
```

> [!NOTE]
> Si el comando `desktop-file-install` no te funciona, tienes que instalar un paquete llamado `desktop-file-utils`

Y por ultimo instalaremos el **Manual Page**, con los siguientes comandos:

```bash
sudo mkdir -p /usr/local/share/man/man1
gzip -c extra/alacritty.man | sudo tee /usr/local/share/man/man1/alacritty.1.gz > /dev/null
gzip -c extra/alacritty-msg.man | sudo tee /usr/local/share/man/man1/alacritty-msg.1.gz > /dev/null
```

Listo ahora tenemos el terminal Alacritty instalado en nuestro Arch Linux.

# Gestor de Inicio de Sesion y Gestor de Ventanas

El gestor de ventanas que uso es [qtile](https://qtile.org), que es un gestor de ventanas de tipo tiling escrito en python, para instalar el gestor de ventanas en arch linux tenemos que utilizar el sistema de paquetes pacman, con el siguiente comando:

```bash
sudo pacman -S qtile
```

Ahora que tenemos instalado qtile tenemos que instalar un gestor de inicio de sesion [lightdm](https://wiki.archlinux.org/title/LightDM), por que si no lo hacemos y reiniciamos el equipo mostrara el inicio de sesion por terminal, para ello vamos a instalarlo con el siguiente comando:

```bash
sudo pacman -S lightdm lightdm-gtk-greeter
```

Activamos el servisio de *lightdm* y reiniciar el equipo, iniciara con el gestor de inicio de sesion *lightdm*:

```bash
sudo systemctl enable lightdm
reboot
```

# Fuentes

Para instalar unas fuentes más descentes que no sean las por defecto que trae el sistema operativo, con el siguiente comando instalaremos unas fuentes:

```bash
sudo pacman -S ttf-dejavu ttf-liberation noto-fonts
```

Para listar todas las fuentes que tienes instaladas:

```bash
fc-list
```

# Configuración de Qtile

Para la configuración de qtile tendras una configuración por defecto, deberías conocer algunos atajos de teclado que vienen por defecto que son los siguientes:

| Atajo                | Acción                              |
| -------------------- | ----------------------------------- |
| **mod + enter**      | abrir terminal                      |
| **mod + k**          | ventana siguiente                   |
| **mod + j**          | ventana anterior                    |
| **mod + w**          | cerrar ventana                      |
| **mod + [12345678]** | ir al espacio de trabajo [12345678] |
| **mod + ctrl + r**   | reiniciar qtile                     |
| **mod + ctrl + q**   | cerrar sesión                       |

La distribución de teclado estará en ingles, para poder cambiarlo tienes que ingresar el siguiente comando:

```bash
# Teclado Latinoamerica
setxkbmap latam

# Teclado España
setxkbmap es
```

Ahora para poder utilizar mi configuración de qtile, tienes que clonar mi repositorio [dotfiles](https://github.com/Pipe930/dotfiles), en la carpeta de tu usuario que creaste al momento de instalar arch linux, muevete a la carpeta, para poner mi configuración, tienes que mover la carpeta qtile que esta dentro de la carpeta .config, tienes que moverlo a la siguiente ruta:

```bash
# Primero borramos la carpeta de la configuración por defecto
rm -dir ~/.config/qtile

# Movemos la carpeta con mi configuración al lugar donde borramos la carpeta anterior
mv ./qtile ~/.config
```

¡Listo!, ahora ya tienes mi configuración de qtile en tu sistema, para que puedas ver los cambios tienes que reiniciar la configuración del sitema con la combinación de teclas `mod + ctrl + r`.

# Audio

En este momento, no tienes instalado un controlador de sonido para el audio de tu pc, para ello necesitamos [pulseaudio](https://wiki.archlinux.org/title/PulseAudio), y se recomienda instalar un programa grafico para el manejo del audio como [pavucontrol](https://archlinux.org/packages/extra/x86_64/pavucontrol/), para ello ejecuta el siguiente comando:

```bash
sudo pacman -S pulseaudio pavucontrol
```

Ahora que ya tenemos un controlador de sonido, Arch Linux ya por defecto está activado, pero puede que tengas que reiniciar para que *pulseaudio* arranque correctamente.

Ahora para poder subir y bajar el volumen del audio en mi configuración especifique las teclas para la subida, bajada y mute del audio.

```bash
# Volumen
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
)
```

Reinicia Qtile con **mod + control + r** y prueba los atajos. Si estás en un portátil, necesites controlar el brillo de tu pantalla, para ello instalaremos [brightnessctl](https://archlinux.org/packages/extra/x86_64/brightnessctl/)

```bash
sudo pacman -S brightnessctl
```

Y los atajos del teclados son los siguientes:

```bash
# Brillo
Key(
    [], 
    "XF86MonBrightnessUp", 
    lazy.spawn("brightnessctl set +10%")
), 
Key(
    [], 
    "XF86MonBrightnessDown", 
    lazy.spawn("brightnessctl set 10%-")
)
```

# Monitores

Si tienes varios monitores, seguramente quieras utilizarlos todos, para ello tenemos xrandr:

```bash
# Lista todas las salidas y resoluciones disponibles
xrandr
# Formato común para un portátil con monitor extra
xrandr --output eDP-1 --primary --mode 1920x1080 --pos 0x1080 --output HDMI-1 --mode 1920x1080 --pos 0x0
```

Ahora bien si no quieres especificar y calcular los pixeles puedes instalar [arandr](https://archlinux.org/packages/extra/x86_64/brightnessctl/) para poder configurar las pantallas a travez de una interfaz grafica:

```bash
sudo pacman -S arandr
```

Ábrela con rofi, te deberian salir todas tus pantallas, puedes configurar la resolución, cual es la principal, etc.

Para un sistema con múltiples monitores deberías crear una instancia de Screen por cada uno de ellos en la configuración de Qtile.

Encontrarás una lista llamada screens en la configuración de Qtile que contiene solo un objeto inicializado con una barra en la parte de abajo. Dentro de esa barra puedes ver los widgets con los que viene por defecto.

Añade tantas pantallas como necesites y copia-pega los widgets, más adelante podrás personalizarlos. Ahora puedes volver a arandr, darle click en "apply" y reiniciar el gestor de ventanats.

Con esto tus monitores deberían funcionar.