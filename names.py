import random
def takuto():
    #returns a random user's id
    lens = [163282074466385921,126745243352563712,266035355013218304,570100493444055041,721133046874767410]
    name = ["takuto","allie","guen","mark","marlo"]
    who = random.randint(0,len(lens)-1)
    return lens[who]