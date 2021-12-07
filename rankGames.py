'''
This code is written by SK Mbatha.
Date: 06-12-2021 20:00
Description:  This code is to be used for a coding challenge test
              by SPAN. This is for recruiment purposes.
'''

import sys
import os

# Define a terminal clear function
def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')

class rankGames:
    
    inputData=[] # Create a list if strings to hold the score input data
    resultTeamNames=[] # List to hold the acquired team names
    resultTeamPoints=[] # List to hold the acquired team points
    sortedTeamNames=[] # List to hold the sorted (by points and alphabetically) team names
    sortedTeamPoints=[] # List to hold the sorted (by points and alphabetically) team points
    
    
    @classmethod
    def _getInput(self):
        '''
        This function loads a list of  input files from command line inputs only if they were provided
        otherwise it asks for input data from the user through 'stdin'.
        Each line of games' scores is saved in the list: rankGames.inputData (list of Strings)
        '''
        
        if len(sys.argv)>1: 
        
            # If there are multiple file names supplies get game results from each
            for i in range(1,len(sys.argv)):
                file=open(sys.argv[i],'r')
                gameResults=file.readlines()
                file.close()
                
                #append each result to the input
                for result in gameResults:
                    rankGames.inputData.append(str(result).replace('\n',''))
            
        else:
            
            while True:
                print("Enter the game results \n:",end='')
                temp=input()
                if '\n' in temp:
                    tempList=temp.split('\n')
                    for i in tempList:
                        rankGames.inputData.append(i.replace('\n',''))
                else:
                    rankGames.inputData.append(temp)
                
                clearTerminal()
                print("Input captured,to add another press A or D if done\n:",end='')
                if input().upper()=='D':
                    break
                clearTerminal()
    
    @classmethod
    def _getNamesAndScores(self):
        '''
        This function uses takes the rankGames.inputData list, extracts the team 
        names and scores seperately, these are stored in index aligned
        lists viz. [rankGames.resultTeamNames] and [rankGames.resultTeamPoints]
        '''
        
        # Proccess the input data
        for game in rankGames.inputData:
            
            # Split the two teams
            teams=game.split(',')
            
            # Remove the whitespaces spaces in each teams's name and score
            teams[0]=teams[0].strip()
            teams[1]=teams[1].strip()
            
            # Split by ' ' character
            team1=teams[0].split(' ')
            team2=teams[1].split(' ')
            
            # Get the team scores
            score=[int(team1[len(team1)-1]),int(team2[len(team2)-1])]
            
            # Get the team names
            team1.pop()
            team2.pop()
            teamName=[' '.join(team1),' '.join(team2)]
            
            
            # If team name is not in result list,add it 
            if teamName[0] not in rankGames.resultTeamNames:
                rankGames.resultTeamNames.append(teamName[0])
                rankGames.resultTeamPoints.append(0)
                
            if teamName[1] not in rankGames.resultTeamNames:
                rankGames.resultTeamNames.append(teamName[1])
                rankGames.resultTeamPoints.append(0)
                
            # Evaluate points calculation
            if score[0]>score[1]:
                rankGames.resultTeamPoints[rankGames.resultTeamNames.index(teamName[0])]+=3
            
            elif score[1]>score[0]:
                rankGames.resultTeamPoints[rankGames.resultTeamNames.index(teamName[1])]+=3
                
            elif score[1]==score[0]:
                rankGames.resultTeamPoints[rankGames.resultTeamNames.index(teamName[0])]+=1
                rankGames.resultTeamPoints[rankGames.resultTeamNames.index(teamName[1])]+=1
            
    @classmethod
    def _sortListData(self):
        '''
        This function takes the names and score lists from 
        [rankGames.resultTeamNames] and [rankGames.resultTeamPoints]
        and then sorts the scores from highest to lowest.
        It also finds the sublists in then  [rankGames.resultTeamNames] with equal
        scores and then sort them in alphabetical order.
        '''
        
        # Sort from highest to lowest point
        while len(rankGames.resultTeamPoints) > 0:
            maxScoreIndex=rankGames.resultTeamPoints.index(max(rankGames.resultTeamPoints))# Find index of maximum 
            rankGames.sortedTeamNames.append(rankGames.resultTeamNames[maxScoreIndex]) # Add on sorted list
            rankGames.sortedTeamPoints.append(rankGames.resultTeamPoints[maxScoreIndex]) # Add on sorted list
            rankGames.resultTeamNames.pop(maxScoreIndex) # Remove on unsorted list
            rankGames.resultTeamPoints.pop(maxScoreIndex) # Remove on unsorted list
            
            
        # Sort the data in alphabetic if same score
        indexBuf=[]
        for i in range(1,len(rankGames.sortedTeamPoints)):
            
            # Detect a series of equal scores
            if rankGames.sortedTeamPoints[i]==rankGames.sortedTeamPoints[i-1]:
                if len(indexBuf)==0:
                    indexBuf.append(i-1)
                    indexBuf.append(i)
                else:
                    indexBuf.append(i)  
            
            # Make found sub lists with the same score sorted alphabetically
            if (rankGames.sortedTeamPoints[i]!=rankGames.sortedTeamPoints[i-1] or i==len(rankGames.sortedTeamPoints)-1) and len(indexBuf)>0:
                
                choppedNames=rankGames.sortedTeamNames[indexBuf[0]:indexBuf[len(indexBuf)-1]+1]
                rankGames.sortedTeamNames[indexBuf[0]:indexBuf[len(indexBuf)-1]+1]=sorted(choppedNames,reverse=False)
                indexBuf=[]
       
    @classmethod
    def _print(self):
        '''
        This function prints the output data as required.
        '''
       
        # Print the data
        for i in range(0,len(rankGames.sortedTeamNames)):
            print(str(i+1)+'. '+rankGames.sortedTeamNames[i]+', '+str(rankGames.sortedTeamPoints[i])+' pts')
       
    @classmethod
    def main(self):
        '''
        All the functions defined above should be implemented in a specific
        order. They are not accessible from outside the class. This function
        mainly implements the functions in the reqiored order and then produce the
        side effect. This is printing the output as required.
        '''
        
        rankGames._getInput()
        rankGames._getNamesAndScores()
        rankGames._sortListData()
        rankGames._print()
         
              
# App entry point
if __name__ == "__main__":   
    
    #Run the program
    rankGames.main()  


            

    

       