#AS OF MAY 27 Current Data. Also format of CSV file
#Age	  Case Count	Death Count	   Underlying Conditions
#0-17	    5370	    10          	8
#18-44	    72173	    651	            536
#45-64  	71691	    3728	        3306
#65-74  	24521   	4140	        3629
#75+	    23181	    8081	        6900
import pandas as pd

class CoronaMortalityCalc:
    def calculateProbability(age,condition,caseCount,deathCount,underLying,):
        if(age<=17 and condition ==0):
            return (deathCount[0] - underLying[0])/caseCount[0]
        elif(age<=17 and condition ==1):
            return underLying[0]/caseCount[0]

        elif(age<=44 and condition ==0):
            return (deathCount[1] - underLying[1])/caseCount[1]
        elif(age<=44 and condition ==1):
            return underLying[1]/caseCount[1]

        elif(age<=64 and condition ==0):
            return (deathCount[2] - underLying[2])/caseCount[2]
        elif(age<=64 and condition ==1):
            return underLying[2]/caseCount[2]

        elif(age<=74 and condition ==0):
            return (deathCount[3] - underLying[3])/caseCount[3]
        elif(age<=74 and condition ==1):
            return underLying[3]/caseCount[3]

        elif( condition ==0):
            return (deathCount[4] - underLying[4])/caseCount[4]
        elif(condition ==1):
            return underLying[4]/caseCount[4]

    if __name__ == '__main__':
        colList = ["Age","Case Count","Death Count","Confirmed Underlying Conditions"]
        df = pd.read_csv("data.csv",usecols=colList)
        ageRanges = df["Age"]
        caseCount = df["Case Count"]
        deathCount = df["Death Count"]
        underLying = df["Confirmed Underlying Conditions"]
        inputAge = int(input("Enter your Age"))
        inputUnderlyingCondition = (input("Do you have a health condition(Y/N)" ))
        if(inputUnderlyingCondition.upper()=="Y"):
            inputUnderlyingCondition=1
        else:
            inputUnderlyingCondition=0

        print("The mortality rate for your inputs is")
        print(calculateProbability(inputAge,inputUnderlyingCondition,caseCount,deathCount,underLying)*100)
        print("NOTE: CDC DATA DOES NOT DISCLOSE THE NUMBER OF CLOSED CASES. THIS MEANS THAT ACTIVE CASES ARE INCLUDED\nTHUS DECREASING THE MORTALITY RATE.\n")

    