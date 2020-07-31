# Codestyle of this project

All files should be indented with spaces to a tab-stop of 4.

## Python

**All** python code is formatted with [black](https://github.com/psf/black), with maximum line length set to 78.

Cases where black's style is ambiguous:

- Strings broken across multiple lines should be broken only after a space.
    Each line should use as many characters as possible without going over 78.

    For example,

    ```python
    my_string = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eget consectetur mi, et consectetur id."
    ```

    should be formatted as

    ```python
    my_string = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eget "
        "consectetur mi, et consectetur id."
    )
    ```

- Very long strings containing no spaces (any string which, by itself, brings
    the line's length to >78 characters) should be split such that the total
    line length is 78 characters; additionally, there should be a split immediately preceding and following the string.

    For example,

    ```python
    my_string = "Hello, I am a string. Supercalifragilistic_expialidocious_I_need_a_longer_token_that's_really_quite_atrocious. Another sentence."
    ```

    should be formatted as

    ```python
    my_string = (
        "Hello, I am a string. "
        "Supercalifragilistic_expialidocious_I_need_a_longer_token_that's_really_"
        "quite_atrocious. "
        "Another sentence."
    )
    ```

- Strings broken across multiple lines should all use the same prefix, even if
    it isn't needed for every string.

    For example,

    ```python
    my_string = f"My long string with {f-string} expressions in it {that} don't all need the prefix but do need wrapping."
    ```

    should be formatted as

    ```python
    my_string = (
        f"My long string with {f-string} expressions in it {that} don't all need "
        f"the prefix but do need wrapping."
    )
    ```

## HTML

- Due to the early internet theme, tags should be in UPPER CASE, like they
    were in many early sites
- One tag per line
- Singleton tags (`BR`, `IMG`, etc.) should use trailing slash with a space
    before it
- `BR` tags must *always* be followed by a newline, but should not be preceded by one.
- Multiline content must always be on a separate line from its tag
- Maximum line length: 78 characters

Example code conforming to this style

```html
<!DOCTYPE HTML>
<HTML>
    <HEAD>
        <TITLE>Page title</TITLE>
    </HEAD>
    <BODY>
        <P>
            Page content<BR />
            More page content
        </P>
        <P>Page content in a separate P tag</P>
    </BODY>
</HTML>
```
