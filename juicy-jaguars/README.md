<div align="center">
    <img src="https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/logo.png" width="200">
</div>
<br>
<div align="center">
    <a href="https://github.com/Juicy-Jaguars/summer-code-jam-2020/blob/master/LICENSE">
        <img src="https://img.shields.io/github/license/Juicy-Jaguars/summer-code-jam-2020">
    </a>
    <a href="http://charlottegaskell.ddns.net/">
        <img src="https://img.shields.io/uptimerobot/status/m785670380-00c12514d5483e1b64bba47f?label=website">
    </a>
</div>
<br>
<div align="center">
<h2>A web browser that runs in your browser, that processes webpages to make them reminiscent of the Web of the 80s and 90s.</h2>
</div>

## Table Of Contents

- [Features](#features)
- [Install](#installing)
  * [Windows](#on-windows)
  * [MacOS/Linux](#on-macoslinux)
  * [Manual Inspection](#manual-inspection)

### Features

#### A completely functional Window Manager
With Minimise, Maximise, full Z-Ordering and draggable windows!
![Window Manager Demo 1](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/win_manage_1.png)
![Window Manager Demo 2](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/win_manage_2.png)

#### A functioning Start Menu
Only the Settings Menu holds anything usable, but this allows you to change the Theme of the OS and the Wallpaper.
![Start Menu Demo](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/start_menu.png)

#### A fully working Web Browser
Internet Explorer works with the vast majority of Web Pages, meaning you can browse the Web just as you would in Chrome or Firefox.
However, there's a twist - and this is where Web95 really shines.
Every webpage you visit is parsed by Web95's server, to make it really feel like its from the 90s!
Fonts, images, colours and more are processed, giving the Web a retro overhaul as you browse.
And since all this is done programatically, it will work on almost any webpage.
![IE Demo 1](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/ie_1.png)
Search with Google, Bing and more;
![IE Demo 2](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/ie_2.png)
Check the news;
![IE Demo 3](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/ie_3.png)
Download the latest version of Python;
![IE Demo 4](https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/src/demos/ie_4.png)
Even watch YouTube Videos!

#### Easter Eggs...
If you look close enough, maybe you'll find one of Web95's hidden Easter Eggs!

### Installing

To install and run Web95, you must have Python 3.8 installed and have Pip installed and on your PATH.

#### On Windows:

```shell
curl https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/setup.py > setup.py && python setup.py install
```

When installing on Windows make sure that your default python version on PATH is Python 3.8.

#### On MacOS/Linux:

```shell
curl https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/setup.py > setup.py; python3 setup.py install
```

#### Manual Inspection

You can the inspect `setup.py` script before running it.

```shell
curl https://raw.githubusercontent.com/Juicy-Jaguars/summer-code-jam-2020/master/juicy-jaguars/setup.py > setup.py
python setup.py install         # Windows
python3 setup.py install        # Mac/Linux
```

**Windows:** `python setup.py install` **Mac/Linux:** `python3 setup.py install`