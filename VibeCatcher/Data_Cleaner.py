import re, string
from nltk.corpus import stopwords
from nltk.tokenize import TweetTokenizer
import pandas as pd
import numpy as np
import csv
import os
import random
from dict.en.abbreviations_en import *
from dict.fr.abbreviations_fr import *

def DataCleanerEn(status, hashtag, path):
    tokenizer = TweetTokenizer(strip_handles=True)
    stop_words = set(stopwords.words('english'))
    corpus = []

    def clean(tweet):
        #decoding
        tweet = tweet.encode('utf-8').decode('unicode-escape')
        #replace
        tweet = re.sub(r'#', " ", tweet)
        #remove decoding
        tweet = re.sub(r'[^\x20-\x7E]',r'', tweet)
        # First character to remove
        tweet = re.sub(r'b"', "", tweet)
        tweet = re.sub(r'"RT', "", tweet)
        tweet = re.sub(r"b'RT", "", tweet)
        tweet = re.sub(r"b'RT", "", tweet)
        tweet = re.sub(r"b'", "", tweet)
        # Contractions
        tweet = re.sub(r"he's", "he is", tweet)
        tweet = re.sub(r"there's", "there is", tweet)
        tweet = re.sub(r"We're", "We are", tweet)
        tweet = re.sub(r"That's", "That is", tweet)
        tweet = re.sub(r"won't", "will not", tweet)
        tweet = re.sub(r"they're", "they are", tweet)
        tweet = re.sub(r"Can't", "Cannot", tweet)
        tweet = re.sub(r"wasn't", "was not", tweet)
        tweet = re.sub(r"don\x89Ûªt", "do not", tweet)
        tweet = re.sub(r"aren't", "are not", tweet)
        tweet = re.sub(r"isn't", "is not", tweet)
        tweet = re.sub(r"What's", "What is", tweet)
        tweet = re.sub(r"haven't", "have not", tweet)
        tweet = re.sub(r"hasn't", "has not", tweet)
        tweet = re.sub(r"There's", "There is", tweet)
        tweet = re.sub(r"He's", "He is", tweet)
        tweet = re.sub(r"It's", "It is", tweet)
        tweet = re.sub(r"You're", "You are", tweet)
        tweet = re.sub(r"I'M", "I am", tweet)
        tweet = re.sub(r"shouldn't", "should not", tweet)
        tweet = re.sub(r"wouldn't", "would not", tweet)
        tweet = re.sub(r"i'm", "I am", tweet)
        tweet = re.sub(r"I\x89Ûªm", "I am", tweet)
        tweet = re.sub(r"I'm", "I am", tweet)
        tweet = re.sub(r"Isn't", "is not", tweet)
        tweet = re.sub(r"Here's", "Here is", tweet)
        tweet = re.sub(r"you've", "you have", tweet)
        tweet = re.sub(r"you\x89Ûªve", "you have", tweet)
        tweet = re.sub(r"we're", "we are", tweet)
        tweet = re.sub(r"what's", "what is", tweet)
        tweet = re.sub(r"couldn't", "could not", tweet)
        tweet = re.sub(r"we've", "we have", tweet)
        tweet = re.sub(r"it\x89Ûªs", "it is", tweet)
        tweet = re.sub(r"doesn\x89Ûªt", "does not", tweet)
        tweet = re.sub(r"It\x89Ûªs", "It is", tweet)
        tweet = re.sub(r"Here\x89Ûªs", "Here is", tweet)
        tweet = re.sub(r"who's", "who is", tweet)
        tweet = re.sub(r"I\x89Ûªve", "I have", tweet)
        tweet = re.sub(r"y'all", "you all", tweet)
        tweet = re.sub(r"can\x89Ûªt", "cannot", tweet)
        tweet = re.sub(r"would've", "would have", tweet)
        tweet = re.sub(r"it'll", "it will", tweet)
        tweet = re.sub(r"we'll", "we will", tweet)
        tweet = re.sub(r"wouldn\x89Ûªt", "would not", tweet)
        tweet = re.sub(r"We've", "We have", tweet)
        tweet = re.sub(r"he'll", "he will", tweet)
        tweet = re.sub(r"Y'all", "You all", tweet)
        tweet = re.sub(r"Weren't", "Were not", tweet)
        tweet = re.sub(r"Didn't", "Did not", tweet)
        tweet = re.sub(r"they'll", "they will", tweet)
        tweet = re.sub(r"they'd", "they would", tweet)
        tweet = re.sub(r"DON'T", "DO NOT", tweet)
        tweet = re.sub(r"That\x89Ûªs", "That is", tweet)
        tweet = re.sub(r"they've", "they have", tweet)
        tweet = re.sub(r"i'd", "I would", tweet)
        tweet = re.sub(r"should've", "should have", tweet)
        tweet = re.sub(r"You\x89Ûªre", "You are", tweet)
        tweet = re.sub(r"where's", "where is", tweet)
        tweet = re.sub(r"Don\x89Ûªt", "Do not", tweet)
        tweet = re.sub(r"we'd", "we would", tweet)
        tweet = re.sub(r"i'll", "I will", tweet)
        tweet = re.sub(r"weren't", "were not", tweet)
        tweet = re.sub(r"They're", "They are", tweet)
        tweet = re.sub(r"Can\x89Ûªt", "Cannot", tweet)
        tweet = re.sub(r"you\x89Ûªll", "you will", tweet)
        tweet = re.sub(r"I\x89Ûªd", "I would", tweet)
        tweet = re.sub(r"let's", "let us", tweet)
        tweet = re.sub(r"it's", "it is", tweet)
        tweet = re.sub(r"can't", "cannot", tweet)
        tweet = re.sub(r"don't", "do not", tweet)
        tweet = re.sub(r"you're", "you are", tweet)
        tweet = re.sub(r"i've", "I have", tweet)
        tweet = re.sub(r"that's", "that is", tweet)
        tweet = re.sub(r"i'll", "I will", tweet)
        tweet = re.sub(r"doesn't", "does not", tweet)
        tweet = re.sub(r"i'd", "I would", tweet)
        tweet = re.sub(r"didn't", "did not", tweet)
        tweet = re.sub(r"ain't", "am not", tweet)
        tweet = re.sub(r"you'll", "you will", tweet)
        tweet = re.sub(r"I've", "I have", tweet)
        tweet = re.sub(r"Don't", "do not", tweet)
        tweet = re.sub(r"I'll", "I will", tweet)
        tweet = re.sub(r"I'd", "I would", tweet)
        tweet = re.sub(r"Let's", "Let us", tweet)
        tweet = re.sub(r"you'd", "You would", tweet)
        tweet = re.sub(r"It's", "It is", tweet)
        tweet = re.sub(r"Ain't", "am not", tweet)
        tweet = re.sub(r"Haven't", "Have not", tweet)
        tweet = re.sub(r"Could've", "Could have", tweet)
        tweet = re.sub(r"youve", "you have", tweet)
        tweet = re.sub(r"donå«t", "do not", tweet)
        tweet = re.sub(r"some1", "someone", tweet)
        tweet = re.sub(r"yrs", "years", tweet)
        tweet = re.sub(r"hrs", "hours", tweet)
        tweet = re.sub(r"2morow|2moro", "tomorrow", tweet)
        tweet = re.sub(r"2day", "today", tweet)
        tweet = re.sub(r"4got|4gotten", "forget", tweet)
        tweet = re.sub(r"b-day|bday", "b-day", tweet)
        tweet = re.sub(r"mother's", "mother", tweet)
        tweet = re.sub(r"mom's", "mom", tweet)
        tweet = re.sub(r"dad's", "dad", tweet)
        tweet = re.sub(r"hahah|hahaha|hahahaha", "haha", tweet)
        tweet = re.sub(r"lmao|lolz|rofl", "lol", tweet)
        tweet = re.sub(r"thanx|thnx", "thanks", tweet)
        tweet = re.sub(r"goood", "good", tweet)
        tweet = re.sub(r"some1", "someone", tweet)
        tweet = re.sub(r"some1", "someone", tweet)
        # Character entity references
        tweet = re.sub(r"&gt;", ">", tweet)
        tweet = re.sub(r"&lt;", "<", tweet)
        tweet = re.sub(r"&amp;", "&", tweet)
        # Typos, slang and informal abbreviations
        tweet = re.sub(r"w/e", "whatever", tweet)
        tweet = re.sub(r"w/", "with", tweet)
        tweet = re.sub(r"<3", "love", tweet)
        # Urls
        tweet = re.sub(r"http\S+", "", tweet)
        # Numbers
        #tweet = re.sub(r'[0-9]', '', tweet)
        # Eliminating the mentions
        tweet = re.sub("(@[A-Za-z0-9_]+)", "", tweet)
        # Remove punctuation and special chars (keep '!')
        for p in string.punctuation.replace('!', ''):
            tweet = tweet.replace(p, '')
        # ... and ..
        tweet = tweet.replace('...', ' ... ')
        if '...' not in tweet:
            tweet = tweet.replace('..', ' ... ')
        # Tokenize
        tweet_words = tokenizer.tokenize(tweet)
        # Eliminating the word if its length is less than 3
        #tweet = [w for w in tweet_words if len(w) > 2]
        # remove stopwords
        tweet = [w.lower() for w in tweet_words if not w in stop_words]

        corpus.append(tweet)

        # join back
        tweet = ' '.join(tweet)

        return tweet

    def convert_abbrev_in_text(tweet):
        t=[]
        words=tweet.split()
        t = [abbreviations_en[w.lower()] if w.lower() in abbreviations_en.keys() else w for w in words]
        return ' '.join(t)

    if status == "train":
        df = pd.read_csv(path+"/train.csv", encoding="utf-8", usecols=[0, 5], names=["label","tweet"])
        out = path+"/Cleaned_train.csv"
    elif status == "pred":
        df = pd.read_csv(path+"/"+hashtag+".csv", encoding="utf_8", header=0)
        out = path+"/Cleaned_"+hashtag+".csv"
    else:
        df = pd.read_csv(path+"/"+hashtag+".csv", encoding="utf-8", header=0)
        out = path + "/Cleaned_" + hashtag + ".csv"

    #random.seed(41)
    #print(df.iloc[random.sample(range(1, 1600000), 10), :])

    df['tweet']=df['tweet'].apply(lambda s : clean(str(s)))
    df['tweet']=df['tweet'].apply(lambda s : convert_abbrev_in_text(s))

    indexNames = df[df['tweet'] == "nan"].index
    df.drop(indexNames, inplace=True)

    indexNames = df[df['tweet'] == ""].index
    df.drop(indexNames, inplace=True)

    df.dropna()

    df = df.to_csv(path+"/tmp.csv", index=False)

    def shuffler(filename):
      df = pd.read_csv(filename, header=0, dtype=object, na_filter=False)
      return df.reindex(np.random.permutation(df.index))

    shuffler(path+"/tmp.csv").to_csv(path+"/tmp2.csv", sep=',', encoding='utf-8', index=False)

    with open(path+"/tmp2.csv", newline='', encoding='utf-8') as f_input, open(out, 'w', newline='', encoding='utf-8') as f_output:

        csv_input = csv.reader(f_input, skipinitialspace=True)
        csv_output = csv.writer(f_output, quoting=csv.QUOTE_NONNUMERIC)

        for row_input in csv_input:
            row_output = []
            for col in row_input:
                try:
                    row_output.append(col)
                except ValueError as e:
                    row_output.append(col)

            csv_output.writerow(row_output)

    if os.path.exists(path+"/tmp.csv"):
      os.remove(path+"/tmp.csv")

    if os.path.exists(path+"/tmp2.csv"):
      os.remove(path+"/tmp2.csv")

