# Dramatic Dragonflies

## Launch Arch Linux 0.1 in the cloud!

This service allows you to connect to VMs running Arch Linux 0.1 (from 2002) on our servers and connect to it from your browser! 

## How To

1. Create a new account
2. Login to your newly craeted account
3. Create a new VM
4. Press "Launch"
5. Enjoy!

## Running this service

Run the following commands in order to run the website:

```
./tools/build_image.sh  # A batch version is also available
docker-compose up
```
And that's it!

## Techical details

In reality, our VMs are closer to a Docker container than an actual VM. A bash instance is ran using the host kernel and isolated from the rest of the system using [minijail](https://github.com/google/minijail). See [runner](https://github.com/Akarys42/summer-code-jam-2020/tree/master/dramatic-dragonflies/the_htvms/runner) for more info.
