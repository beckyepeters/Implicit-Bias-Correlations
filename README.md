# Implicit Bias Correlations
Capstone Project #1 for RPP2 Cohort of Galvanize Data Science Immersive Program - Correlations Between Types of Bias &amp; Changes Over Time


CLEANING DATA: 

Gender-Career IAT: 
* Loaded .sav files into pandas dataframes & concatenated all 16 years of data (Starting n = 3,159,286) 
*  Cleaned data to delete incomplete sessions or those missing key attitudes / variables for this specific project
    * Completed Tests = 1,627,738 (51.52% completion rate)
    * Acceptable Error Rate: 
        * Per other studies from researchers (specifically following steps in cleaning scripts used for [this study from 2007-2015](https://osf.io/k9vqc/)), identified and removed participants with high rates of error (more than 30% or more than 10% of trials were 'too fast'), using their criteria. 
        * Completed Tests with Acceptable number of errors = 1,442,692
    * Recode necessary variables with descriptive names where necessary & numeric response where possible: 
        * Education: 
            * Highest Education Completed scale changed from 13 items to 14 somewhere along the way so I kept the 13 and put the added 14th ("MBA") back into 'other advanced degree' as it was in years prior. 
            * There were 11,083 data points collected with the 14th category, those were absorbed back into the edu_13 column; removed 'edu' column with redundant values. 
        * Religion: 
            * Combined religion columns with different indicators; kept religious id as most relevant (not religious, a little religious, etc... instead of having specific denominations)
        * 

Notes after 4.3 Saturday session 
- Wasted morning trying to use plotly, abandoned at noon 
- Got some good plots from what I thought was clean data but then I saw a big dip in 2016 participation and am concerned about that
- Also idea to demonstrate unchanging or stagnant or changing demographics among this population of people who take the test (seems always 70% female, does that carry for other tests or just the gender ones?, and also other parameters). 
- US map to show changes over years would be cool, like a giphy kind that changes as you hover over it :) 
- Get a one-on-one with Heather on Monday or Tuesday before class to make determinations about inferential statistics, hypothesis testing, or correlations. No -- Try to do correlations plots before you talk to her!! Get hyp testing ideas from her but she already told you correlation is a good one, so get that done first. 
- Implicit - how do you name the unit of measurement? It's time but not really reaction time, they do stuff to it that I haven't read about in any of their studies... look more... 
- 