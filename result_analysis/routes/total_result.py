# importing tabula python library for extracting data from PDF
import tabula 
# storing data to 'df' variable
df = tabula.read_pdf("/home/hishamalip/github/asdlab/result_analysis/views/s4.pdf", pages='all') 
# converting input pdf to csv format
# tabula.convert_into("/home/hishamalip/Desktop/result_analysis/views/s4.pdf", "s4.csv", output_format="csv", pages='all') 
# storing data to x in array format
x = df.to_numpy() 
# count_dept() : A function for returing the number of students appeared for exam
# start_index : Starting index of each department 
def count_dept(start_index):
    count = 0
    flag2= 0
    for i in range(start_index, len(x)):
        flag1 = 0
        for j in range(0,2):
            if type(x[i][j]) == float:
                flag2 = 1
                break
            else:
                flag1 = 1
        if flag2 == 1:
            break
        if flag1 == 1:
             count = count+1
    return count

# percentage() : A function for returning total number of students passed,failed and the pass percentage
# start_index : Starting index of each department 
# count : Total count of students appeared for exam in each deaprtment
def percentage(start_index,count):
    f=0
    p=0
    d=0
    total=0
    end_index= start_index + count
    for i in range(start_index, end_index):
        flag=0
        for j in range(1, 2):
            t = x[i][j] 
            #print(t)
            
            for k in range(0, len(t)):
                if t[k] == '(':
                    if t[k+1] == 'F' or (t[k+1] == 'A' and t[k+2] == 'b')  or (t[k+1] == 'D' and t[k+1] == 'e') or t[k+1] == 'T':
                        f=f+1
                        #print("fail")
                        flag=1
                        break
            if flag == 0:
                #print("pass")
                p=p+1
        d=(p*100)/count

    return d, f, p
# Variables 
percenatge_ce=0
percenatge_cs=0
percenatge_ec=0
percenatge_ee=0
percenatge_ae=0
percenatge_ie=0
percenatge_me=0

start_ce=0
start_ee=0
start_me=0
start_ie=0
start_ae=0
start_cs=0
start_ec=0

count_ce=0
count_ee=0
count_ec=0
count_ie=0
count_ae=0
count_cs=0
count_me=0

ce=0
ec=0
ee=0
me=0
ie=0
ec=0
cs=0
ae=0
# Loop which gives starting index of each department
for i in range(0,len(x)):
    q=x[i][0]
    if type(q) != float :
        for j in range(0,len(q)):
            if len(q) == 11 or len(q) ==10 :
                # Finding starting index of civil engineering
                if q[j] == 'C' and q[j+1 ] == 'E' and ce == 0:
                    #print("Civil Engineering")
                    dept='Civil Engineering'
                    ce=1
                    start_ce=i
                    break
                 # Finding starting index of electrical engineering    
                elif q[j] == 'E' and q[j+1] == 'E' and ee == 0:
                    #print("ELECTRICAL Engineering")
                    dept='Elctrical Engineering'
                    ee=1
                    start_ee=i
                    break
                 # Finding starting index of computer engineering    
                elif q[j] == 'C' and q[j+1] == 'S' and cs == 0:
                    #print("COMPUTER  Engineering")
                    dept='Computer Engineering'
                    cs=1
                    start_cs=i
                    break
                 # Finding starting index of mechanical engineering
                elif q[j] == 'M' and q[j+1] == 'E' and me == 0:
                    #print("MECHANICAL Engineering")
                    dept='mechanical Engineering'
                    me=1
                    start_me=i
                    break
                 # Finding starting index of industrial engineering
                elif q[j] == 'I' and q[j+1] == 'E' and ie == 0:
                    #print("INDUSTRAIL Engineering")
                    dept='industrial Engineering'
                    ie=1
                    start_ie=i
                    break
                 # Finding starting index of applied engineering
                elif q[j] == 'A' and q[j+1] == 'E' and ae==0:
                    #print("APPLIED Engineering")
                    dept='Applied Engineering'
                    ae=1
                    start_ae=i
                    break
                 # Finding starting index of electronics engineering
                elif q[j] == 'E' and q[j+1] == 'C'and ec == 0:
                    #print("ELECTRONICS Engineering")
                    start_ec=i
                    dept='Electronics Engineering'
                    ec=1
                    break          
        count_ce=count_dept(start_ce)
        count_me=count_dept(start_me)
        count_cs=count_dept(start_cs)
        count_ec=count_dept(start_ec)
        count_ie=count_dept(start_ie)
        count_ae=count_dept(start_ae)
        count_ee=count_dept(start_ee)
    percenatge_ce, fail_ce, pass_ce = percentage(start_ce,count_ce)
    percenatge_me, fail_me, pass_me = percentage(start_me,count_me)
    percenatge_ee, fail_ee, pass_ee = percentage(start_ee,count_ee)
    percenatge_ie,fail_ie, pass_ie = percentage(start_ie,count_ie)
    percenatge_ec, fail_ec, pass_ec = percentage(start_ec,count_ec)
    percenatge_cs, fail_cs, pass_cs = percentage(start_cs,count_cs)
    percenatge_ae,fail_ae, pass_ae = percentage(start_ae,count_ae)
#print(count_ce)
#print(count_ee)
#print(count_me)
#print(count_ie)
#print(count_ae)
#print(count_ec)
#print(count_cs)
#print(start_ce)
#print(start_ee)
#print(start_me)
#print(start_ie)
#print(start_ae)
#print(start_cs)
print("CIVIL ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_ce))
print("NUMBER OF STUDENTS PASSED =" + str(pass_ce))
print("NUMBER OF STUDENTS FAILED =" + str(fail_ce))
print("PASS PERCENTAGE =" + str(round(float(percenatge_ce),2)))
print("                      ")
print("ELECTRICAL ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_ee))
print("NUMBER OF STUDENTS PASSED =" + str(pass_ee))
print("NUMBER OF STUDENTS FAILED =" + str(fail_ee))
print("PASS PERCENTAGE =" + str(round(float(percenatge_ee),2)))
print("                      ")
print("MECHANICAL ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_me))
print("NUMBER OF STUDENTS PASSED =" + str(pass_me))
print("NUMBER OF STUDENTS FAILED =" + str(fail_me))
print("PASS PERCENTAGE =" + str(round(float(percenatge_me),2)))
print("                      ")
print("INDUSTRIAL ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_ie))
print("NUMBER OF STUDENTS PASSED =" + str(pass_ie))
print("NUMBER OF STUDENTS FAILED =" + str(fail_ie))
print("PASS PERCENTAGE =" + str(round(float(percenatge_ie),2)))
print("                      ")
print("APPLIED ELECTRONICS AND ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_ae))
print("NUMBER OF STUDENTS PASSED =" + str(pass_ae))
print("NUMBER OF STUDENTS FAILED =" + str(fail_ae))
print("PASS PERCENTAGE =" + str(round(float(percenatge_ae),2)))
print("                      ")
print("ELECTRONICS ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_ec))
print("NUMBER OF STUDENTS PASSED =" + str(pass_ec))
print("NUMBER OF STUDENTS FAILED =" + str(fail_ec))
print("PASS PERCENTAGE =" + str(round(float(percenatge_ec),2)))
print("                      ")
print("COMPUTER SCIENCE AND ENGINEERING ")
print("STUDENT APPEARED FOR EXAM =" + str(count_cs))
print("NUMBER OF STUDENTS PASSED =" + str(pass_cs))
print("NUMBER OF STUDENTS FAILED =" + str(fail_cs))
print("PASS PERCENTAGE =" + str(round(float(percenatge_cs),2)))

