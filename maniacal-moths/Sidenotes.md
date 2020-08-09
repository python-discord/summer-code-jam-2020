# Newsly

## Side Notes

There are a couple of things that need to be done additionally to utilise every feature of Newsly.  
**Note that I've made adequate arrangements for the app to be funtional without you having to go through the steps below**, but if you'd like to test them regardless, continue reading.


The `Refresh Database` button on the website is meant to get the latest articles in real time. To actually make it work, you will have to obtain the API key for [NewsCatcher](https://newscatcherapi.com/) API. There are two ways in which you can do this:  
1) DM me on discord(hot9cups#3125) and I'll provide you my key.
2) Get your own key. 

If you're getting your own key, steps to do that are explained very well [here](https://newscatcherapi.com/how-to-start).  
Head to their official [site](https://rapidapi.com/newscatcher-api-newscatcher-api-default/api/newscatcher/pricing). Select the free Basic Plan, and sign up. Then navigate to 'Test Endpoints' and there you will find a section called 'Code Snippets' towards the right which will contain your unique API key.

After you've obtained your key, head to the file `db_gen.py` inside the directory `aggregator`. There, you'll find a `self.headers` attribute inside the class `Database_Generator`. Insert your key in the place of "SECRET-ID-HERE".  
And you're good to go. (I should mention, the API goes down occasionally. That was the entire reason I decided to cache the articles and uploaded the sqllite database on the repo, so you don't need to gather articles yourself).

Another note: In case you decide to create a profile on Newsly, do ensure to visit your profile page after you log-in to ensure your preferred language and country are set correctly. At times, it gets defaulted to Arabia and Argentina and I'm working on fixing it. But for now, visit your profile page and ensure your preferred settings are correct(Once you set them manually in the profile page though, they will always be correct in the future).