########################################################################################################################

def DataCleanerFr(status, hashtag, path):
    tokenizer = TweetTokenizer(strip_handles=True)
    stop_words = set(stopwords.words('french'))
    corpus = []

    def clean(tweet):
        # decoding
        tweet = tweet.encode('utf-8').decode('unicode-escape')
        #replace
        tweet = re.sub(r'#', " ", tweet)
        tweet = re.sub(r"\xc3\xa9", "e", tweet)
        tweet = re.sub(r"\xc3\xa8", "e", tweet)
        tweet = re.sub(r"\xc3\xaa", "e", tweet)
        tweet = re.sub(r"\xc3\xab", "e", tweet)
        tweet = re.sub(r"\xe2\x80\x99", " ", tweet)
        tweet = re.sub(r"\xc3\xa7", "c", tweet)
        tweet = re.sub(r"\xc3\xa0", "a", tweet)
        tweet = re.sub(r"\xc3\xa1", "a", tweet)
        tweet = re.sub(r"\xc3\xbb", "u", tweet)
        tweet = re.sub(r"\xc3\xbc", "u", tweet)
        # remove decoding
        tweet = re.sub(r'[^\x20-\x7E]', r'', tweet)
        #decoding
        tweet = tweet.encode('latin-1').decode('utf-8')
        #mistake
        tweet = re.sub(r"cest", "c’est", tweet)
        tweet = re.sub(r"’", " ", tweet)
        # First character to remove
        tweet = re.sub(r'b"', "", tweet)
        tweet = re.sub(r'"RT', "", tweet)
        tweet = re.sub(r"b'RT", "", tweet)
        tweet = re.sub(r"b'RT", "", tweet)
        tweet = re.sub(r"b'", "", tweet)
        tweet = re.sub(r'RT', "", tweet)
        # Character entity references
        tweet = re.sub(r"&gt;", ">", tweet)
        tweet = re.sub(r"&lt;", "<", tweet)
        tweet = re.sub(r"&amp;", "&", tweet)
        # Typos, slang and informal abbreviations
        tweet = re.sub(r"w/e", "peu importe", tweet)
        tweet = re.sub(r"w/", "avec", tweet)
        tweet = re.sub(r"<3", "amour", tweet)
        # Urls
        tweet = re.sub(r"http\S+", "", tweet)
        # Numbers
        #tweet = re.sub(r'[0-9]', '', tweet)
        # Eliminating the mentions
        tweet = re.sub("(@[A-Za-z0-9_]+)", "", tweet)
        # Remove punctuation and special chars (keep '!')
        for p in string.punctuation.replace('!', ''):
            tweet = tweet.replace(p, '')
        # ... and ..
        tweet = tweet.replace('...', ' ... ')
        if '...' not in tweet:
            tweet = tweet.replace('..', ' ... ')
        # Tokenize
        tweet_words = tokenizer.tokenize(tweet)
        # Eliminating the word if its length is less than 3
        #tweet = [w for w in tweet_words if len(w) > 2]
        # remove stopwords
        tweet = [w.lower() for w in tweet_words if not w in stop_words]

        corpus.append(tweet)

        # join back
        tweet = ' '.join(tweet)

        return tweet

    def convert_abbrev_in_text(tweet):
        t=[]
        words=tweet.split()
        t = [abbreviations_fr[w.lower()] if w.lower() in abbreviations_fr.keys() else w for w in words]
        return ' '.join(t)

    if status == "train":
        df = pd.read_csv(path+"/train.csv", encoding="utf-8", usecols=[0, 5], names=["label","tweet"])
        out = path+"/Cleaned_train.csv"
    elif status == "pred":
        df = pd.read_csv(path+"/"+hashtag+".csv", encoding="utf-8", header=0)
        out = path+"/Cleaned_"+hashtag+".csv"
    else:
        df = pd.read_csv(path+"/"+hashtag+".csv", encoding="utf-8", header=0)
        out = path + "/Cleaned_" + hashtag + ".csv"

    #random.seed(41)
    #print(df.iloc[random.sample(range(1, 1600000), 10), :])

    df['tweet']=df['tweet'].apply(lambda s : clean(str(s)))
    df['tweet']=df['tweet'].apply(lambda s : convert_abbrev_in_text(s))

    indexNames = df[df['tweet'] == "nan"].index
    df.drop(indexNames, inplace=True)

    indexNames = df[df['tweet'] == ""].index
    df.drop(indexNames, inplace=True)

    df.dropna()

    df = df.to_csv(path+"/tmp.csv", index=False)

    def shuffler(filename):
      df = pd.read_csv(filename, header=0, dtype=object, na_filter=False)
      return df.reindex(np.random.permutation(df.index))

    shuffler(path+"/tmp.csv").to_csv(path+"/tmp2.csv", sep=',', encoding='utf-8', index=False)

    with open(path+"/tmp2.csv", newline='', encoding="utf8") as f_input, open(out, 'w', newline='', encoding="utf8") as f_output:

        csv_input = csv.reader(f_input, skipinitialspace=True)
        csv_output = csv.writer(f_output, quoting=csv.QUOTE_NONNUMERIC)

        for row_input in csv_input:
            row_output = []
            for col in row_input:
                try:
                    row_output.append(col)
                except ValueError as e:
                    row_output.append(col)

            csv_output.writerow(row_output)

    if os.path.exists(path+"/tmp.csv"):
      os.remove(path+"/tmp.csv")

    if os.path.exists(path+"/tmp2.csv"):
      os.remove(path+"/tmp2.csv")