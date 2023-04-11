# Some important Libraries
import stopwordsiso as stopwords
import nltk 
import pandas as pd
import numpy as np
import seaborn as sns
import colorama
from colorama import Fore
import re
stop_words=stopwords.stopwords("so")
from prettytable import PrettyTable
from texttable import Texttable
import string
import datetime
from iteration_utilities import unique_everseen
wordlist=[];

# load dataset as json format
import json
with open("Lexicon/Lexicon.txt", "r") as file:
    dataset= file.read()
    json_dicti = json.loads(dataset.lower())

# list of Stop Words
extr_StopWords = [
    'waa', 'waana','balse','iyadoo','ma', 'waan','laga','isagoo','la', 'ah', 'oo', 'ee', 'waxey','waxay',
    'lasoo' , 'ugu', 'waxa','uu','eeyga','loo', 'sii','Haddaba', 'haddii','loona','hadda','inkastoo',
     'kula','waxuu', 'uga',  'soo', 'si', 'ku', 'kuu',  'kasoo', 'eey', 'iyo', 'aad', 'baan', 'u', 
    'leh', 'beey', 'ahna','yahay','mana','waxaana','sida','kaddib','dib','maxay','inay','inaan',
     'inaana','inaanay','inaaney','lakin',  'kale','ka', 'inuu', 'in','hadana', 'dhan','ayuu','aaney',
      'ayee',  'ayaa','kala','kule', 'sidoo', 'kalena','aysan', 'laakiin','hor','ayay','kuwaas',
       'wali','isku','halkaasoo','ay','kuna','aan','isla','markaana','ahaanba','iyadoo','inta',
        'aysan','kamid', 'kaasoo','wax' ,'kala','Guud','intaas','Muxuu','awgeed','miyuu','inuu',
        'iska','kamid','kaliya','markiiba','Kuwo','Kuwa','intaysan','wuxuuna','xitaa','kuwee',
         'kuwaas','kuwa','kuwaas','kuwii','intii','intaa','dabadeed','yihiin','gabi','iskaba', 
         'ahaanba','awgii','isugu','kuwaasoo','kaddibna', 'waxba','usoo','lagama','wuu',
        'lamana','lasoo','naga','loogu','aadka','kii','kana','idiin','inoo','aynu','yaa','iney',
        'waxaan','waxaa','waliba','kasta','ilaa','ahayd','waxana','ina','inan','waxaas','maxaad',
         'lagu','wixii','uusan','walba','ahayn','wuxuu','inaga','kuwo','ila','wada','una','xataa',
         'walina','way','inaad','kama','ahaa','lama','kaga','kaas','nagu','aay','ha','aaynu',
         'uma','ayaad','kusoo','aha','sidee','iskugu','kalana','kamida','hore','inkasta','iwm',
          'waxayna','hase','maxaan','ayaana','kahor','kadib','kaa','aheyn' ,'kugu','waxaanu',
           'kan', 'ayey' ,'kaasi',"noo",'iga','iigu','ayayna','inuusan','baannu','looga','idin' ,
           'kadibna','ahaatee','ama','waaye','nooga','isu','kaleba','maxaa','islamarkaana','lagala', 
            'soo','wuxi','kastaba','naloo','walbo','kuma','is','mise','igu','lakiin','baa','yaan'
            ,'nagala','amase','haa','waxaad','idiinku','maxad','kasii','baad','waxan','sidii',
            'kuwaasi','muxuu','iskeed','ula','nugul','horta','intiisa','yeeshee','kusii','uugu','sideen'
            ,'unbuu','looguna','inaanu','markuu','bal',"mooyee",'hadduu','midba','wuxu','waayo','iima','iimaanu',
            'waxsoo','caadiga','innoo','aanad','lala','amma','waad','kuugu','hadii','markaa','hasii','lee','anaan'
            ,'ii','tankale','weeyaan','waase','isoo','haatan','haddana','waxaanay','hadaan','ayna','uuna','inaysan'
                ,'aya','laguna','laguma','ta','inaa','lkn','haku','hasoo','waayahay','kulasoo','laakin','sidaas'
]

