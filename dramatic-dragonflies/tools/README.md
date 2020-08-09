# Utility Tools

Here is a short description of all the tools in this directory :

* `build_image.bat` / `build_image.sh` : Main script used to generate a ROM. 
It is booting up the `build_image.Dockerfile`, run `make_image.sh` inside and 
extract the generated `rom.tar.gz` file.

* `build_image.Dockerfile` : Simple container in charge of providing a reproducible 
build environment for the ROM. It is also downloading the Arch ISO.

* `make_image.sh` : Script ran inside the build container in order to generate the ROM.

* `process_watch` : opens a process in a pty and passes its stdio to it, allowing using
pipe based IPC while still getting the advantages of a pty
