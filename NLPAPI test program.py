
# I get this test program from 
# https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3#6

# test program for cloud natural language API
from google.cloud import language


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")


#text1 = 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness,it was the epoch of belief, it was the epoch of incredulity, it was the season of Darkness, it was the spring of hope, it was the winter of despair '
#print(analyze_text_sentiment(text1))

#text2 = "the game is worth to buy"
#print(analyze_text_sentiment(text2))

text3 = 'you are terrible'
print(analyze_text_sentiment(text3))



