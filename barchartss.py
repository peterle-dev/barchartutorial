import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
# importing pyplot from matplotlib


# plt.xkcd()
# builds the plot as comic theme.

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
	language_counter.update(response.split(';'))


languages = []
popularity = []

for item in language_counter.most_common(15):
	languages.append(item[0])
	popularity.append(item[1])

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)



#print(languages)
#print(popularity)




#print(language_counter.most_common(15))

# most_common is a method that counts the most common languages


	#row = next(csv_reader)
	#print(row['LanguagesWorkedWith'].split(';'))


# row = next any beyond helps clean the data for better plotting by separating the values by ;


plt.xlabel("Number of People Who use these Programs")
# plt.ylabel("Number of people in Use")
plt.title("Most Popular Languages")
# The code above sets the descriptions for X and Y

# plt.legend(loc ='upper left')

#plt.grid(True)


#plt.tight_layout()

# plt.savefig('bar.png')

plt.show()

