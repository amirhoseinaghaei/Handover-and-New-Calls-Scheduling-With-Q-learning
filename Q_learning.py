import random
from tqdm import tqdm
import numpy as np 
import time 

def QLearning_Algorithm(State_list , C , P):
    
    def Discount():
        return 0.9  
    
    def choose_action_epsilon_greedy(state):
        
        if np.random.uniform(0, 1) < 0.01:
            action = random.choice(['Reject_New', 'Accept_New'])
                
        else:
            action = max((Quality[(state.Name, action)], action )for action in ['Reject_New', 'Accept_New',])[1]
        return action
    def Next_Reward_State(in_state, action):
        x= random.uniform(0,1)
        if len(in_state.State_list[action]) == 1:
                nextStateName  = '{}'.format(in_state.State_list[action][0][0])
                reward = in_state.State_list[action][0][2]

        if len(in_state.State_list[action]) == 2:
            if  0< x <= in_state.State_list[action][0][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][0][0])
                reward = in_state.State_list[action][0][2]
            else:
                nextStateName  = '{}'.format(in_state.State_list[action][1][0])
                reward = in_state.State_list[action][1][2]
        if len(in_state.State_list[action]) == 3:
            if  0< x <= in_state.State_list[action][0][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][0][0])
                reward = in_state.State_list[action][0][2]
            if  in_state.State_list[action][0][1] < x <= in_state.State_list[action][0][1] + in_state.State_list[action][1][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][1][0])
                reward = in_state.State_list[action][1][2]               
            else:    
                nextStateName  = '{}'.format(in_state.State_list[action][2][0])
                reward = in_state.State_list[action][2][2]  
        if len(in_state.State_list[action]) == 4:
            if 0< x <= in_state.State_list[action][0][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][0][0])
                reward = in_state.State_list[action][0][2]
            elif in_state.State_list[action][0][1] < x <=in_state.State_list[action][0][1] + in_state.State_list[action][1][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][1][0])
                reward = in_state.State_list[action][1][2]
            elif in_state.State_list[action][0][1] + in_state.State_list[action][1][1] < x <=in_state.State_list[action][0][1] + in_state.State_list[action][1][1] + in_state.State_list[action][2][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][2][0])
                reward = in_state.State_list[action][2][2]
            else:
                nextStateName  = '{}'.format(in_state.State_list[action][3][0])
                reward = in_state.State_list[action][3][2]
        return nextStateName , reward
    def Next_State_Terminal(in_state, action):
        x= random.uniform(0,1)
        if len(in_state.State_list[action]) == 2:
            if  0< x <= in_state.State_list[action][0][1]:
                nextStateName  = '{}'.format(in_state.State_list[action][0][0])
            else:
                nextStateName  = '{}'.format(in_state.State_list[action][1][0])
        else:
                nextStateName  = '{}'.format(in_state.State_list[action][0][0])
        return nextStateName
    def CalculateNewQuality(in_state , reward, action , MaxQ, discount_factor , learning_rate):
        return Quality[(in_state.Name , action)] + learning_rate * (reward + discount_factor *  MaxQ  - Quality[(in_state.Name , action)])
    Quality = {}
    for state in State_list:

            Quality[(state.Name , "Reject_New")] = 0  
            Quality[(state.Name , "Accept_New")] = 0
            Quality[(state.Name , "Drop")] = 0
    Reward_per_Episode = []
    Reject_per_Episode =[]
    Accept_per_Episode = []
    Visited_State_Count  = {}
    for i in State_list:
        Visited_State_Count[i.Name] = 0
    for i in tqdm(range(1000)): 
        Episode_Reward = 0
        Episode_Reject = 0
        Episode_Accept = 0
        while True:
            Var_State = random.choice(State_list)
            if int(((Var_State.Name).split(", ")[0]).split("(")[1]) != int(((Var_State.Name).split(", ")[1]).split(")")[0]):
                break
        for i in range(1000): 
            if int(((Var_State.Name).split(", ")[0]).split("(")[1]) != int(((Var_State.Name).split(", ")[1]).split(")")[0]):
                Occupied = (C - (int(((Var_State.Name).split(", ")[0]).split("(")[1])) + (int(((Var_State.Name).split(", ")[1]).split(")")[0])))/C

                Var_Action = choose_action_epsilon_greedy(Var_State)
                Visited_State_Count[Var_State.Name] += 1
                Next_State , Reward = Next_Reward_State(Var_State,Var_Action)
                if Var_Action == "Reject_New":
                    if (int(((Var_State.Name).split(", ")[0]).split("(")[1])) - (int(((Next_State).split(", ")[0]).split("(")[1])) == 1:
                        Episode_Reject += 1
                if Var_Action == "Accept_New":
                    if (int(((Var_State.Name).split(", ")[0]).split("(")[1])) - (int(((Next_State).split(", ")[0]).split("(")[1])) == 1:
                        Episode_Reject += 1
                    if (int(((Next_State).split(", ")[1]).split(")")[0]) - int(((Var_State.Name).split(", ")[1]).split(")")[0])) == 1:
                        Episode_Accept += 1          
                MaxQ = max((Quality[(Next_State, action)], action )for action in ['Reject_New', 'Accept_New'])[0]
                Quality[(Var_State.Name , Var_Action)]  = CalculateNewQuality(Var_State, Reward, Var_Action, MaxQ, Discount() , 0.6)
            else: 
                Var_Action = "Drop"
                Next_State = Next_State_Terminal(Var_State , Var_Action)
                Reward = 0
                Quality[(Var_State.Name , Var_Action)] = 0
                Episode_Reward += 1
                 
        
            for i in State_list:
                if i.Name == Next_State:
                    Var_State = i

        Reward_per_Episode.append(Episode_Reward)
        Reject_per_Episode.append(Episode_Reject)
        Accept_per_Episode.append(Episode_Accept)
    print("-------------------------------------------------------------------------")
    print('{:15} {:15} {:15}'.format('s' , '  pi(s)' , 'Q'))
    for keys, value in Quality.items():
         print('{:15} {:15} {:15}'.format( keys[0] ,  keys[1], value))
    
    print("-------------------------------------------------------------------------")
    print('{:15} {:15} {:15}'.format('s' , '  pi(s)' , 'Q'))
    Number_of_accept = 0
    Number_of_reject = 0
    for i in range(0,len(Quality.items()),3):
        if int(((list(Quality.items())[i][0][0]).split(", ")[1]).split(")")[0]) == int(((list(Quality.items())[i][0][0]).split(", ")[0]).split("(")[1]):
            print('{:15} {:15} {:15}'.format( list(Quality.items())[i+2][0][0] , list(Quality.items())[i+2][0][1], 0))

        else:
        
            compare_list = [list(Quality.items())[i][1] , list(Quality.items())[i+1][1] , list(Quality.items())[i+2][1]]
            index = compare_list.index(max(compare_list))
            if list(Quality.items())[i+index][0][1] == "Accept_New":
                Number_of_accept += 1
            if list(Quality.items())[i+index][0][1] == "Reject_New":
                Number_of_reject += 1
            print('{:15} {:15} {:15}'.format( list(Quality.items())[i+index][0][0] , list(Quality.items())[i+index][0][1], max(compare_list)))

    print("Number of rejects: {} , Number of accept: {}".format(Number_of_reject,Number_of_accept))
    print("Total visits of terminal state:{}".format(sum(Reward_per_Episode)))
    print("Total accepted hanover calls :{}".format(sum(Reject_per_Episode)))
    print("Total accepted new calls:{}".format(sum(Accept_per_Episode)))
    print("-------------------------------------------------------------------------")
    print('{:15} {:15}'.format('s' , 'number of times its visited'))
    for keys, value in Visited_State_Count.items():
        print('{:15}  {:15}'.format( keys, value))

