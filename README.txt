I choose to use google NLP API.
I tested three examples.
For the first example 'It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness,it was the epoch of belief, it was the epoch of incredulity, it was the season of Darkness, it was the spring of hope, it was the winter of despair '
The answer is score -30, magnitude 30 which meanst that the emotional is not strong. It is relatively negative emotion shows in the text.
For the second example "the game is worth to buy". The output is score 90, magnitude 90. The program successfully detect the positive emotional in the this sentence.
For the third example ' 'you are terrible' The output is score -90, magnitude 90. The The program successfully detect the strong negative emotional in the this sentence.

except from google NLP, I also explored google healthcare NLP API.
I created and managed a dataset. Created DICOM, FHIR, or HL7v2 store in the dataset. .
I also use FHIR view function to check information in the dataset I imported.
