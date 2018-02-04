# For the Graph
class Date:
    def __init__(self, month, day):
        self.__month = month
        self.__day = day
        self.__data = ''

    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = data

    def get_day(self):
        return self.__day
    def set_day(self, day):
        self.__day = day

    def get_month(self):
        return self.__month
    def set_month(self, month):
        self.__month = month


class BloodPressure(Date):
    def __init__(self, month, day, systolic, diastolic):
        super().__init__(month, day)
        self.__systolic = systolic
        self.__diastolic = diastolic

    def get_systolic(self):
            return self.__systolic
    def set_systolic(self, systolic):
            self.__systolic = systolic

    def get_diastolic(self):
            return self.__diastolic
    def set_diastolic(self, diastolic):
            self.__diastolic = diastolic


class BloodGlucose(Date):
    def __init__(self, month, day, blood_glucose):
        super().__init__(month, day)
        self.__blood_glucose = blood_glucose

    def get_blood_glucose(self):
        return self.__blood_glucose

    def set_blood_glucose(self, blood_glucose):
        self.__blood_glucose = blood_glucose


class Bmi(Date):
    def __init__(self,month , day, weight, height):
        super().__init__(month,day)
        self.__weight = weight
        self.__height = height

    def get_weight(self):
        return self.__weight
    def set_weight(self, weight):
        self.__weight = weight
    
    def get_height(self):
        return self.__height
    def set_height(self,height):
        self.__height = height
    
    def get_bmi(self):
        return self.__weight / (self.__height * self.__height)


