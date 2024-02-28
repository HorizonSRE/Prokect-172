class Doctor():
    def __init__(self):
        print("This is the Doctor class")
    def BMI(height, weight):
        bmi=weight/(height*height)
        print("Your BMI is "+str(bmi))
    def heart_rate(heart_rates):
        if(heart_rates>60 and heart_rates<100):
            print("Great! Your heart rate is normal.")
        else:
            print("Your heart rate is abnormal please visit a clinic.")
        
class Patient(Doctor):
    def __init__(self, name, weight, height, heart_rates):
        self.patient_name=name
        self.patient_height=height
        self.patient_weight=weight
        self.patient_heartrates=heart_rates
    def healthCheck(self):
        print("\n Patient Name: ", self.patient_name)
        Doctor.BMI(self.patient_height, self.patient_weight)
        Doctor.heart_rate(self.patient_heartrates)
    
patient1=Patient("Bartholomew", 50, 0.7, 80)
patient1.healthCheck()
patient2=Patient("Sleepy Joe", 30, 0.99, 50)
patient2.healthCheck()