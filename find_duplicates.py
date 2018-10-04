f = open("/home/dhanya/Downloads/TwitterProject/data/example-search-tweepy-2-2018-10-04.txt","r")
content = f.readlines()
"""count=0
for i in range(len(content)):
    for j in range(len(content)):
        if(content[i]==content[j] and i!=j):
            count+=1
"""
print len(list(set(content)))
print len(content)
