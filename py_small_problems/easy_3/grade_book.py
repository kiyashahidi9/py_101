def get_grade(gr1, gr2, gr3):
    average = (gr1 + gr2 + gr3) // 3

    if average in range(90, 101):
        return 'A'
    elif average in range(80, 90):
        return 'B'
    elif average in range(70, 80):
        return 'C'
    elif average in range(60, 70):
        return 'D'
    elif average in range(0, 60):
        return 'F'
    
print(get_grade(95, 90, 93) == 'A')      # True
print(get_grade(50, 50, 95) == "D")      # True