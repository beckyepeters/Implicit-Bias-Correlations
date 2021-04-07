# Helper Functions for Implicit Bias Capstone 1

def clean(year): 
    



def age_group(age):
    bins = [10, 20, 30, 40, 50, 60, 70, 80]
    age = int(age)
    if age < 20:
        bucket = '<20'
    
    if age in range(20, 30):
        bucket = '20-30'
        
    if age in range(30, 40):
        bucket = '40-49'
        
    if age in range(40, 50):
        bucket = '50-59'
   
    if age in range(50, 60):
        bucket = '50-60'

    if age >= 60:
        bucket = '60+'

    return bucket 