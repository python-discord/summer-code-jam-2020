from the_htvms.runner.config import VMConfig


def start_vm(config: VMConfig) -> str:
    """
    Start a new VM using the provided config.

    The runner ID will be returned.
    """
    raise NotImplementedError


def stop_vm(id_: str) -> bool:
    """
    Kill the VM with the provided ID.

    True is returned on success.
    """
    raise NotImplementedError
