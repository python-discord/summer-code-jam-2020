
# ANSI Color codes for the terminal, make sure to reset after using
COLOR = {
    'reset': '\x1b[0m',
    'black': '\x1b[30m',
    'red': '\x1b[31m',
    'green': '\x1b[32m',
    'yellow': '\x1b[33m',
    'blue': '\x1b[34m',
    'magenta': '\x1b[35m',
    'cyan': '\x1b[36m',
    'white': '\x1b[37m',
    'brightBlack': '\x1b[1;30m',
    'brightRed': '\x1b[1;31m',
    'brightGreen': '\x1b[1;32m',
    'brightYellow': '\x1b[1;33m',
    'brightBlue': '\x1b[1;34m',
    'brightMagenta': '\x1b[1;35m',
    'brightCyan': '\x1b[1;36m',
    'brightWhite': '\x1b[1;37m',
}


def colorize(color, text):
    """Prefixes an ANSI color escape and resets color after."""

    return COLOR[color] + text + COLOR['reset']
