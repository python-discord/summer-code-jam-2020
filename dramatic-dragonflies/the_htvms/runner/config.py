from dataclasses import dataclass
from typing import List


@dataclass
class VMConfig:
    """Dataclass representing the config a VM."""
    default_shell: str
    attached_disks: List[str]
