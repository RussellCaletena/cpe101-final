nums = [[98, 90, 91], [46, 76, 62], [85, 90, 83], [77, 79, 81]]

#student1 = [98, 90, 91]
def student_pass(studentGradeList):
    total = 0
    for grade in studentGradeList:
        total += grade
    averageGrade = total / len(studentGradeList)
    return (int(averageGrade))

passingGrade = 70
def all_passing(nums, passingGrade):
    passList = []
    i = 0
    while i < len(nums):
        if student_pass(nums[i]) > passingGrade:
            passList.append('True')
        else:
            passList.append('False')
        i += 1
    print (passList)

all_passing(nums, passingGrade)
all_passing(nums, passingGrade = 80)
