'''
Matthew Petracca from Smithtown, NY
Sophomore Computer Science Student @ Virginia Tech
Capital One: Oscars Challenge

I solved the challenges using python, and the numpy and pandas libraries.
'''

# import the libraries
import pandas as pd
import numpy as np

# read in the csv file as a DataFrame
tweets = pd.read_csv('oscar_tweets.csv') # make sure your csv file in your working directory

# Problem 1:

# creates a list of the eight best picture nominees
bestPicNoms = ['Birdman', 'Sniper', 'Imitation', 'Selma', 'Theory', 'Boyhood', 'Whiplash', 'Budapest']

# creates a dictionary of the eight best picture nominees and their respective amount of related tweets
bestPicNums = {'Birdman': 0, 'Sniper': 0, 'Imitation': 0, 'Selma': 0, 'Theory': 0, 'Boyhood': 0, 'Whiplash': 0, 'Budapest': 0}

# Loop through tweets, splitting each tweet into strings of individual words, and incrementing appropriate best picture in the dictionary by each mention            
for text in tweets[' Text']:
    words = text.split()
    for nomName in words:
        if nomName in bestPicNoms:
            bestPicNums[nomName]+=1

print bestPicNums

# Problem 2:

# creates a function that returns True if birdman was in a tweet, False if not
def Birdman(x): return ('Birdman' or '#Birdman') in x.split()
# vectorizes the Birdman function using numpy
vBirdman = np.vectorize(Birdman)

# creates a pandas series with booleans of True and False based on the vBirdman function on all the tweets
birdman = pd.Series(map(vBirdman, tweets[' Text']))

time = pd.Series(map(lambda x: [x.split()[3].split(':')[0], x.split()[3].split(':')[1]], tweets['Time']))
data = pd.Series(zip(birdman, time))
filt = filter(lambda x: x[0] == True, data)
sup = map(lambda x: x[1], filt)

mostTime = ['00', '00']
mostCount = 0
currentTime = ['00', '00']      
currentCount = 0

for x in sup:
    if x == currentTime:
        currentCount+=1
    else:
        if currentCount >= mostCount:
            mostCount = currentCount
            mostTime = currentTime
        currentTime = x
        currentCount = 1

print mostTime, mostCount 

# Problem 3:

