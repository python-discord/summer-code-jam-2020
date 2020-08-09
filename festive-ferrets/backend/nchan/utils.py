def shorten_text(text: str, length: int) -> str:
    """
    Shorten text to length chars cut to last space or new line and add '...'

    :param text: Text to be shortened
    :type text: str
    :param length: Maximum text length after cut, not counting '...'
    :type length: int
    :return: Shortened text
    :rtype: str
    """
    short_text = text
    if len(short_text) > length:
        short_text = short_text[:length + 1]
        cut_index = max(short_text.rfind(' '), short_text.rfind('\n'))
        if cut_index != -1:
            short_text = short_text[:cut_index]
        short_text += '...'
    return short_text
