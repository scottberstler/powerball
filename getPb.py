"""
This file is used to track user data, and figure out what the winning # is.
ver 1.0.0 by Scott Berstler - 10.03.2016
"""

# known issues:
#   if the user hits enter without entering data within the first 2 prompts, the script will throw an exception.
# Note: Due to availability, this script has only been tested on Microsoft Windows 10 with Python 2.7.11 




from random import Random

class values:
    pbnum = {}
    first5nums = {}
    returnlist = []
    
class makecount():

    def __init__(self, masterd):
        self.iterateinput(masterd)
        
    
    def iterateinput(self, masterd):
        # go through collected data
        pb = 0
        for v in masterd.itervalues():
            # find the 1st 5 # and the PB
            self.count5(v)
            pb = self.countpb(v)
        values.returnlist.extend(self.first5())
        values.returnlist.insert(len(values.returnlist),pb)

    def countpb(self,numl):
        # count how many unique PB # and priorize for the winning #
        r = Random()
        num , high, tmp = numl[-1], 0, []
        if values.pbnum.has_key(num) == True:
            newval = values.pbnum.get(num) + 1
            values.pbnum[num] = newval
        else:
            values.pbnum[num] = 1
        high = sorted(list(set(values.pbnum.values())), reverse = True)[0]
        for k in  values.pbnum.iteritems():
            if k[1] == high:
                tmp.append(k[0])
        return int(tmp[(r.randint(1, len(tmp)))-1])
        
    
    def count5(self,numl):
        # count the unique #
        for num in (numl[-6], numl[-5], numl[-4], numl[-3], numl[-2]):
            if values.first5nums.has_key(num) == True:
                newval = values.first5nums.get(num) + 1
                values.first5nums[num] = newval
            else:
                values.first5nums[num] = 1

    def first5(self):
        # prioritize the 1st 5 # 
        f5 , f5, hm = 0, [], 5
        t = sorted(list(set(values.first5nums.values())), reverse = True)
        if len(t) < hm:
            while len(t) > hm:
                t.append(t[-1])
        elif len(t) > hm:
            t = t[:hm]
        else:
            pass
        f5.extend(self.pickval(f5, t,hm))
        return sorted(f5)
                      
    def pickval(self, existingd, numsl, quantity):
        # get the int with the highest priorities for the 1st 5 and randomly choose from #'s with conflicts
        r = Random()
        temp, final = [], []
        for num in numsl:
            for d in values.first5nums.iteritems():
                if d[1] == num:
                    temp.append(d[0])
            while 1:
                re = r.randint(1, len(temp))
                final.append(int(temp.pop(re-1)))
                if len(final) == quantity or len(temp) == 0 or len(existingd) == quantity:
                    break
                else:
                    pass     
        return final
                         
