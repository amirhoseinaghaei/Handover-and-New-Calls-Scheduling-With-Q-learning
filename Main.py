from Defining_States import State
from Q_learning import QLearning_Algorithm
C = 10
P = 0.4

def Create_State(C,P):
    State_List = []
    for i in range(C+1):
        for j in range(C+1):
            if j + (C-i) <= C:
                State_List.append(State("({}, {})".format(i,j) , j ,i , C,P))
    print(len(State_List))
    return State_List
QLearning_Algorithm(Create_State(C,P) , C , P)

