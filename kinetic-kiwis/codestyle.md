# Codestyle of this project

All files should be indented with a tab width of 4.

## Python

**All** python code is formatted with [black](https://github.com/psf/black), with default settings.

Cases where black's style is ambiguous:

- Strings broken across multiple lines should be broken only after a space;
    very long strings containing no spaces (any string which, by itself, brings
    the line's length to >88 characters) should be split such that the total
    line length is 88 characters; additionally, there should be a split immediately preceding the string.

    For example,

    ```python
    my_string = "hello I am a very long string. Supercalifragilistic_expialidocious_I_need_a_longer_token_that's_really_quite_atrocious"
    ```

    should be formatted as

    ```python
    my_string = (
        "hello I am a very long string. "
        "Supercalifragilistic_expialidocious_I_need_a_longer_token_that's_really_quite_atro"
        "cious"
    )
    ```
