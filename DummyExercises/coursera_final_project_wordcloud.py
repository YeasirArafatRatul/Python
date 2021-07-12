
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys
#import wikipedia



'''

# get path to script's directory
currdir = path.dirname(__file__)

def get_wiki(query):
	# get best matching title for given query
	title = wikipedia.search(query)[0]

	# get wikipedia page for selected title
	page = wikipedia.page(title)
	return page.content


def create_wordcloud(text):
	# create numpy araay for wordcloud mask image
	mask = np.array(Image.open(path.join(currdir, "cloud.png")))

	# create set of stopwords	
	stopwords = set(STOPWORDS)

	# create wordcloud object
	cloud = WordCloud(background_color="white",
					max_words=200, 
					mask=mask,
	               	stopwords=stopwords)
	
	# generate wordcloud
	cloud.generate(text)

	# save wordcloud
	cloud.to_file("myfile.jpg")


if __name__ == "__main__":
	# get query
	query = sys.argv[1]

	# get text for given query
	text = get_wiki(query)
	
	# generate wordcloud
	create_wordcloud(text)
'''

#for creating wordcloud
#cloud = wordcloud.WordCloud()
#cloud.generate_from_frequencies(frequencies)
#cloud.to_file("myfile.jpg")



def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    
    # LEARNER CODE START HERE
    file_words=[]
    words_frequencies={}
    count=0
    #removing punctuations
    for punctuation in punctuations:
        if punctuation in file_contents:
            file_contents=file_contents.replace(punctuation,"",len(file_contents))
    file_words=file_contents.split()
    
    for word in file_words:
        if word.lower() in words_frequencies or word.lower() not in uninteresting_words:
            count += 1
            words_frequencies[word] = count

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(words_frequencies)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()


