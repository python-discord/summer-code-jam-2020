from subprocess import run

from the_htvms.runner.config import VMConfig
from the_htvms.runner.constants import MINIJAIL_VM_BASE_CONFIG, DISK_PATH


def start_vm(config: VMConfig) -> str:
    """
    Start a new VM using the provided config.

    The runner ID will be returned.
    """
    arguments = list(MINIJAIL_VM_BASE_CONFIG)

    # Add the rootfs
    arguments = ['-k', f'{DISK_PATH}/{config.attached_disks[0]},/,ext2'] + arguments

    # Add the disks to the VM
    if len(config.attached_disks) > 1:
        for i, disk in enumerate(config.attached_disks[1:]):
            arguments.extend(
                ('-b', f'{DISK_PATH}/{disk},/dev/fd{i}')
            )

    # Add the shell
    arguments.append(f'/bin/{config.default_shell}')

    # Start the VM
    run(('../build/process_watch', 'minijail0', *arguments))


def stop_vm(id_: str) -> bool:
    """
    Kill the VM with the provided ID.

    True is returned on success.
    """
    raise NotImplementedError
