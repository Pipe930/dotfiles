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
> En el comando de `grub-install` el ultimo argumento indica que si tienes un gestor de arranque ya instalado lo eliminara, si es la primera vez quita el argumenro `--removable`