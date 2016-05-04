import re
def add(a,b):
    return a+b

def addFixedValue(a):
    y = 5
    return y +a
  
print add(1,2)
print addFixedValue(1)

def dictionaryCheck():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'};
    print "dict['Name']: ", dict['Name'] 
    print "dict['Age']: ", dict['Age']
   
    
dictionaryCheck()

string = 'JBAS'
stringnew = 'WFLYCTL0030'
def regexCheck():
    if re.search("WFLY[A-Z0-9]+|JBAS[0-9]+", string):
        print"Regex : %s" % re.search("WFLY[A-Z0-9]+|JBAS[0-9]+", string)
    else:
        print"False " 
    
regexCheck()