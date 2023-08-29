import joblib
import pandas as pd
import numpy as np
model=joblib.load(r"C:\Users\MOHANKUMAR\Downloads\model1.joblib")
def eprediction(circuit_design,control_systems,power_electronics,analog_communication,r_f,cpp,electrical_system,cad,pcb,labview):
    
        epred = pd.DataFrame({
            'CIRCUIT DESIGN': [circuit_design],
            'CONTROL SYSTEMS': [control_systems],
            'POWER ELECTRONICS':[power_electronics],    
            'ANALOG COMMUNICATION':[analog_communication],
            'RF':[r_f],
            'C++':[cpp],
            'ELECTRICAL SYSTEM':[electrical_system],
            'CAD':[cad],
            'PCB':[pcb],
            'LABVIEW':[labview]},index=[0])
        predict1 = model.predict(epred)
        ans = np.array(predict1)
        print("".join(map(str, ans)))
        return ans
model1=joblib.load(r"C:\Users\MOHANKUMAR\Downloads\model2.joblib")
def cprediction(data_base,c_architecture,cyber_security,networking,software_development,ai_ml, graphics_designer,data_science):
        cpred = pd.DataFrame({
            'DATABASE': [data_base],
            'Computer Architecture': [c_architecture],
            'Cyber Security':[cyber_security],    
            'Networking':[networking],
            'Software Development':[software_development],
            'AI ML':[ai_ml],
            'Data Science':[graphics_designer],
            'Graphics Design':[data_science],},index=[0])
        predict1 = model1.predict(cpred)
        ans = np.array(predict1)
        print("".join(map(str, ans)))
        return ans
def send(lst):
        a = eprediction(lst[0],lst[1],lst[2],lst[3],lst[4],lst[5],lst[6],lst[7],lst[8],lst[9])
        return a
def sendcs(clst):
        a = cprediction(clst[0],clst[1],clst[2],clst[3],clst[4],clst[5],clst[6],clst[7])
        return a