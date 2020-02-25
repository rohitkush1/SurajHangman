def calc_grade_points(grade, ap):
    if grade.upper() == 'A':
        if ap == True:
            return 'AP and A, 5'
        else:
            return 'No AP but A, 4'
    if grade.upper() == 'B':
        if ap == True:
            return 'AP and B, 4'
        else:
            return 'No AP but B, 3'

    if grade.upper() == 'C':
        if ap == True:
            return 'AP and C, 3'
        else:
            return 'No AP but C, 2'

    if grade.upper() == 'D':
        if ap == True:
            return 'No AP and D, 1'
        else:
            return 'No AP but D, 1' 

    if grade.upper() == 'F':
        if ap == True:
            return 'No AP and F, 0'
        else:
            return 'No AP but F, 0'                   
    
print(calc_grade_points('F', True))

def test():
    if (calc_grade_points("A", True) == "AP and A, 5"):
        print("Working for A, True")
    if(calc_grade_points("A", False) == "No AP but A, 4"):
        print("Working for A, False")
    if(calc_grade_points("B", True) == "AP and B, 4"):
        print("Working for B, True")
    if(calc_grade_points("B", False) == "No AP but B, 3"):
        print("Working for B, False")
    if(calc_grade_points("C", True) == "AP and C, 3"):
        print("Working for C, True")
    if(calc_grade_points("C", False) == "No AP but C, 2"):
        print("Working for C, False")
    if(calc_grade_points("D", True) == "No AP and D, 1"):
        print("Working for D, True")
    if(calc_grade_points("D", False) == "No AP but D, 1"):
        print("Working for D, False")
    if(calc_grade_points("F", True) != "No AP and F, 0"):
        print("Not Working for F, True")
    if(calc_grade_points("F", False) == "No AP but F, 0"):
        print("Working for F, False")
        
    