class Information():
    def __init__(self, nric, status, 
                eye_bv, eye_sp, eye_we, eye_ed, eye_lo,
                kiney_sw, kiney_wg, kiney_id,
                heart_brain_so, heart_brain_ff, heart_brain_fd, heart_brain_sw, heart_brain_n, heart_brain_cp, heart_brain_sj,
                feet_,
                nerves_bp, nerves_n, nerves_to, nerves_cd, nerves_pw,
                neuropathy_pn, neuropathy_at, neuropathy_gm, neuropathy_ph, neuropathy_ud,
                medication, others):
        self.__nric = nric
        self.__status = status
        self.__eye_bv = eye_bv
        self.__eye_sp = eye_sp
        self.__eye_we = eye_we
        self.__eye_ed = eye_ed
        self.__eye_lo = eye_lo
        self.__kiney_sw = kiney_sw
        self.__kiney_wg = kiney_wg
        self.__kiney_id = kiney_id
        self.__heart_brain_so = heart_brain_so
        self.__heart_brain_ff = heart_brain_ff
        self.__heart_brain_fd = heart_brain_fd
        self.__heart_brain_sw = heart_brain_sw
        self.__heart_brain_n = heart_brain_n
        self.__heart_brain_cp = heart_brain_cp
        self.__heart_brain_sj = heart_brain_sj
        self.__feet_ = feet_
        self.__nerves_bp = nerves_bp
        self.__nerves_n = nerves_n
        self.__nerves_to = nerves_to
        self.__nerves_cd = nerves_cd
        self.__nerves_pw = nerves_pw
        self.__neuropathy_pn = neuropathy_pn
        self.__neuropathy_at = neuropathy_at
        self.__neuropathy_gm = neuropathy_gm
        self.__neuropathy_ph = neuropathy_ph
        self.__neuropathy_ud = neuropathy_ud
        self.__medication = medication
        self.__others = others
        self.__data = ''

    def get_data(self):
        return self.__data
    def set_data(self, data):
        self.__data = data

    def get_nric(self):
        return self.__nric
    def set_nric(self,nric):
        self.__nric = nric
        
    def get_status(self):
        return self.__status
    def set_status(self,status):
        self.__status = status
        
    def get_eye_bv(self):
        return self.__eye_bv
    def set_eye_bv(self,eye_bv):
        self.__eye_bv = eye_bv
        
    def get_eye_sp(self):
        return self.__eye_sp
    def set_eye_sp(self,eye_sp):
        self.__eye_sp = eye_sp
 
    def get_eye_we(self):
        return self.__eye_we
    def set_eye_we(self,eye_we):
        self.__eye_we = eye_we
         
    def get_eye_ed(self):
        return self.__eye_ed
    def set_eye_ed(self,eye_ed):
        self.__eye_ed = eye_ed
         
    def get_eye_lo(self):
        return self.__eye_lo
    def set_eye_lo(self,eye_lo):
        self.__eye_lo = eye_lo
        #########################################################################################################
        #########################################################################################################
        #########################################################################################################
    def get_kiney_sw(self):
        return self.__kiney_sw
    def set_kiney_sw(self,kiney_sw):
        self.__kiney_sw = kiney_sw
         
    def get_kiney_wg(self):
        return self.__kiney_wg
    def set_kiney_wg(self,kiney_wg):
        self.__kiney_wg = kiney_wg
         
    def get_kiney_id(self):
        return self.__kiney_id
    def set_kiney_id(self,kiney_id):
        self.__kiney_id = kiney_id
        #########################################################################################################
        #########################################################################################################
        #########################################################################################################    
    def get_heart_brain_so(self):
        return self.__heart_brain_so
    def set_heart_brain_so(self,heart_brain_so):
        self.__heart_brain_so = heart_brain_so
         
    def get_heart_brain_ff(self):
        return self.__heart_brain_ff
    def set_heart_brain_ff(self,heart_brain_ff):
        self.__heart_brain_ff = heart_brain_ff
         
    def get_heart_brain_fd(self):
        return self.__heart_brain_fd
    def set_heart_brain_fd(self,heart_brain_fd):
        self.__heart_brain_fd = heart_brain_fd
         
    def get_heart_brain_sw(self):
        return self.__heart_brain_sw
    def set_heart_brain_sw(self,heart_brain_sw):
        self.__heart_brain_sw = heart_brain_sw
         
    def get_heart_brain_n(self):
        return self.__heart_brain_n
    def set_heart_brain_n(self,heart_brain_n):
        self.__heart_brain_n = heart_brain_n
         
    def get_heart_brain_cp(self):
        return self.__heart_brain_cp
    def set_heart_brain_cp(self,heart_brain_cp):
        self.__heart_brain_cp = heart_brain_cp
         
    def get_heart_brain_sj(self):
        return self.__heart_brain_sj
    def set_heart_brain_sj(self,heart_brain_sj):
        self.__heart_brain_sj = heart_brain_sj
        #########################################################################################################
        #########################################################################################################
        #########################################################################################################         
    def get_feet_(self):
        return self.__feet_
    def set_feet_(self,feet_):
        self.__feet_ = feet_
        #########################################################################################################
        #########################################################################################################
        #########################################################################################################         
    def get_nerves_bp(self):
        return self.__nerves_bp
    def set_nerves_bp(self,nerves_bp):
        self.__nerves_bp = nerves_bp
         
    def get_nerves_n(self):
        return self.__nerves_n
    def set_nerves_n(self,nerves_n):
        self.__nerves_n = nerves_n
         
    def get_nerves_to(self):
        return self.__nerves_to
    def set_nerves_to(self,nerves_to):
        self.__nerves_to = nerves_to
         
    def get_nerves_cd(self):
        return self.__nerves_cd
    def set_nerves_cd(self,nerves_cd):
        self.__nerves_cd = nerves_cd
         
    def get_nerves_pw(self):
        return self.__nerves_pw
    def set_nerves_pw(self,nerves_pw):
        self.__nerves_pw = nerves_pw
        #########################################################################################################
        #########################################################################################################
        #########################################################################################################         
    def get_neuropathy_pn(self):
        return self.__neuropathy_pn
    def set_neuropathy_pn(self,neuropathy_pn):
        self.__neuropathy_pn = neuropathy_pn
         
    def get_neuropathy_at(self):
        return self.__neuropathy_at
    def set_neuropathy_at(self,neuropathy_at):
        self.__neuropathy_at = neuropathy_at
         
    def get_neuropathy_gm(self):
        return self.__neuropathy_gm
    def set_neuropathy_gm(self,neuropathy_gm):
        self.__neuropathy_gm = neuropathy_gm
         
    def get_neuropathy_ph(self):
        return self.__neuropathy_ph
    def set_neuropathy_ph(self,neuropathy_ph):
        self.__neuropathy_ph = neuropathy_ph
         
    def get_neuropathy_ud(self):
        return self.__neuropathy_ud
    def set_neuropathy_ud(self,neuropathy_ud):
        self.__neuropathy_ud = neuropathy_ud
        #########################################################################################################         
        #########################################################################################################         
        #########################################################################################################                  
    def get_medication(self):
        return self.__medication
    def set_medication(self,medication):
        self.__medication = medication
         
    def get_others(self):
        return self.__others
    def set_others(self,others):
        self.__others = others

    def get_all(self):
        return  self.__nric,self.__status,self.__eye_bv, self.__eye_sp, self.__eye_we, self.__eye_ed, self.__eye_lo, self.__kiney_sw, self.__kiney_wg, self.__kiney_id, self.__heart_brain_so, self.__heart_brain_ff,self.__heart_brain_fd, self.__heart_brain_sw, self.__heart_brain_n,self.__heart_brain_cp,self.__heart_brain_sj,self.__feet_,self.__nerves_bp, self.__nerves_n,self.__nerves_to,self.__nerves_cd,self.__nerves_pw,self.__neuropathy_pn,self.__neuropathy_at,self.__neuropathy_gm,self.__neuropathy_ph,self.__neuropathy_ud,self.__medication,self.__others