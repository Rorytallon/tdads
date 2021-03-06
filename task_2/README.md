# TDADS Task 2 - Airline Tweets

## Structure

- Code is in `code`
- Sample code outputs are in `code_output`
- 'Output folder with all the visuals you use' is `output`. If more needs adding to this let [George](mailto:sc18gah@leeds.ac.uk) know.

## Setup

- Due to the way we wrote our code, there are a number of things you can run (with different requirements). All these should be run from the `code/` folder, which should include everything necessary. Some extra data is in `code/extra_data/`.
- You need to install some pip and NLTK libraries:
  ```
  pip install -r requirements.txt
  python -c 'import nltk; nltk.download("stopwords"); nltk.download("wordnet"); nltk.download("punkt")'
  ```
- The following files are available to run:

### Location Recognition

#### Usage

- LocationRecognition.py - run as main module, outputs to:
  _ code_output/tweets_with_locations.csv
  _ code_output/locations_totals.csv

#### Requirements

- tweets.csv
- preproc.py
- world-cities.csv
- airport-codes.csv

### Naive Bayes

#### Usage

- NaiveBayes.py - run as main module

#### Requirements

- tweets.csv
- preproc.py

### Latent Semantic Analysis - LDA

#### Usage

- LDA_gensim.py - run as main module, outputs to code_output/airline_topics/

#### Requirements

- tweets.csv
- preproc.py

### Latent Semantic Analysis - SVD

#### Usage

- LSA.py - run as main module, outputs to code_output/topic_tweets.csv

#### Requirements

- preprocessed_negative_tweets.csv
- preproc.py

## Logistical Regressor

#### Usage

```bash
python logistic_regressor.py
```

It will then ask for you to enter the name of the file of processed tweets you want to use.

The first run of the program is the slowest. It has to generate a tweet vectors file which takes about five minutes on my laptop.

Once it has the file it will run much faster. The file is also too large to upload to github.

#### Requirements

- `preprocessed_tweets.csv`: A file of the tweets preproccessed. Other files can be used but this one is uploaded on the github. It just needs to be a csv file of the same format as the original tweets.csv.
- `logistic_model.py`: Python file required for the program to run.
- `one_hot_encoder.py`: Python file required to vectorize the tweets.

#### Outputs

- `results.csv`: A csv file of three columns. The words in the dictionary; the sentiment the model assigned to them; and the confidence it has in that assignment.
- `vectors_file.txt`: Text file containing the converted tweets. Only made once.

### Preliminary Analysis Tool

#### Usage

```bash
python preliminary_analysis_tool.py
```

It will then ask you for the file name of the tweets to analyse.

It will also ask you for the column name, how many bars to include, the way to sort them, and the minimum required tweets.

#### Requirements

- `tweets.csv`: A file of tweets for the program to analyse.

#### Outputs

- This program outputs two matplotlib plots. One chart of the counts of the given constraints, and one of the same graph as proportions.

### Recurrent Neural Network

#### Usage

To test the RNN, with an already trained model "sentiment_analysis_model.h5", on the airline data supplied by Will:

```bash
python RNN.py [sentiment_analysis_model.h5]
```

To test the RNN, with an already trained model "sentiment_analysis_model.h5", on the extension airline data scraped from Twitter:

```bash
python RNN_other_datasets.py [sentiment_analysis_model.h5]
```

#### Requirement

`tweets_for_RNN.csv`: A file containing all of the tweets (the extension tweets scraped from Twitter on top of those supplied by Will).

#### Output

`sentiment_analysis_model_temp.h5`: If the already trained model is not supplied to any script, the program will train a new model (\~30 minutes) and save it in this file in the same directory.

#### Troubleshooting

`Can't find model 'en'`: Please run your console with administrator privileges and run:

```bash
python -m spacy download en
```

# Most others

- All others should work as normal from running the `.py` file in `code`.
