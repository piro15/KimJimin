def Menu1(name,mid,final) :
    student_dic[str(name)]=[int(mid),int(final)]

def Menu2() :
    for key in student_dic:
        avg=(student_dic[key][0]+student_dic[key][1])/2
        if avg>=90:
            student_dic[key]=(student_dic[key][0],student_dic[key][1],'A')
            
        elif avg>=80:
            student_dic[key]=(student_dic[key][0],student_dic[key][1],'B')
            
        elif avg>=70:
            student_dic[key]=(student_dic[key][0],student_dic[key][1],'C')
            
        else:
            student_dic[key]=(student_dic[key][0],student_dic[key][1],'D')

def Menu3() :
    print('-----------------------')
    print('name  mid  final  grade')
    print('-----------------------')
    strFormat='%-6s%-5s%-7s%-6s'
    s= strFormat % ('sep1','sep2','sep3','sept4')
    
    for key in student_dic:
        s= strFormat %(key,student_dic[key][0],student_dic[key][1],student_dic[key][2])
        print(s)

def Menu4(delete):
    del student_dic[delete]

student_dic={}

print("*Menu*******************************")
print("1. Inserting students Info(name score1 score2)")
print("2. Grading")
print("3. Printing students Info")
print("4. Deleting students Info")
print("5. Exit program")
print("*************************************")
while True :
    choice = input("Choose menu 1, 2, 3, 4, 5 : ")
    if choice == "1":
        try:
            student=input("Enter name mid-score final-score : ").split()
            if len(student)!=3 :
                print('Num of data is not 3!')
            elif student[0] in student_dic :
                print('Already exist name!')
            elif int(student[1])<=0 or int(student[2])<=0 :
                raise ValueError
            elif not student[1].isdecimal or not student[2].isdecimal :
                raise ValueError
            else:
                Menu1(student[0],student[1],student[2])
        except ValueError:
            print('Score is not positive integer!')

    elif choice == "2" :
        if len(student_dic)==0:
            print('No student data!')
        else:
            Menu2()
            print('Grading to all students.')

    elif choice == "3" :
        try:
            if len(student_dic)==0:
                raise Exception
            for key in student_dic:
                if student_dic[key][2]== None:
                    raise IndexError
        except IndexError:
            print("There is a student who didn't get grade.")
        except Exception:
            print('No student data!')
        else:
            Menu3()
        

    elif choice == "4" :
        if len(student_dic)==0:
            print('No student data!')
        else:
            delete=input("Enter the name to delete : ")
            if delete in student_dic:
                Menu4(delete)
                print(delete,'student information is deleted.')
            else:
                print('Not exist name!')

    elif choice == "5" :
        print('Exit Program!')
        break

    else :
        print('Wrong number. Choose again.')
        
