# Sarcastic Sparrows

### Sparrow Capital
The year is 1995. The release of consumer-friendly browsers like Mosaic and Netscape are quickly making the internet a household name throughout the world. Venture capital firms are tossing money at any upstart tech company with a ".com" in their name. IPOs are being valuated in the hundreds of millions of dollars despite never turning a profit or releasing a successful product. The information age has dawned upon the new millenia and there is profit to be made... or is there?

Between approximately 1995 and 2000 the NASDAQ rose nearly 400% only to come crashing back down by 78% in 2002 -- a period that has come to be known as the "Dotcom Bubble". Prior to the bursting of the bubble, many quit their jobs to try their hand at the new gold rush of day trading. Some made fortunes from employee stock options or day-trading, but far many more squandered their wealth on bad bets.

In Sparrow Capital you will try your hand at playing the market right at the start of the bubble to see if you have what it would have taken to make it big. You will start with a small initial bank and, over the course of the 7 year period, buy & sell the shares of over 150 companies to build your portfolio. Will you pick the winners that make your millions? Will you sell right at the top of the market before it's all gone before your eyes? Or will the burst of the bubble have you wishing that Y2K was as bad as they said it was going to be?

---
### Usage

To run in production (assuming you're in the sarcastic-sparrows project directory):

```bash
docker-compose -f production.yml up --build
```
The first thing the app is going to do is to pre-load the 580,000+ records of static stock data into the database. Be warned that this takes about 1 minute to complete.

Finally, open the website at [0.0.0.0:8000](http://0.0.0.0:8000).

#### Hacking

Run the app using docker-compose:
```
docker-compose -f local.yml up --build
```

To run the tests:
```
docker-compose -f local.yml run --rm django pytest
```

Please use the pre-commit hook, as well
to allow for lint checks on commit.
Assuming you are in the sarcastic-sparrows
directory:

```
cp .pre-commit-config.yaml ../.pre-commit-config.yaml
pip install pre-commit
pre-commit install
```

The first command will copy the pre-commit config file
to the project root directory (where all the teams' files
are). The latter will pip install pre-commit, and finally,
install the hook in .git.

If you don't want to commit the files but want to check
with pre-commit first, run: `pre-commit run --all-files`

---
### License and Credit

This project is licensed under the MIT License.

This project was created by:

- [rdcox](https://github.com/rdcox)
- [sschar15](https://github.com/sschr15)
- [andrewrhunt](https://github.com/andrewrhunt)
- [TheGermanAZ](https://github.com/TheGermanAZ)
- [Yoom](https://github.com/YoomamaFTW)
