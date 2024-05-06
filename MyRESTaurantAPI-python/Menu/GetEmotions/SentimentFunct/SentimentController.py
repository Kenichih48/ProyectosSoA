import os
from google.cloud import language_v1



class Sentiment:
    
    def GCNL(text, route):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = route
        client = language_v1.LanguageServiceClient()
        document = language_v1.Document(
            content = text, type_=language_v1.Document.Type.PLAIN_TEXT
        )
        sentiment = client.analyze_sentiment(
            request={"document": document}
        ).document_sentiment

        print("Text: {}".format(text))
        print("Sentiment: {}, Magnitude: {}".format(sentiment.score, sentiment.magnitude))
        return sentiment.score, sentiment.magnitude

    #Ranges:
    #-1 to -0.7 Clearly Negative Sentiment | send 0
    #-0.7 to -0.3 Negative Sentiment | send 1
    #-0.3 to 0.3 & Magnitude < 1 Neutral | send 2
    #-0.3 to 0.3 & Magnitude > 1 Mixed | send 3
    #0.3 to 0.7 Positive Sentiment | send 4
    #0.7 to 1 Clearly Positive Sentiment |send 5 
    def filterSentiment(score, magnitude):
        result = 0
        if (score < -0.7):
            result = 0
        elif (score < -0.3):
            result = 1
        elif ((score < 0.3) and (magnitude < 1)):
            result = 2
        elif ((score < 0.3) and (magnitude >= 1)):
            result = 3
        elif (score < 0.7):
            result = 4
        else:
            result = 5
        return result


    def getSentiment(text, route):
        #Recibir text de front end acá
        #text = "This dish was alright, I mean it did its job, better than Applebees that's for sure" #entrada usuario
        score, magnitude = Sentiment.GCNL(text, route)
        sentiment = Sentiment.filterSentiment(score, magnitude)
        print(sentiment)
        #mandar sentiment a front end acá
        return sentiment
