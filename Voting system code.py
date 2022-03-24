#'Voting system code'
nominee_1=input('Enter your name: ')
nominee_2=input('Enter your name: ')

num_1_votes=0
num_2_votes=0
voter_ID=[1,2,3,4,5,6,7,8,9,10]
total_voters=len(voter_ID)
while True:
#for voter in voter_ID:
        
    if voter_ID==[]:
        print('voting session over')
        
        if num_1_votes>num_2_votes:
           percent=(num_1_votes/total_voters)*100
           print(percent)

        elif num_2_votes>num_1_votes:
           percent=(num_2_votes/total_voters)*100
           print(nominee_2," ",percent)
           break
    else:
         voter=int(input('Enter your voter_ID: '))
         if voter in  voter_ID:
            
            print('Eligible to vote')
            voter_ID.remove(voter)
            #print(voter)
            vote='1' or '2'
            vote= int(input("Enter your vote: " ))
            
            if vote == 1:
                num_1_votes=+1
                #print(num_1_votes)
                print('Thanks for voting')
                #break
            elif vote==2:
               num_2_votes=+1
               #print(num_2_votes)
               print('Thanks for voting')
               #break
            else:
                print('Invalid voter')
            
    #else: 
        #break
          #  print('You have votered or you are not registered go check your details')
           
