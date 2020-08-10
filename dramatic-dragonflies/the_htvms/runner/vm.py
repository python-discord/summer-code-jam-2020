import os
import secrets
from subprocess import run

from the_htvms.runner.config import VMConfig
from the_htvms.runner.constants import MINIJAIL_VM_BASE_CONFIG, DISK_PATH, MINIJAIL_VM_EXECUTABLE, VM_RUNNER_PATH


def start_vm(config: VMConfig) -> str:
    """
    Start a new VM using the provided config.

    The runner ID will be returned.
    """
    arguments = list(MINIJAIL_VM_BASE_CONFIG)
    
    uid = secrets.token_hex(4)

    # Add the disks to the VM
    if len(config.attached_disks) > 1:
        for i, disk in enumerate(config.attached_disks[1:]):
            arguments.extend(
                ('-b', f'{DISK_PATH}/{disk},/dev/fd{i}')
            )

    # Mount the rootfs disk
    if not os.path.exists(f'{VM_RUNNER_PATH}/{uid}'):
        os.makedirs(f'{VM_RUNNER_PATH}/{uid}')
    run(
        ('mount', f'{DISK_PATH}/{config.attached_disks[0]}', f'{VM_RUNNER_PATH}/{uid}'),
        check=True
    )
    arguments.extend(('-P', f'{VM_RUNNER_PATH}/{uid}'))

    # Add the executable
    arguments.extend(MINIJAIL_VM_EXECUTABLE)

    # Start the VM
    return '../build/process_watch', 'minijail0', *arguments


def stop_vm(id_: str) -> bool:
    """
    Kill the VM with the provided ID.

    True is returned on success.
    """
    raise NotImplementedError
