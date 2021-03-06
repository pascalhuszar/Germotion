# Germotion - Sentiment Analysis / Emotion Analysis for the German language.

Here you can find two scripts with a ruled based approach, estimating emotional and sentimental value of German text.

## Emotion Analysis
Up to seven different emotions (Verachtung, Freude, Wut,...) will be detected. The return will be a dictionary. The value represent the share of the corresponding emotion. 
##### Example: 
```python
	Query: "Jede gute Sache im Leben, jeder Sieg der Liebe über den Hass, der Gerechtigkeit über die Ungerechtigkeit, der Gleichheit und Brüderlichkeit über die Ausbeutung, der Eintracht über die Zwietracht, gibt Zeugnis für die Auferstehung in unserem Leben."

	Output: {"Verachtung": 34, "Freude": 12, "Wut": 54}
```

## Sentiment Analysis
Take the sentimental value from two dictionaries. Both dictionaries contains of words that have a certain value in the range of -1 to +1 and represents the sentimental value. 
Positive value implies positive/good words, negative value negative/bad words. 
##### Example: 
```python
	Query: "Jede gute Sache im Leben, jeder Sieg der Liebe über den Hass, der Gerechtigkeit über die Ungerechtigkeit, der Gleichheit und Brüderlichkeit über die Ausbeutung, der Eintracht über die Zwietracht, gibt Zeugnis für die Auferstehung in unserem Leben."

	Output: {'sentiment': -0.37}
```

## Requirements 
Python 3.7

## How To
```bash
	1. $ cd *yourpath*/Germotion
	2. python3 -m pip install -r requirements.txt
	3. Open one of the script. In the main function, enter a query and run main.
```


## Resources:
Emotion dictionary: https://bitbucket.org/rklinger/german-emotion-dictionary/src/master/ \
Sentiment dictionary: http://wortschatz.uni-leipzig.de/en/download/

## License
Released under the MIT License.


