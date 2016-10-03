"""
This file is used to gather user data for the powerball project.

ver 1.0.0 by Scott Berstler - 10.03.2016
"""

# known issues:
#   if the user hits enter without entering data within the first 2 prompts, the script will throw an exception.
# Note: Due to availability, this script has only been tested on Microsoft Windows 10 with Python 2.7.11 


from sys import argv, stdout

class get():
    
    def __init__(self):
        self.data = {}
        rev = '1.0.0'
    
    def getall(self):
        count = 0
        while 1:
            tmp, ln, fn, one, two, three, four, five, pb =\
                 [], "", "", "", "", "", "", "", ""
            # get first and last name
            fn = self.getFirst()
            if fn == False: break
            else: tmp.append(fn)
            ln = self.getLast()
            if ln == False: break
            else: tmp.append(ln)
              
            # get first 5 numbers
            one = self.getNum1(tmp)
            if one == False: break
            else: tmp.append(one)
            two = self.getNum2(tmp)
            if two == False: break
            else: tmp.append(two)
            three = self.getNum3(tmp)
            if three == False: break
            else: tmp.append(three)
            four = self.getNum4(tmp)
            if four == False: break
            else: tmp.append(four)
            five = self.getNum5(tmp)
            if five == False: break
            else: tmp.append(five)

            # get power ball number
            pb = self.getPB()
            if pb == False:
                break
            else:
                tmp.append(pb)
            count = count+1
            self.data[count] = tmp
        return self.data
#### used produce prompts and validate data fits its respective criteria
    def getLast(self):
        return self.prompt("Please enter the last name: ")

    def getFirst(self):
        return self.prompt("If you are done entering data, hit enter. If you have additional entries, please start by entering the first name: ")

    def getNum1(self, tmp):
        isGoodNum = False
        while 1:
            isGoodNum = self.qualifyNum(self.prompt("Please enter the first number (1-69): "), 69, tmp[2:])
            if isGoodNum != False:
                return isGoodNum
            else:
                self.retry()

    def getNum2(self, tmp):
        isGoodNum = False
        while 1:
            isGoodNum = self.qualifyNum(self.prompt("Please enter the second number (1-69). Please note: this number must be unique. You have already chosen " +\
                                           str(tmp[-1]) + ": "), 69, tmp[2:])
            if isGoodNum != False:
                return isGoodNum
            else: self.retry()

    def getNum3(self, tmp):
        isGoodNum = False
        while 1:
            isGoodNum = self.qualifyNum(self.prompt("Please enter the third number (1-69). Please note: this number must be unique. You have already chosen " +\
                           str(tmp[-2]) + " and " + str(tmp[-1]) + ": "), 69, tmp[2:])
            if isGoodNum != False:
                return isGoodNum
            else: self.retry()

    def getNum4(self, tmp):
        isGoodNum = False
        while 1:
            isGoodNum = self.qualifyNum(self.prompt("Please enter the fourth number (1-69). Please note: this number must be unique. You have already chosen " +\
                           str(tmp[-3]) + " , " + str(tmp[-2])+ " and " + str(tmp[-1]) + ": "), 69, tmp[2:])
            if isGoodNum != False:
                return isGoodNum
            else: self.retry()

    def getNum5(self, tmp):
        isGoodNum = False
        while 1:
            isGoodNum = self.qualifyNum(self.prompt("Please enter the fifth number (1-69). Please note: this number must be unique. You have already chosen " +\
                           str(tmp[-4]) + " , " + str(tmp[-3])  + " , " + str(tmp[-2])+ " and " + str(tmp[-1]) + ": "), 69, tmp[2:])
            if isGoodNum != False:
                return isGoodNum
            else: self.retry()


    def getPB(self):
        isGoodNum = False
        while 1:
            isGoodNum = self.qualifyNum(self.prompt("Please enter the Power Ball. (1-29): "), 29)
            if isGoodNum != False:
                return isGoodNum
            else: self.retry()


    def prompt(self, displayText):
        arg = ""
        # some error detection
        try:
            arg = str(raw_input(str(displayText)))
            if arg == "":
                return False
            else:
                return str(arg)
        except:
            return False
        # return the argument given on the command line

        
    def qualifyNum(self, num, highValue = 69, numListOfUsed = [] ):
        ## Validates nums are 1-X
        try:
            tmpnum, used  = int(num), False
            for l in numListOfUsed:
                if tmpnum == int(l):
                    used = True
                else:
                    pass
            if tmpnum >= 1 and tmpnum <= highValue and used == False:
                return num
            else: return False
        except:
            return False
        
    def retry(self):
        ## gives user prompt the data did not qualify
        stdout.write("Please try again\n")
        stdout.flush()

        
