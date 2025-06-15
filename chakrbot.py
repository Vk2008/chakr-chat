import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import contractions
import pandas
from datetime import date

def chakr_chat(user_input):
    greet =['hi', 'hello', 'hey', 'greet', 'chakr', 'chat']
    bid = ['bye', 'thankyou', 'thank']
    relief_str = ['relief', 'camp', 'food', 'stay', 'rescue', 'operation']
    help_str = ['help', 'ndrf', 'save', 'helpline', 'number']
    insurance_str = ['insurance', 'money', 'claim', 'renewal']
    updates_str = ['updat', 'news', 'today', 'condition'] #'updat' --stemmer returns it in this format
    train_str = ['train', 'railway', 'cancel', 'schedule', 'station']

    #text-normalisation
    user_input = user_input.lower()
    contr_remv = contractions.fix(user_input) #fixes contractions

    #punctuation eliminator
    punc = '' #string after removing puntuations
    for char in contr_remv:
        if char.isalnum() == True or char.isspace() == True:
            punc += char

    #tokenization
    tokens = word_tokenize(punc) #list of words

    #stop-word removal
    sw = set(stopwords.words('english')) #omit repetitions
    n_tokens = []
    for word in tokens:
        if word not in sw:
            n_tokens.append(word)

    #stemming lemmatization
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    text_s = []
    text_l = []
    for word in n_tokens:
        text_s.append(stemmer.stem(word))
        text_l.append(lemmatizer.lemmatize(word))
    text = text_s + text_l

    for i in text:
        if i in greet:
            return 'Chakr-Chat activated. How can I help You?'
        
        elif i in relief_str:
            relief_data = pandas.read_csv('relief.csv')

            print('Chakr-Chat: Enter your ward number') 
            ward = int(input('You: '))
            
            for i in range(0,200): #work static, can be changed as required
                if relief_data.iloc[i,0] == ward:
                    print('Chakr-Chat: As per my latest update, you should go to')
                    return relief_data.iloc[i,1]
        
        elif i in help_str:

            print('Chakr-Chat: State Disaster Manangement Authority Helpline: 1070')
            print('Chakr-Chat: Whatsapp: 9445869848')
            print('Chakr-Chat: NDRF Helpline Number: +91-9711077372')
            file = open('help.txt')
            content = file.readlines()

            print('Chakr-Chat: Enter your pincode') 
            pin = (input('You: '))
            for i in range(0,13):
                if content[i][0:6] == (pin):
                    return 'Pin Code', content[i].rstrip('\n')

                
        elif i in insurance_str:
            

            print('Chakr-Chat: Flood-damaged vehicles are covered under motor insurance policies. Claims can be made for own damage, third-party liability, and total loss.')
            print('Chakr-Chat: Enter your insurance company')
            comp = input('You: ')

            if 'icici' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Report. Once reported, you\'ll be assigned a dedicated Claim Manager.', 'Provide approval to the Claim Assessment', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document loss, please type RELIEF. For more: 1800 2666'
            
            elif 'acko' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Raise claim through Acko app', 'Your vehicle will be collected', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement', 'Original Purchase Invoice',sep ='\n')
                return 'In case of document loss, please type RELIEF. For more: 1800 266 2256'
    
            elif 'sundaram' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Inform about the claim. You\'ll be contacted by them further', sep = '\n')
                print('Chakr-Chat: Documents Required','Claim Form','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document loss, please type RELIEF. For more: 18005689999'
            
            elif 'cholamandalam' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Request for Claim Intiation', 'INspection', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document loss, please type RELIEF. For more: 1800 208 5544'
            
            elif 'hdfc' in comp.lower():
                print('Chakr-Chat: Steps to Claim', 'Register claim', 'Wait for claim approval', sep = '\n')
                print('Chakr-Chat: Documents Required','Identity Proof','RC of vehicle','Driving License','Agreement',sep ='\n')
                return 'In case of document loss, please type RELIEF. For more: 022 6234 6234'
            
            else:
                return 'The company is not yet associated with Chakr-Chat. I recommend visiting their website.'
            
        elif i in train_str:
            train_data = pandas.read_csv('train_data.csv')
            print('Chakr-Chat: I\'ll need your train number to help you navigate')
            train_no = input('You: ')
            if train_no[0] == '0':
                train_no = train_no[1:]
            tn = int(train_no)
            info = train_data[train_data['train_no'] == tn]
            if len(info) != 0:
                print('Chakr-Chat: \n', info.head())
            return 'You can visit https://scr.indianrailways.gov.in/ for more details'        
        
        elif i in updates_str:
            today = str(date.today()) #default dtype class datetime date
            file = open('update.txt')
            news = file.readlines()
            for i in range(len(news)):
                if str(news[i][:-1]) == today:
                    print('Chakr-Chat: ', today, 'Headlines')
                    a = i
                else:
                    a = 0
            n = sent_tokenize(news[a+1])
            for j in n:
                print(j)
            return 'Stay Safe'
                            
        elif i in bid:
            return 'Thank You for being with Chakr-Chat. Be Safe!'


def main():
    while True:
        user_input = input('You: ')

        response = chakr_chat(user_input)
        if response == None:
            response = 'Stay Safe'
        print('Chakr-Chat:', response)

## if __name__ == '__main__': #__name__ built-in python variable, when script is executed __name__ is set to __main__ by default
##    main() 

main()