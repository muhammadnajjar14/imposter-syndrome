#!/usr/bin/env python
# coding: utf-8

# In[25]:


#https://raw.githubusercontent.com/riyaeliza123/imposter-syndrome/main/Imposter%20Syndrome%20csv.csv

import pandas as pd
import numpy as np


# In[42]:


df = pd.read_csv('https://raw.githubusercontent.com/riyaeliza123/imposter-syndrome/main/Imposter%20Syndrome%20csv.csv')
#df
df = df.drop('S.NO.', 1)
df.rename(columns = {'Do you chalk your success up to fates, luck or\nerror?':'success', 
                     'Many times, you feel crushed by constructive criticism, seeing it as evidence of your "ineptness"?':'many ineptness',
                     'Do you believe "If I can do it, anybody can"?':'if anybody can',
                     'Do you agonize over the smallest flaws in your work?':'agonize',
                     'Do you believe that everything you do must be completely perfect?':'perfect',
                     'In rare cases you feel crushed by constructive criticism, seeing it evidence of your "ineptness"?':'rare ineptness',
                     'Do you feel incompetent despite attaining success?':'imcompetent',
                     'You compare your abilities to people around you and think that others may be more intelligent than you.':'compare',
                     'You blame your luck for success rather than hard work':'luck not hard work',
                     'Do you think shortcut to success makes you smarter':'shortcut',
                     'Do you often fear not meeting other people\'s expectations?':'expectations',
                     'I am a perfectionist':'perfectionist',
                     'Do you feel like a non-valuable member of the family if you don\'t participate in domestic work?':'domestic',
                     '"I have to be good at a particular activity to enjoy it" (As in, if you picked up a new hobby like painting, the only way you feel good about doing it is if you are using perfect techniques and doing it the "right" way)':'enjoy activity',
                     'I believe that means is more important than the ends':'means',
                     'When people compliment you, you think you are not as accomplished as they think':'compliment',
                     'Most of your success has been a stroke of luck':'stroke of luck',
                     'You have an above-average IQ score':'IQ score',
                     'Your emotional quotient is better than your general IQ score':'EQ',
                     'You downplay compliments from others.':'no compliments',
                     'Do you feel like an unimportant family member if you don\'t involve in decision-making process?':'not imp',
                     'Which places do you think you can be yourself without being judged?':'place not judged',
                     'What places do you think you pretend to be someone you are not?':'place judged',
                     'At least 70% of individuals have dissatisfaction in their lives. Women mostly face self-image issues and in men, it is driven by the fear of not being successful or letting people down. Do you agree with this? And in your experience, how have you seen variances to the mentioned scenarios?':'letting people down',
                     'As the campus has reopened after conducting classes, examinations, and project reviews online over the past 2 years, do you feel that this might bring up changes in confidence levels, due to the adjustments which may have arisen doubts in self-esteem from the initial change of method?':'post covid confidence'
                     

                        }, inplace = True)

#df


# In[43]:


#preprocessing
#in the comfort percentage, change all NA to 0
#df1=df[0:5]  #first 6 rows

df.update(df1[['comfort.home','comfort.college','comfort.friends', 'comfort.work','comfort.online', 'comfort.alterego']].fillna(0))
#df1


# In[44]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


# In[45]:


#pass sentence, returns pos/neg
#take each sentence, add all pos, neu and neg and finally give overall sentiment per gender
#make 2 datasets (m,f) and do sentiment analysis

dfmale = df[df['Gender'] == 'M']
#print (dfmale)
dffemale = df[df['Gender'] == 'F']
dffemale


# In[ ]:


# function to print sentiments of the sentence.
def sentiment_scores(sentence):
 
    sid_obj = SentimentIntensityAnalyzer()
    
    sentiment_dict = sid_obj.polarity_scores(sentence) #polarity_scores is predefined, contains neg, neu and pos
    print("Overall sentiment dictionary is : ", sentiment_dict)
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative")
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral")
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive")
    print("Sentence Overall Rated As", end = " ")
    # decide sentiment as positive, negative and neutral
    if sentiment_dict['compound'] >= 0.05 :
        print("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        print("Negative")
    else :
        print("Neutral")

