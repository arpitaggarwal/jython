def readFile():
    f=open('/Users/ArpitAggarwal/workspace/jython-basics/com/test.csv', 'r')
    print f
    for line in f:
        print line.rstrip()
    f.close

def copyCSVToTextFile():
    f=open('/Users/ArpitAggarwal/workspace/jython-basics/com/test.csv', 'r')
    output = open('/Users/ArpitAggarwal/workspace/jython-basics/com/test.txt', 'w')
    for line in f:
        output.write(line.rstrip() + '\n')
    f.close()
    
    
readFile()
copyCSVToTextFile()
