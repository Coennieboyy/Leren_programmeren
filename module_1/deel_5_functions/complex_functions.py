# toets_data has name:score combinations separated by a komma
toets_data = 'Sofie:8,Emma:7,Ahmed:9,Daan:6,Lisa:8,Fatima:7,Ruben:9,Ayoub:6,Bram:6,Maria:7'
separator = ','
position= 8 # position of Bram, first position starts with 0

def get_value(data: str, separator: str, position: int) -> str:
    splitted_strings = data.split(separator) # string splits itself into collection of strings
    if 0 <= position< len(splitted_strings):
        value = splitted_strings[position] # read value at position of split_values
    else:
        value = None
    return value

value = get_value(toets_data, separator, position)
print(value) # prints: Bram:6



import re
# replace alle separators "." , ",", " en ", "omdat ", "zodat ", "want ", " wanneer " en "dat ”by a marker "|"


def replace():
    marked_text = re.sub(r"\.|,|!|\?| en |omdat |zodat |want |wanneer |dat ", "|", text)
    sub_sentences = marked_text.split("|") # split de text on marker "|"
 
def sentence():
    ego_score = 0
    for sentence in sub_sentences: # repeat for every sentence in a list sentences
        sentence = sentence.strip() # remove leading and trailing spaces
        sentence = sentence.lower() # convert uppercase characters to lowercase
        if len(sentence) > 0:
        words = sentence.split(' ') # split sentence into words
        # first words of sentence equal to ik?
        if len(words) >= 2 and (words[0] in ('ik','mijn') or words[1] in ('ik','mijn')):
            ego_score += 1
 
print(ego_score)