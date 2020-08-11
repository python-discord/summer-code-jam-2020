import os
import secrets
from subprocess import run

from the_htvms.runner.constants import DISK_PATH, DISK_ROM_SIZE, DISK_BLANK_SIZE, DISK_STAGING_PATH, DISK_ROM_PATH


def create_disk(type_: str) -> str:
    """
    Create a new disk on the runner.

    Type can be either `blank` or `rom`.
    Return the disk ID.
    """
    # Check the validity of the type
    if type_ not in ('rom', 'blank'):
        raise ValueError(f'Invalid type {type_}')

    # Check that the disk folder exists
    if not os.path.exists(DISK_PATH):
        os.makedirs(DISK_PATH)

    # Generate a new UID
    uid = type_[0] + secrets.token_hex(4)

    # Use dd to fill up a new file
    size = DISK_ROM_SIZE if type_ == 'rom' else DISK_BLANK_SIZE
    path = f'{DISK_PATH}/{uid}'
    run(
        ('dd', 'if=/dev/zero', f'of={path}', f'bs={size}', 'count=1'),
        check=True
    )

    # Create the filesystem
    run(
        ('mkfs.ext2', path),
        check=True
    )

    # Copy ROM if needed
    if type_ == 'rom':
        # Check that the disk staging folder exists
        if not os.path.exists(DISK_STAGING_PATH):
            os.makedirs(DISK_STAGING_PATH)

        # Mount the disk in the staging folder
        run(
            ('mount', '-o', 'loop', path, DISK_STAGING_PATH),
            check=True
        )
        run(
            ('cp', '-a', f'{DISK_ROM_PATH}/.', DISK_STAGING_PATH),
            check=True
        )
        run(
            ('umount', DISK_STAGING_PATH),
            check=True
        )
    return uid


def delete_disk(id_: str) -> bool:
    """
    Delete the disk with the provided ID.

    True is returned on success.
    """
    try:
        os.remove(f'{DISK_PATH}/{id_}')
    except:  # rmtree doesn't define which exception it can raise ¯\_(ツ)_/¯
        return False
    return True
