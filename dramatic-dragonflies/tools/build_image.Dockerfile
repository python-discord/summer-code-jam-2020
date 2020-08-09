FROM archlinux:20200705

WORKDIR /image
RUN pacman -Syy wget dos2unix --noconfirm
RUN wget http://cdimage.debian.org/mirror/archlinux/archive/iso/arch-0.1-full-i686.iso -O ./arch.iso \
    -q --show-progress --progress=bar:force 2>&1

ENTRYPOINT ["./make_image.sh"]
ADD ./make_image.sh .
RUN dos2unix make_image.sh
