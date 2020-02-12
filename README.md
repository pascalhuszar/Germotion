# Germotion - Sentiment Analysis / Emotion Analysis for the German language.

Here you can find two scripts with a ruled based approach, estimating emotional and sentimental value of German text.

## Emotion Analysis
Up to seven diffrent emotions (Verachtung, Freude, Wut,...) will be detected. The return will be an dictionary. The value represent the share of the corresponding emotion. 
##### Example: 

	Query: "Jede gute Sache im Leben, jeder Sieg der Liebe über den Hass, der Gerechtigkeit über die Ungerechtigkeit, der Gleichheit und Brüderlichkeit über die Ausbeutung, der Eintracht über die Zwietracht, gibt Zeugnis für die Auferstehung in unserem Leben."

	Output: {"Verachtung": 34, "Freude": 12, "Wut": 54}

## Sentiment Analysis
Gets the sentimental value from two dictionaries. Both dictionaries contain of words that have a certain value in range of -1 to +1 and represents the sentimental value. 
Positive value implies positive/good words, negative value negative/bad words. 
##### Example: 

	Query: "Jede gute Sache im Leben, jeder Sieg der Liebe über den Hass, der Gerechtigkeit über die Ungerechtigkeit, der Gleichheit und Brüderlichkeit über die Ausbeutung, der Eintracht über die Zwietracht, gibt Zeugnis für die Auferstehung in unserem Leben."

	Output: {'sentiment': -0.37}

## Requirements 
Python 3.7

## How To
Open one of the script. In the main function, enter a query and run main. 

## Resources:
Emotion dictionary: https://bitbucket.org/rklinger/german-emotion-dictionary/src/master/ \
Sentiment dictionary: http://wortschatz.uni-leipzig.de/en/download/


