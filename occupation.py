def runfile():
    fie= open("occupations.csv", 'r')
    fie.readline()
    textLines=fie.read()
    splitLines=[]
    for line in fie:
        splitLines.append(line.split(','))
    print splitLines
    data={}
    
