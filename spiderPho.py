# retrieve phonteic transcription of English words

from urllib import urlopen
from bs4 import BeautifulSoup
import re


lang = raw_input("English, French, Italian, Spanish, or Portuguese? ")
input_type = "word"
word1 = "word"
word2 = "word"

def choose_lang(lang):
    """Choose language and input type: word or list"""
    global input_type
    if lang == "English" or lang == "english":
        print ""
        input_type = raw_input("Ok, English. List or word? ")
        spiderEng(input_type)
        print ""
    elif lang == "French" or lang == "french":
        #print ""
        #input_type = raw_input("Ok, French. List or word? ")
        spiderFra(input_type)
        #print ""
    elif lang == "Italian" or lang == "italian":
        print ""
        input_type = raw_input("Ok, Italian. List or word? ")
        spiderIta(input_type)
        print ""
    elif lang == "Spanish" or lang == "spanish":
        #print ""
        #input_type = raw_input("Ok, Spanish. List or word? ")
        spiderSpa(input_type)
        #print ""
    elif lang == "Portuguese" or lang == "portuguese":
        print ""
        input_type = raw_input("Ok, Portuguese. List or word? ")
        spiderPor(input_type)
        print ""
    else:
        print "Language choice error."

def spiderEng(input_type):
    if input_type == "word" or input_type == "Word":
        print ""
        entered_word = raw_input("Enter word: ")
        url = ('http://www.merriam-webster.com/dictionary/' + entered_word)
        ourUrl = urlopen(url).read()
        soup = BeautifulSoup(ourUrl)
        body = soup.find('span', {"class":'pr'})
        body.encode('utf-8')
        print ""
        print body.text.encode('utf-8')
        print ""
    elif input_type == "list" or input_type == "List":
        print ""
        data_file_name = raw_input("Enter name of data file: ")
        word = list(open(data_file_name))
        for phono in word:
            url = ('http://www.merriam-webster.com/dictionary/' + phono)
            ourUrl = urlopen(url).read()
            soup = BeautifulSoup(ourUrl)
            body = soup.find('span', {"class":'pr'})
            body.encode('utf-8')
            print ""
            print body.text.encode('utf-8')
            print ""
    else:
        print ""
        print "Huh? "
        choose_lang("English")

def spiderFra(input_type):
    print ""
    print "French is momentarily out of order."
    print ""
    retry_lang = raw_input("Try another language: ")
    choose_lang(retry_lang)
        
def spiderSpa(input_type):
    print ""
    print "Spanish is momentarily out of order."
    print ""
    retry_lang = raw_input("Try another language: ")
    choose_lang(retry_lang)

def spiderIta(input_type):
    if input_type == "word" or input_type == "Word":
        print ""
        entered_word = raw_input("Enter word: ")
    	url = ('http://www.collinsdictionary.com/dictionary/italian-english/' + entered_word)
    	ourUrl = urlopen(url).read()
    	soup = BeautifulSoup(ourUrl)
    	body = soup.find('span', {"class":'pron'})
    	body.encode('utf-8')
        print ""
    	print body.text.encode('utf-8')
        print ""
    elif input_type == "list" or input_type == "List":
        print ""
        data_file_name = raw_input("Enter name of data file: ")
        word = list(open(data_file_name))
        for phono in word:
            url = ('http://www.collinsdictionary.com/dictionary/italian-english/' + phono)
            ourUrl = urlopen(url).read()
            soup = BeautifulSoup(ourUrl)
            body = soup.find('span', {"class":'pron'})
            body.encode('utf-8')
            print ""
            print body.text.encode('utf-8')
            print ""
    else:
        print ""
        print "Huh? "
        choose_lang("Italian")


def spiderPor(input_type):
    if input_type == "word" or input_type == "Word":
        print ""
        entered_word = raw_input("Enter word: ")
    	url = ('http://pt.pons.eu/dict/search/results/?q=' + entered_word + '&l=espt&in=pt&lf=pt')
    	ourUrl = urlopen(url).read()
    	soup = BeautifulSoup(ourUrl)
    	body = soup.find('span', {"class":'phonetics'})
        print ""
        print body.text
        print ""
    elif input_type == "list" or input_type == "List":
        print ""
        data_file_name = raw_input("Enter name of data file: ")
        word = list(open(data_file_name))
        for phono in word:
    	    url = ('http://pt.pons.eu/dict/search/results/?q=' + phono + '&l=espt&in=pt&lf=pt')
    	    ourUrl = urlopen(url).read()
    	    soup = BeautifulSoup(ourUrl)
    	    body = soup.find('span', {"class":'phonetics'})
            print ""
    	    print body.text
            print ""
    else: 
        print ""
        print "Huh? "
        choose_lang("Portuguese")
        
def levenshtein(s1, s2):
    l1 = len(s1)
    l2 = len(s2)

    matrix = [range(l1 + 1)] * (l2 + 1)
    for zz in range(l2 + 1):
      matrix[zz] = range(zz,zz + l1 + 1)
    for zz in range(0,l2):
      for sz in range(0,l1):
        if s1[sz] == s2[zz]:
          matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz])
        else:
          matrix[zz+1][sz+1] = min(matrix[zz+1][sz] + 1, matrix[zz][sz+1] + 1, matrix[zz][sz] + 1)
    return matrix[l2][l1]

def measure_pho_distance(yes_or_no):
    global word2
    if yes_or_no == "Yes" or yes_or_no == "yes":
        lang_choice_two = raw_input("Which language? ")
        choose_lang(lang_choice_two)
        input_type = "word"
        word2 = word1
        LD = levenshtein(word1, word2)
        print "First word: " + word1
        print "Second word: " + word2
        print "LD: ", LD
    elif yes_or_no == "No":
        pass
    else:
        print "LD fuxed."
        
       
        
choose_lang(lang)
#yes_or_no = raw_input("Compute the Levenshtein distance with a word from another language? ")
#measure_pho_distance(yes_or_no)
