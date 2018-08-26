height = input("請問您的身高是:")
weight = input("請問您的體重是:")
bmi = float(weight) / (float(height)/100)**2
print ('您的身高為:', height, '體重為:',weight,',謝謝,請隨時注意身體健康!')
print('您的BMI:', bmi)