# Preprocessing like stop words and duplicate words
try:
    wpt = nltk.WordPunctTokenizer()
    def PreprocessText(doc):
        # lower case and remove special characters\whitespaces
        try:
            doc = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
            doc = doc.lower()
            doc = doc.strip()
        # tokenize document
            tokenized = wpt.tokenize(doc)
        # filter stopwords out of document
            processedText = [tokenized for tokenized in tokenized  if tokenized not in extr_StopWords]
        # re-create document from filtered text
            doc = ' '.join(processedText)
            wordlist=doc.split()
            wordlist = list(set(wordlist)) 
            return wordlist
        except:
            print("")    

except:
    print("normal text was expected!") 

# Rule Based Algorithm
def RuleBasedLemm(word):
    if (word.lower().startswith('miisa') or word.lower().startswith('miisaa') or word.lower().startswith('miisk')):
        return "miis"
    elif word.lower().startswith('cudud'):
        return "cudud"
    elif word.lower().startswith('aasaas'):
        return "aasaas"  
    elif word.lower().startswith("bani"):
         return "bani'aadan"        
    elif word.lower().startswith("hirga"): 
         return "hirgali"        
    elif word.lower().startswith("qaddiya"): 
                 return "qaddiyad"        
    elif word.lower().startswith("baqdaad"): 
                 return "Baqdaad"        
    elif word.lower().startswith("koox"):
                 return "koox"        
    elif word.lower().startswith("sacuudi"):
                 return "sacuudi"        
    elif word.lower().startswith("sacuudi"):
                 return "sacuudi"        
    elif word.lower().startswith("siyaab"):
                 return "siyaabo"        
    elif word.lower().startswith("abuur"):
                 return "abuur"        
    elif word.lower().startswith("fashil"):
                 return "fashil"        
    elif word.lower().startswith("bartam"):
                 return "bartamaha"        
    elif word.lower().startswith("maxall"):
                 return "maxall"        
    elif word.lower().startswith("tiknola") or word.lower().startswith("tiknoloj") or word.lower().startswith("tiknool"): 
                 return "tiknoolaji"        
    elif word.lower().startswith("dhaqdhaqaaq") or word.lower().startswith("dhaqaaq") or word.lower().startswith("dhaqdhaqqay"):
                 return "dhaqdhaqaaq"        
    elif word.lower().startswith("culays"): 
                 return "culays"        
    elif word.lower().startswith("xaadir"): 
                 return "xaadiri"        
    elif word.lower().startswith("ruqsa") or word.lower().startswith("ruqse"): 
                 return "ruqsee"        
    elif word.lower().startswith("saxaf") : 
                 return "saxaafi"        
    elif word.lower().startswith("mihnad") or word.lower().startswith("mihne")  :
                 return "mihnad"        
    elif word.lower().startswith("istaag"): 
                 return "istaag"        
    elif word.lower().startswith("bulsh"): 
                 return "bulsho"        
    elif word.lower().startswith("wargeli"): 
                 return "wargeli"        
    elif word.lower().startswith("gaashaanbuur"): 
                 return "gaashaan"        
    elif word.lower().startswith("go'aan") or word.lower().startswith("go'an") or word.lower().startswith("goan") or word.lower().startswith("goaan") or word.lower().startswith("goaam"):#wargay
                 return "go'aan"        
    elif word.lower().startswith("isbaddal") or word.lower().startswith("isbadal") : 
                 return "isbaddal"        
    elif word.lower().startswith("aaddana")  : 
                 return "aaddan"        
    elif word.lower().startswith("caasimad")  : 
                 return "caasimad"        
    elif word.lower().startswith("caleem")  : 
                 return "caleemasaar"        
    elif word.lower().startswith("mala-awaa")  : 
                 return "mala-awaal"        
    elif word.lower().startswith("todoba")  : 
                 return "todobo"        
    elif word.lower().startswith("khidmad")  : 
                 return "khidmad"        
    elif word.lower().startswith("miisaan")  : 
                 return "miisaan"        
    elif word.lower().startswith("dawlad")  : 
                 return "dawlad"        
    elif word.lower().startswith("ciriir") or  word.lower().startswith("cariri") or  word.lower().startswith("carirsh"):
                 return "ciriiri"        
    elif word.lower().startswith("ajinab") or word.lower().startswith("ajnabi")  : 
                 return "ajinabi"        
    elif word.lower().startswith("aqlabi")  : 
                 return "aqlabiyad"        
    elif word.lower().startswith("diirad")  : 
                 return "diirad"        
    elif word.lower().startswith("cudud")  : 
                 return "cudud"        
    elif word.lower().startswith("gool")  : 
                 return "gool"        
    elif word.lower().startswith("asxaab")  : 
                 return "asxaab"        
    elif word.lower().startswith("milyan") or  word.lower().startswith("malyan") or word.lower().startswith("malaayiin") :#wargay
                 return "milyan"        
    elif word.lower().startswith("horyaal")  : 
                 return "horyaal"        
    elif word.lower().startswith("kaalin")  : 
                 return "kaalin"        
    elif word.lower().startswith("Olomb")  : 
                 return "Olombiko"        
    elif word.lower().startswith("fiic")  : 
                 return "fiicnow"        
    elif word.lower().startswith("abid")  : 
                 return "abid"        
    elif word.lower().startswith("maqaam")  : 
                 return "maqaamsii"        
    elif word.lower().startswith("wacdar")  : 
                 return "wacdaree"        
    elif word.lower().startswith("wanaag") or  word.lower().startswith("wanaaj"): 
                 return "wanaaji"        
    elif word.lower().startswith("cimil")  : 
                 return "cimilo"        
    elif word.lower().startswith("Waxbaro") or  word.lower().startswith("Waxbara") : 
                 return "Waxbaro"        
    elif word.lower().startswith("taleefoon") or  word.lower().startswith("talefoon") or word.lower().startswith("talefon") : 
                 return "taleefoon"        
    elif word.lower().startswith("saaxiib")  : 
                 return "saaxiib"        
    elif word.lower().startswith("dalxiis"):
                 return "dalxiis"        
    elif word.lower().startswith("madaaf") or word.lower().startswith("madfac"):
                 return "madfac"        
    elif word.lower().startswith("Cashar") or word.lower().startswith("Cashir") :
                 return "Cashar"        
    elif word.lower().startswith("macsalaa"):
                 return "macsalaamee"        
    elif word.lower().startswith("hamuun"):
                 return "hamuun"  
    elif word.lower().startswith("firir"):
                 return "firir"  
    elif word.lower().startswith("agagaar"):
                 return "agagaarkee"  
    elif word.lower().startswith("dhufeys") or word.lower().startswith("dhufays"):
                 return "dhufays"  
    elif word.lower().startswith("muxaadi") or word.lower().startswith("muxaada"):
                 return "muxaadaree"  
    elif word.lower().startswith("bulsha"):
                 return "bulsho"  
    elif word.lower().startswith("fanaan") or  word.lower().startswith("fannaan") :
                 return "fanaan"  
    elif word.lower().startswith("waydaari") or word.lower().startswith("waydaars") or word.lower().startswith("iswaydaars") :
                 return "waydaari" 
    elif word.lower().startswith("shaac"):
                 return "shaaci"   
    elif word.lower().startswith("sooyaal"):
                 return "sooyaal"   
    elif word.lower().startswith("islaam"):
                 return "islaam"   
    elif word.lower().startswith("khudbad") or word.lower().startswith("khudbe"):
                 return "khudbee"   
    elif word.lower().startswith("seynis"):
                 return "seynis"   
    elif word.lower().startswith("culim") or word.lower().startswith("culama") :
                 return "culimo"   
    elif word.lower().startswith("kumaand"):
                 return "kumaandoos"   
    elif word.lower().startswith("federaal"):
                 return "federaal"   
    elif word.lower().startswith("baasaboor"):
                 return "baasaboor"   
    elif word.lower().startswith("ilaali"):
                 return "ilaali"   
    elif word.lower().startswith("shirkad"):
                 return "shirkad"   
    elif word.lower().startswith("cashir") or word.lower().startswith("cashar"):
                 return "cashar"   
    elif word.lower().startswith("mudaaharaad") or word.lower().startswith("mudaharaad"):
                 return "mudaharaad"   
    elif word.lower().startswith("dastuur"):
                 return "dastuur"  
    elif word.lower().startswith("mudaaharaad") or word.lower().startswith("mudaharaad"):
                 return "mudaharaad"  
    elif word.lower().startswith("faahfaah"):
                 return "faahfaahi"  
    elif word.lower().startswith("xayaysii") or word.lower().startswith("xayeysii"):
                 return "xayaysii"  
    elif word.lower().startswith("isbuuc") or word.lower().startswith("asbuuc"):
                 return "isbuuc"  
    elif word.lower().startswith("xanaaji") or word.lower().startswith("xanaaj"):
                 return "xanaaji"  
    elif word.lower().startswith("maami") or word.lower().startswith("maam"):
                 return "maamo"  
    elif word.lower().startswith("islaant") or word.lower().startswith("islaamo"):
                 return "islaan"  
    elif word.lower().startswith("barnaamij"):
                 return "barnaamij"  
    elif word.lower().startswith("idinsi"):
                 return "sii"  
    elif word.lower().startswith("allah") or word.lower().startswith("alah") or  word.lower().startswith("ilaah"):
                 return "allah"  
    elif word.lower().startswith("majaaj"):
                 return "majaajilee"  
    elif word.lower().startswith("galmudug"):
                 return "galmudug"  
    elif word.lower().startswith("agoon"):
                 return "agoon"  
    elif word.lower().startswith("iskaan"):
                 return "iskaan"  
    elif word.lower().startswith("hormuud"):
                 return "hormuud"  
    elif word.lower().startswith("dahabshiil"):
                 return "dahabshiil"  
    elif word.lower().startswith("maalgash") or word.lower().startswith("maalgal") :
                 return "maalgali"  
    elif word.lower().startswith("astaan"):
                 return "astaan"  
    elif word.lower().startswith("masiir"):
                 return "masiir"  
    elif word.lower().startswith("natiij"):
                 return "natiijo"  
    elif word.lower().startswith("sharci"):
                 return "sharci"  
    elif word.lower().startswith("qaxooti"):
                 return "qaxooti"  
    elif word.lower().startswith("koonfur"):
                 return "koonfur"  
    elif word.lower().startswith("abdifatah") or word.lower().startswith("cabdif") :
                 return "cabdifitah"  
    elif word.lower().startswith("jilic") or word.lower().startswith("jileec") :
                 return "jilci"
    elif word.lower().startswith("umad"):
                 return "umad"    
    elif word.lower().startswith("qorsh"):
                 return "qorshee" 
    elif word.lower().startswith("lix"):
                 return "lix" 
    elif word.lower().startswith("maskax"):
                 return "maskax" 
    elif word.lower().startswith("shakhs"):
                 return "shakhsi" 
    elif word.lower().startswith("akhri"):
                 return "akhri" 
    elif word.__contains__("wadaag"):
                 return "lawadaag" 
    elif word.__contains__("ramadaan"):
                 return "ramadaan" 
    elif word.__contains__("ogays") or word.__contains__("ogeys"):
                 return "ogeysii" 
    elif word.__contains__("maadaam") or word.__contains__("madaam"):
                 return "maadaama" 
    elif word.__contains__("dabar"):
                 return "dabar" 
    elif word.__contains__("gaari"):
                 return "gaari" 
    elif word.__contains__("sxb") or word.__contains__("saaxiib"):
                 return "saaxiib" 
    elif word.__contains__("anfac"):
                 return "anfac" 
    elif word.lower().startswith("ali") or word.lower().startswith("cali") :
                 return "cali" 
    elif word.__contains__("imtixaan") or word.__contains__("itixaan"):
                 return "imtixaan" 
    elif word.__contains__("warqad") or word.__contains__("waraaq"):
                 return "warqad" 
    elif word.lower().startswith("shukran") or word.lower().startswith("shugran") :
                 return "shukran" 
    elif word.__contains__("cabir"): 
                 return "cabir" 
    elif word.__contains__("baahi") or word.__contains__("baahan"):
                 return "baahi" 
    elif word.__contains__("xirfad"):
                 return "xirfad" 
    elif word.__contains__("khalkhal"):
                 return "khalkhali" 
    elif word.__contains__("khudaar"):
                 return "khudaar" 
        
