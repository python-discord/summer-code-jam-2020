# Disk settings
DISK_PATH = '/var/htvms/disks'
DISK_ROM_SIZE = '350M'
DISK_BLANK_SIZE = '50M'

DISK_STAGING_PATH = '/var/htvms/disk_staging'
DISK_ROM_PATH = '/rom'

VM_MAX_RAM = 1073741824  # 1Gb

MINIJAIL_VM_BASE_CONFIG = (
    '-b', '/build/boot,/boot,0',  # Add ro boot folder
    '-d',  # Base /dev folder
    '-e',  # New network space
    '-p',  # New PID namespace
    '-P', '/var/empty',  # Pivot to empty chroot
    '-R', f'RLIMIT_AS,{VM_MAX_RAM},{VM_MAX_RAM}',  # Limit memory
    '-R', 'RLIMIT_NPROC,90,100',  # Limit processes
    '-t',  # Mount tmpfs
    '--uts=htvm',  # Hostname
    '/bin/bash', '-c', 'bash'  # Hacky bash invocation
)
