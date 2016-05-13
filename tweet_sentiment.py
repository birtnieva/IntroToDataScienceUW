import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    lines(tweet_file)

    # Check type of opened file
    # print type(tweet_file)

    # Create dictionary for scoring each term
    # Terms and score are stored in a file
    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")     # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)           # Convert the score to an integer.



    # Create a list from tweets from output.txt
    # Tweets are taken via twitter API
    tweets = []
    tweets = [json.loads(line) for line in open(sys.argv[2])]

    for tweet in tweets[0]['statuses']:
        words = tweet['text'].encode('utf-8').split(" ")
        tweet_score = 0
        for word in words:
            if word in scores:
                tweet_score += int(scores[word])
        print (tweet_score)


if __name__ == '__main__':
    main()
