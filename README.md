# Twitter bot

This is a very simple twitter bot that allows you to tweet on a regular basis.

The bot uses a Google Spreadsheet to get the content, and tweet it. It can tweet
with images as well, so you can share the Spreadsheet with your team and they only
have to add content to the spreadsheet. Then, the bot will take care of it.


## Installation

To install it, clone the repository and create a virtual environment:

```
virtualenv env
```

Activate the env:

```
source env/bin/activate
```

Then install all the libraries:

```
pip install -r requirements.txt
```

Done!

## Configuring it

You will need several configuration items:

* Twitter consumer key
* Twitter consumer secret key
* Twitter token code
* Twitter token secret
* URL of your google spreadsheet
* JSON oauth file name for Google Drive

Once you have all that information, copy the settings.py.tmpl to settings.py and fill it.

## Google Spreadsheet

The first sheet should be the sheet used as the index. Name it dashboard. You don't have to
write anything in there, the bot will use the cell A1 to tell you wich is the last sheet used to tweet.

Then, add as many sheets as you need. Basically use sheets to split content. For example: one sheet for your
devops content, one for your sales, one for your community, etc. The bot will be jumping between them to tweet
about it.

For these sheets you have to follow the following structure:

* **A1**: the tweet text.
* **B1**: leave it empty. The bot will update this column with the word *last* so you know which is the last tweeted tweet from this sheet.
* **C1**: URL link to the image that you want to include in your tweet.

## Tweeting by hand

If you want to test it, you only have to run the following command:

```
python app.py
```

If everything goes well, you will see the tweet posted in your account.

## Tweeting at given times

As this bot is a script, you can use Cron to tweet 5 times a day, once a week, etc. 

## Adding new content

If you want to add new content, all you have to do is to open the Google Spreadsheet and
add a new row in one of the available sheets, or create a new one if this tweet belongs to a
new category.

# LICENSE
AGPLv3 see COPYING file.
