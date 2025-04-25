def grade(score):
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90:
        return 'B'
    elif 70 <= score < 80:
        return 'C'
    elif 60 <= score < 70:
        return 'D'
    else:
        return 'F'

print(grade(95))  
print(grade(85))  
print(grade(72))  
print(grade(65)) 
print(grade(50))  
