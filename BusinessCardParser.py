import re
import requests
import nltk

def inputData():
    finished = False
    text = []
    counter = 1
    print('Input each line from the OCR results and press ENTER.\nWhen you are done simply hit ENTER\n')
    while finished== False:
        line = input(f'Input line {counter} from OCR resuts:')
        text.append(line)
        counter +=1
        if line == '':
            finished = True
    #droping the last item from the list as it is just a empty string       
    text = text[:-1]
    return text

def parse_person(line):
    names = []
    #using the NTLK parts of speach model to check for people.
    for i, chunk in enumerate(nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(line)))):
        if type(chunk) == nltk.tree.Tree:
            if chunk.label() == 'PERSON':
                names.append(chunk[0][0])
    '''
    The above code works great for English names.  However it struggled to identify the non-anglo surname 'Haung'.
    Therefore I added this code to grab the second word after an NLTK identified person.  
    To solve the non-anglo problem effecently you would want to retrain a word net underlying NLTK to include 
    a more comprehensive list of global names. 
    
    A potential bug in this code is that it would extract a company such as "Kellys Carpets" as a name.
    Addationally,  it does not account for potential middle names.  
    '''
    if len(names)==1:
        names.append(line.split(' ')[i])
    return ' '.join(names)
        
def getName(text):
    for line in text:
        person = parse_person(line)
        if person:
            return('Name: '+person) 

        
def getPhoneNumber(text):
    #joining list together because regex's are expensive and this way we only run it one vs. several. 
    text = ' '.join(text)
    #Writing regex to grab the first 5 characters before the phone number to ensure we do not grab a fax number
    phone_pattern = re.compile(r'((?:.{5})(?:\+1\s)?[\(]?\d{3}[\)|-]\s?\d{3}[-|\s]\d{4})')
    #matching the pattern and grabbing the second capture group which is the number
    number =re.findall(phone_pattern, text)
    #only selecting the numbers that are not labeled as a fax.
    number = [x[5:] for x in number if 'Fax' not in x][0]
    #cleaning the number by removing any non-digits
    number = re.sub(r'\D','',number)
    return('Phone: '+number)

def getEmailAddress(text):
    #joining list together because regex's are expensive and this way we only run it one vs. several. 
    text = ' '.join(text)
    #simple regex for email limiting the size of each component to 255 out of habit as regex's are expensive. 
    emailPattern = re.compile(r'\s((?:\w|\.){1,255}@\w{1,255}\.\w{1,255})')
    email = re.findall(emailPattern, text)
    return('Email: '+email[0].strip())

def getContactInfo():
    text = inputData()
    print('\n\nYour contact information is below:\n\n')
    print(getName(text))
    print(getPhoneNumber(text))
    print(getEmailAddress(text))
    
getContactInfo()