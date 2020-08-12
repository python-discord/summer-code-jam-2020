# Maniacal Moths

## Newsly
With the theme for the codejam being 'Early Internet', Newsly is an app that takes care of your Early(morning) Internet usage.

Essentially, Newsly is a news-aggregator, which gathers the latest trending articles from (almost) every website and has support for a plethora of languages and countries.  
The articles are then summarized and categorized, with options for detailed-reading available as well.

Newsly heavily relies on two fantastic APIs:  
1) [NewsCatcher API](https://newscatcherapi.com/)
2) [NewsPaper3k](https://pypi.org/project/newspaper3k/)

## Requirements
Python >= 3.8  
Django >= 3.0

## Installation
1) Clone this repository locally
2) Use the package manager [pip](https://pip.pypa.io/en/stable/) to install newspaper3k.

```bash
pip install newspaper3k
```

## Usage
After cloning the repository, open your anaconda terminal and navigate to the root directory.
```python
> cd cloned_folder\newsly
> python manage.py runserver
```
Then open a browser and head to [http://127.0.0.1:8000/about](http://127.0.0.1:8000/about)

##### Sidenote
For the judges/reviewers/people who are going to use the app, please read [Sidenotes.md](https://github.com/hot9cups/summer-code-jam-2020/blob/master/maniacal-moths/Sidenotes.md) before proceeding.

## License
[MIT](https://choosealicense.com/licenses/mit/)