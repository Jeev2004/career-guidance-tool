import joblib
import pandas as pd
import numpy as np
model=joblib.load(r"C:\Users\MOHANKUMAR\Downloads\model1.joblib")
def prediction(circuit_design,control_systems,power_electronics,analog_communication,r_f,cpp,electrical_system,cad,pcb,labview):
    
        a = pd.DataFrame({
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
        predict1 = model.predict(a)
        b = np.array(predict1)
        print("".join(map(str, b)))
        return b
def printf(data):
        print(data)
a = "hi"
printf(a)