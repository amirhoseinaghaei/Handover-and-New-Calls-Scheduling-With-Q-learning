Lambda_h = 1.5        
Lambda = 10
Mu_h = 1
Mu = 1

class State(object):
    def __init__(self, Name, New, Handover, C, P):
        self.State_list = { "Accept_New":[] , "Reject_New":[], "Drop":[]}
        self.Name = Name 
        self.New = New
        self.handover = Handover
        self.Create_State_Dict(New, Handover, C , P)
    def Create_State_Dict(self, New, Handover ,C ,P):
        R = 1
        R_Adding_handover = 1
        R_Adding_handover_in_high_occupaction = 0
        R_Permiting_new_call_in_low_occupation = 2
        Rt = 0
        R_Permiting_new_call_in_high_occupation = -1
        if New == 0 and 1<= Handover <= C-1 : 
            if Handover == 1:
                self.State_list["Accept_New"].append(((Handover+1 , New),  ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + Lambda + Lambda_h),R))
                self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/((C-Handover)*Mu_h + Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/((C-Handover)*Mu_h + Lambda + Lambda_h),R_Permiting_new_call_in_low_occupation))
                self.State_list["Reject_New"].append(((Handover+1 , New),  ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + Lambda_h),R))
                self.State_list["Reject_New"].append(((Handover-1 , New), (Lambda_h)/((C-Handover)*Mu_h + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))

            else:
                self.State_list["Accept_New"].append(((Handover+1 , New),  ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + Lambda + Lambda_h),R))
                self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/((C-Handover)*Mu_h + Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/((C-Handover)*Mu_h + Lambda + Lambda_h), R_Permiting_new_call_in_high_occupation if ((C-Handover+New)/C) > P else R_Permiting_new_call_in_low_occupation))
                self.State_list["Reject_New"].append(((Handover-1 , New),(Lambda_h)/((C-Handover)*Mu_h + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Reject_New"].append(((Handover+1 , New),  ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + Lambda_h),R))
       
        if New == Handover:
            if New == 0 and Handover == 0:
                self.State_list["Drop"].append(((Handover+1  , New), 1,Rt))
            if New == C and Handover == C:
                self.State_list["Drop"].append(((Handover  , New-1), 1,Rt))            
            self.State_list["Drop"].append(((Handover , New-1), (New*Mu)/((C-Handover)*Mu_h + New*Mu),Rt))
            self.State_list["Drop"].append(((Handover+1  , New), ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + New*Mu),Rt))

        if Handover == C and 1<= New <= C-1:
            if New == C-1: 
                self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/((New)*Mu + Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/((New)*Mu + Lambda + Lambda_h),R_Permiting_new_call_in_low_occupation))
                self.State_list["Accept_New"].append(((Handover , New-1), ((New)*Mu)/((New)*Mu + Lambda + Lambda_h),R))
                self.State_list["Reject_New"].append(((Handover-1 , New), (Lambda_h)/((New)*Mu + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Reject_New"].append(((Handover , New-1), ((New)*Mu)/((New)*Mu + Lambda_h),R))
            else:
                self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/((New)*Mu + Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/((New)*Mu + Lambda + Lambda_h),R_Permiting_new_call_in_high_occupation if ((C-Handover+New)/C) > P else R_Permiting_new_call_in_low_occupation))
                self.State_list["Accept_New"].append(((Handover , New-1), ((New)*Mu)/((New)*Mu + Lambda + Lambda_h),R))
                self.State_list["Reject_New"].append(((Handover-1 , New), (Lambda_h)/((New)*Mu + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Reject_New"].append(((Handover , New-1), ((New)*Mu)/((New)*Mu + Lambda_h),R))
        if 1 <= New <= C-2 and New+1 <= Handover <= C-1:
            
            if Handover == New + 1:
                self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Accept_New"].append(((Handover+1 , New), ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h),R))
                self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h), R_Permiting_new_call_in_low_occupation ))
                self.State_list["Accept_New"].append(((Handover , New-1), ((New)*Mu)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h),R))
            else:
                self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
                self.State_list["Accept_New"].append(((Handover+1 , New), ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h),R))
                self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h), R_Permiting_new_call_in_high_occupation if ((C-Handover+New)/C) > P else R_Permiting_new_call_in_low_occupation))
                self.State_list["Accept_New"].append(((Handover , New-1), ((New)*Mu)/((C-Handover)*Mu_h + (New)*Mu + Lambda + Lambda_h),R))
            self.State_list["Reject_New"].append(((Handover-1 , New), (Lambda_h)/((C-Handover)*Mu_h + (New)*Mu + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
            self.State_list["Reject_New"].append(((Handover+1 , New), ((C-Handover)*Mu_h)/((C-Handover)*Mu_h + (New)*Mu + Lambda_h),R))
            self.State_list["Reject_New"].append(((Handover , New-1), ((New)*Mu)/((C-Handover)*Mu_h + (New)*Mu + Lambda_h),R))

        if Handover == C and New == 0:
            self.State_list["Accept_New"].append(((Handover-1 , New), (Lambda_h)/(Lambda + Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))
            self.State_list["Accept_New"].append(((Handover , New+1), (Lambda)/(Lambda + Lambda_h), R_Permiting_new_call_in_high_occupation if ((C-Handover+New)/C) > P else R_Permiting_new_call_in_low_occupation))
            self.State_list["Reject_New"].append(((Handover-1 , New), (Lambda_h)/(Lambda_h),R_Adding_handover_in_high_occupaction if ((C-Handover+New)/C) > P else R_Adding_handover))