# Processing Method for Lemmatizing and Statistics
try:
## this method does processing text to root word utiliting method of RuleBasedLemm and lexicon data  
    def Process(items,doc):
        notFoundWords=[] # used for getting unresolved word to print
        dict_check=[] # used for preventing duplicate value of document
        ruleCheck=[] # used for preventing duplicate value of RuleBasedLemm
        document = re.sub(r'[^a-zA-Z0-9\s]', '', doc, re.I|re.A)
        resolvedCounter=0
        test=0
        totalValues=0
        keys=0
        resovledwordText="Resolved words"
        try:
            dict_check.clear()
            ruleCheck.clear()
            start_time = datetime.datetime.now()
            print (resovledwordText.center(40, '#'))
            for word in items:
                for key, values in json_dicti.items():
                    totalValues=totalValues+1
                    keys=len(key)
                    if(isinstance(values, list)):
                        if word.lower() in values and word.lower()  not in dict_check:
                            print(key)
                            dict_check.append(word.lower())
                            resolvedCounter=resolvedCounter+1 
                if RuleBasedLemm(word) and RuleBasedLemm(word)  is not None and word  not in ruleCheck and word not in dict_check:
                    print(RuleBasedLemm(word))
                    ruleCheck.append(word)
                    resolvedCounter=resolvedCounter+1
            t = Texttable()
            tokenizeDoc = wpt.tokenize(doc)
        # filter stopwords out of document
            stopWordsText = [tokenizeDoc for tokenizeDoc in tokenizeDoc  if tokenizeDoc  in extr_StopWords]
            specialchars=0 #propose of special characters
           
            for tt in tokenizeDoc:
                if tt in string.punctuation:
                    specialchars=specialchars+1
            origindoc=len(stopWordsText)+resolvedCounter+len(items)-resolvedCounter+specialchars
            totalfound=str(round((resolvedCounter/len(items)*100),2))
            t.add_row(['Origin Docs size in words', origindoc])
            t.add_row(['stop Words(non-unique)', len(stopWordsText)])
            t.add_row(['special characters',specialchars])
            t.add_row(['Unresolved words', len(items)-resolvedCounter])
            t.add_row(['Resolved words', resolvedCounter])
            t.add_row(['percent found', str(round((resolvedCounter/len(items)*100),2))+"%"])
            t.add_row(['words from lexicon', len(dict_check)])
            t.add_row(['words from rule based', len(ruleCheck)])

            print(t.draw())
            notFoundWords.clear()
            cstr = " Displaying Unresolved Word "
            print (cstr.center(40, '#'))
            for word in items:
                if word.lower() not in dict_check and word.lower() not in ruleCheck:
                #if word in dict_check:
                    print(word.lower())
                    test=test+1
                    notFoundWords.append(word.lower())
            print(len(dict_check))
            print(len(ruleCheck))
            print(len(notFoundWords))
            dict_check.clear()
            ruleCheck.clear()
            end_time = datetime.datetime.now()
            performance="  Time taken : " # text displaying before time taken
            print (performance.center(10, '#'),end_time-start_time)
            #return totalfound
        except:
            print("normal text was expected!") 
except:
    print("") 

# Lemmatize Method 
def Lemmatize(document):
    return Process(PreprocessText(document),document)

# checking if provided text is dataframe format
def DataFrameFormat(text):
    for index, row in text.iterrows():
        Lemmatizer(row['text'])

# callee Method by using previuos Methods
def Lemmatizer(document):
    if isinstance(document, pd.DataFrame):
        return DataFrameFormat(document)
    else:
        return Lemmatize(document)
