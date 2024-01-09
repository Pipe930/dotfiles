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