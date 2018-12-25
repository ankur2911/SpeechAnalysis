# SpeechAnalysis

The program aims at comparing the presidential inaugural speeches of two recent presidents of United States of American, President Barack Obama, the 44th President of USA and President Donald J Trump, the 45th and current President of USA. I have used POS tagging, Lexical diversity and common words used as the parameters upon which the speeches have been compared. I have also used Markov chain to generate random sentences using both the speech corpus.

Approach

I first removed the stop words and punctuations from the corpus, following which I tokenized each of the corpus. I have applied the techniques mentioned in a sequential manner, i.e., I ran the same experiment first on President Obama’s speech and then on President Trump’s speech. This gave me the results in a manner in which I can compare both the speeches together on a similar point. Also, I have tried to include as much graphical representation as possible, as this will give a better view to the user of the results. Using different types of graphs was a calculated decision, in the hope of getting an accurate result for all the experiments.
I have displayed the Lexical diversity score for both the speeches on the console as well, to compare the numerical value. Also, as an extra point to analyze the speeches, I have generated new sentences for both the speeches using Markov chain technique, which have been displayed on the console as well.


Experiments

As I described earlier, I have conducted a number of experiments on both the corpus to compare them and come up with a conclusion. In this section, I will describe each of the experiments in detail.

First, I have determined the Lexical Diversity in the speech for both the Presidents. According to Wikipedia, the lexical diversity of a given text is defined as the ratio of total number of words to the number of different unique word stems. I got the lexical diversity scores for both the Presidents and have displayed that on console. I have also displayed a plot to represent the same.

Next, I worked on POS tagging. A word can be a noun, a verb and adjective, NLTK helped in determining this.
Then, I worked on getting the top 50 most frequent words used by both the Presidents. For this I used the NLTK library, which has an inbuild function of Frequency Distribution for getting the frequent words. I specified the number of frequent words that I need while displaying the plot for the same.

Lastly, I tried to come up with new sentences that could be made using the corpus. I have used Markov chain model for the same. I defined a make_pair method which pairs the words from the corpus and creates a word dictionary. Then I have randomly appended the word pairs after selecting the first word randomly.