# creates a dictionary mapping all state names, and major cities, to their appropriate states' two letter abbreviation
states = {'alabama': 'AL', 'al': 'AL',
        'alaska': 'AK', 'anchorage': 'AK', 'ak': 'AK', 
        'arizona': 'AZ', 'az': 'AZ', 'mesa': 'AZ', 'phoenix': 'AZ', 'tucson': 'AZ',  
        'arkansas': 'AR', 'ar': 'AR',  'little': 'AR', 
        'diego': 'CA', 'angeles': 'CA', 'california': 'CA', 'ca': 'CA',  'angels': 'CA', 
        'francisco': 'CA', 'jose': 'CA', 'sacremento': 'CA',  'chula': 'CA', 'oakland': 'CA', 
        'pasadena': 'CA', 'fresno': 'CA',  'bakersfield': 'CA', 'anaheim': 'CA', 'santa': 'CA', 'riverside': 'CA', 'stockton': 'CA',
        'denver': 'CO', 'co': 'CO', 'colorado': 'CO', 'aurora': 'CO', 'boulder': 'CO', 
        'haven': 'CT', 'connecticut': 'CT', 'ct': 'CT', 
        'delaware': 'DE', 'de': 'DE', 
        'district': 'D.C.', 
        'florida': 'FL', 'fl': 'FL', 'orlando': 'FL', 'miami': 'FL', 'jacksonville': 'FL', 'tampa': 'FL',  
        'georgia': 'GA', 'ga': 'GA', 'atlanta': 'GA', 
        'hawaii': 'HI', 'honolulu': 'HI', 'hi': 'HI', 
        'idaho': 'ID', 'id': 'ID', 
        'illinois': 'IL', 'chicago': 'IL', 'il': 'IL', 
        'indiana': 'IN', 'wayne': 'IN',  'indianapolis': 'IN', 'in': 'IN', 
        'iowa': 'IA', 'moines': 'IA', 'ia': 'IA', 
        'kansas': 'KS', 'ks': 'KS', 'wichita': 'KS',  
        'kentucky': 'KY', 'louisville': 'KY',  'lexington': 'KY', 'ky': 'KY', 
        'louisiana': 'LA',  'orleans': 'LA', 'la': 'LA',  
        'maine': 'ME', 'me': 'ME', 
        'maryland': 'MD', 'md': 'MD', 'baltimore': 'MD', 
        'massachusetts': 'MA', 'ma': 'MA',  'boston': 'MA', 
        'michigan': 'MI', 'mi': 'MI', 'detroit': 'MI', 'milwaukee': 'MI', 
        'minnesota': 'MN', 'mn': 'MN', 'minneapolis': 'MN',  'paul': 'MN', 'twin': 'MN',   
        'mississippi': 'MS', 'ms': 'MS', 
        'missouri': 'MO', 'louis': 'MO', 'mo': 'MO', 
        'montana': 'MT', 'mt': 'MT', 
        'nebraska': 'NE',  'lincoln': 'NE', 'omaha': 'NE', 'ne': 'NE', 
        'nevada': 'NV', 'vegas': 'NV',  'henderson': 'NV', 'reno': 'NV', 'nv': 'NV', 
        'hampshire': 'NH', 'nh': 'NH',  
        'newark': 'NJ', 'jersey': 'NJ', 'hoboken': 'NJ', 'nj': 'NJ', 
        'mexico': 'NM', 'albuquerque': 'NM', 'abq': 'NM', 'nm': 'NM', 
        'manhattan': 'NY', 'staten': 'NY', 'bronx': 'NY', 'brooklyn': 'NY', 'queens': 'NY', 'buffalo': 'NY',  'rochester': 'NY', 'york': 'NY', 'ny': 'NY', 
        'carolina': 'NC', 'raleigh': 'NC', 'greensboro': 'NC', 'charlotte': 'NC', 'nc': 'NC',  
        'dakota': 'ND',  'nd': 'ND', 
        'ohio': 'OH', 'Toledo': 'OH', 'cleveland': 'OH', 'cincy': 'OH', 'cincinnati': 'OH', 'columbus': 'OH',  'oh': 'OH', 
        'oklahoma': 'OK', 'ok': 'OK',  'tulsa': 'OK',  
        'oregon': 'OR', 'eugene': 'OR', 'portland': 'OR',  'or': 'OR', 
        'pennsylvania': 'PA', 'pittsburgh': 'PA',  'philly': 'PA', 'philadelphia': 'PA', 'pa': 'PA',  
        'rhode': 'RI', 'ri': 'RI', 
        'carolina': 'SC', 'sc': 'SC', 
        'dakota': 'SD', 'sd': 'SD',
        'tennessee': 'TN', 'memphis': 'TN', 'nashville': 'TN', 'tn': 'TN', 
        'texas': 'TX',  'plano': 'TX', 'houston': 'TX', 'dallas': 'TX', 'antonio': 'TX', 'worth': 'TX',  'paso': 'TX', 'arlington': 'TX', 'corpus': 'TX', 'tx': 'TX', 
        'salt': 'UT', 'utah': 'UT', 'ut': 'UT', 
        'vermont': 'VT', 'vt': 'VT',  
        'virginia': 'VA', 'roanoke': 'VA',  'va': 'VA', 
        'washington': 'WA',  'seattle': 'WA', 'wa': 'WA',  
        'west': 'WV', 'wv': 'WV', 
        'wisconsin': 'WI', 'wi': 'WI', 'green': 'WI', 
        'wyoming': 'WY', 'wy': 'WY'}

# a list of state abbreviations
abbrev = ['AL','AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'D.C.', 'FL', 'GA',
 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN',
 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK',
 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY', 'Outside U.S.']
 
# creates a dictionary of the state abbreviations and how many times they were in a tweet's user's location
hits = {'AL': 0,'AK': 0, 'AZ': 0, 'AR': 0, 'CA': 0, 'CO': 0, 'CT': 0, 'DE': 0, 'D.C.': 0, 'FL': 0, 'GA': 0,
 'HI': 0, 'ID': 0, 'IL': 0, 'IN': 0, 'IA': 0, 'KS': 0, 'KY': 0, 'LA': 0, 'ME': 0, 'MD': 0, 'MA': 0, 'MI': 0, 'MN': 0,
 'MS': 0, 'MO': 0, 'MT': 0, 'NE': 0, 'NV': 0, 'NH': 0, 'NJ': 0, 'NM': 0, 'NY': 0, 'NC': 0, 'ND': 0, 'OH': 0, 'OK': 0,
 'OR': 0, 'PA': 0, 'RI': 0, 'SC': 0, 'SD': 0, 'TN': 0, 'TX': 0, 'UT': 0, 'VT': 0, 'VA': 0, 'WA': 0, 'WV': 0, 'WI': 0, 'WY': 0, 'Outside U.S.': 0}
            
# sets a pandas series locations to the tweets' user's locations
locations = tweets[' User Location']

def func(x):
    if type(x) is float:
        return ['Outside U.S.']
    else:
        return x.lower().split()

locations = map(func, locations) 

newLocs = [0 for x in range(len(locations))]

for loc in range(len(locations)):
    for word in locations[loc]:
        if states.get(word, 'Outside U.S.') != 'Outside U.S.':
            newLocs[loc] = states[word]
        else:
            newLocs[loc] = 'Outside U.S.'
            
for state in newLocs:
    if state in abbrev:
        hits[state] = hits.get(state) + 1

        
newDict = {hits[state]: state for state in abbrev}   
series = pd.Series(hits[state] for state in abbrev).order(ascending=False)

# the most active to least active states by tweets
order = [[newDict[num], num] for num in series]
print order