filename='[file name with path]'

import datetime
def timenow():
    time=datetime.datetime.now()
    timevalue=float(time.hour*60+time.minute+time.second/60)
    return timevalue

paragraph = ''
f = open(filename,'r',encoding="ISO-8859-1")
#f = open(filename,'r',encoding="utf8")
data = f.read()
totalwords = len(data.split())

A=0
B=0
C=0
R=0
count=0

with open(filename, encoding="utf8", errors='ignore') as f:
    lines = f.readlines()
for line in lines:
    if line.isspace():  # is it an empty line?
        #print ("hello")
        if paragraph:
            #print ("hello there")
            count=count+1
            print ("Paragraph: ", count)
            a=timenow()
            A=A+a
            print (paragraph)
            res = len(paragraph.split())
            input("Press Enter to continue....")
            b=timenow()
            B=B+b
            c=res/(b-a)
            R=R+res
            C=R/(B-A)
            balancetimeestimate=(totalwords-R)/C
            totaltimeestimate=B-A+balancetimeestimate
            print()
            print (res ,"words in",'{:.2f}'.format(b-a),"minutes =",'{:.0f}'.format(c)," wpm")
            print ("Average ",'{:.0f}'.format(C),"wpm")
            print ("Remaining words: ", (totalwords-R))
            print ("Remaining time estimate: ",'{:.1f}'.format(balancetimeestimate),"min")
            print ("Total time estimate: ",'{:.1f}'.format(totaltimeestimate),"min")
            #input("Press Enter to continue2...")
            print(".....................................................")
            print()
            paragraph = ''
        else:
            continue
    else:
        paragraph += ' ' + line.strip()
count=count+1
print ("Paragraph: ", count)
a=timenow()
input("Press Enter to continue...")
A=A+a
print (paragraph)
res = len(paragraph.split())
input("Press Enter to finish...")
b=timenow()
B=B+b
c=res/(b-a)
R=R+res
C=R/(B-A)
balancetimeestimate=(totalwords-R)/C
totaltimeestimate=B-A+balancetimeestimate
print()
print (res ,"words in",'{:.2f}'.format(b-a),"minutes =",'{:.0f}'.format(c)," wpm")
print ("Average ",'{:.0f}'.format(C),"wpm")
print ("Remaining time estimate: ",'{:.1f}'.format(balancetimeestimate),"min")
print ("Total time estimate: ",'{:.1f}'.format(totaltimeestimate),"min")
print(".........Page Over...............................................")
