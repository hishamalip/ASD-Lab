# importing tabula python library for extracting data from PDF
import tabula 
# storing data to 'df' variable
df = tabula.read_pdf("s4.pdf", pages='all') 
# converting input pdf to csv format
#tabula.convert_into("s4.pdf", "subject.csv", output_format="csv", pages='all') 
# storing data to x in array format
x = df.to_numpy() 
# count_dept() : A function for returing the number of students appeared for exam
# start_index : Starting index of each department 
def display(pass_count,fail_count,percentage):
    total= pass_count + fail_count
    print("STUDENT APPEARED FOR EXAM =" + str(total))
    print("NUMBER OF STUDENTS PASSED =" + str(pass_count))
    print("NUMBER OF STUDENTS FAILED =" + str(fail_count))
    print("PASS PERCENTAGE =" + str(round(float(percentage),2)))



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
    # civil engineering
    
    global fhs210, phs210, dhs210, fma202, pma202, dma202, fce202, pce202, dce202, fce204, pce204, dce204, fce206, pce206, dce206
    global fce208, pce208, dce208, fce232, pce232, dce232, fce234, pce234, dce234
    fhs210= phs210= dhs210= fma202= pma202= dma202= fce202= pce202= dce202= fce204= pce204= dce204= fce206= pce206= dce206= 0
    fce208= pce208= dce208= fce232= pce232= dce232= fce234= pce234= dce234= 0
    
    # electrical and electronics
    global fhs200, phs200, dhs200,      fee202, pee202, dee202,     fee204, pee204, dee204,     fee206, pee206, dee206,     fee208, pee208, dee208,     fee232, pee232, dee232,     fee234, pee234, dee234
    fee202= pee202= dee202=      fee204= pee204= dee204=    fee206= pee206= dee206=     fee208= pee208= dee208=     fee232= pee232= dee232=     fee234= pee234= dee234=    fhs200= phs200= dhs2000     =   0

    # mechanical
    global fme202, pme202, dme202,      fme204, pme204, dme204,     fme206, pme206, dme206,     fme220, pme220, dme220,    fme232, pme232, dme232
    fhs210= phs210= dhs210=      fme202= pme202= dme202=      fme204= pme204= dme204=     fme206= pme206= dme206=     fme220= pme220= dme220=    fme232= pme232= dme232     =   0

    # computer science
    global fcs202, pcs202, dcs202,     fcs204, pcs204, dcs204,     fcs206, pcs206, dcs206,     fcs208, pcs208, dcs208,     fcs232, pcs232, dcs232,     fcs234, pcs234, dcs234
    fcs202= pcs202= dcs202=      fcs204= pcs204= dcs204=    fcs206= pcs206= dcs206=     fcs208= pcs208= dcs208=     fcs232= pcs232= dcs232=     fcs234= pcs234= dcs234= 0
    
    # industrial
    global fme218, pme218, dme218,      fie202, pie202, die202,     fme222, pme222, dme222,     fma208, pma208, dma208,     fie232, pie232, die232
    fme218= pme218= dme218=      fie202= pie202= die202=     fme222= pme222= dme222=     fma208= pma208= dma208=     fie232= pie232= die232 = 0
    
    # electronics and communication
    global fec202, pec202, dec202,      fec206, pec206, dec206,     fec208, pec208, dec208,     fec230, pec230, dec230 
    fec202= pec202= dec202=      fec206= pec206= dec206=     fec208= pec208= dec208=     fec230= pec230= dec230     =   0
    
    # applied electronics
    global fma204, pma204, dma204,      fae202, pae202, dae202,     fec204, pec204, dec204,     fae204, pae204, dae204,    fee216, pee216, dee216, fec232, pec232, dec232, fae232, pae232 ,dae232
    fma204= pma204= dma204=      fae202= pae202= dae202=     fec204= pec204= dec204=     fae204= pae204= dae204=    fee216= pee216= dee216= fec232= pec232= dec232= fae232= pae232= dae232 = 0
    
    
    end_index= start_index + count
    for i in range(start_index, end_index):
        flaghs210= flagma202= flagce202= flagce204= flagce206= flagce208= flagce232= flagce234 = 0 
        
         # electrical flags
        flaghs200 = flagee202 = flagee204 = flagee206 = flagee208 = flagee232 = flagee234 = 0

        # mechanical flags
        flagme202 = flagme204 = flagme206 = flagme232 = flagme220 = 0
        
        #computer flags
        flagcs202 = flagcs204 = flagcs206 = flagcs208 = flagcs232 = flagcs234 = 0
        
        # industrial flags
        flagme218 = flagie202 = flagme222 = flagma208 = flagie232 = 0
        
        # electronics and communication flags
        flagec202 = flagec206 = flagec208 = flagec230 = 0
        
        # applied electronics flags
        flagma204= flagae202= flagec204= flagae204= flagee216= flagec232= flagae232=  0 
        
        for j in range(1, 2):
            t = x[i][j] 
            ########################## CIVIL ENGINEERING ####################################
            if 'HS210' in t:
                hs210=t.index('HS210')
                hs210=hs210+5
                if t[hs210] == '(':
                    if t[hs210+1] == 'F' or (t[hs210+1] == 'A' and t[hs210+2] == 'b')  or (t[hs210+1] == 'D' and t[hs210+1] == 'e') or t[hs210+1] == 'T':
                        # print(x[i][0])
                        fhs210=fhs210+1
                        flaghs210=1
        
            if 'MA202' in t:
                ma202=t.index('MA202')
                ma202=ma202 + 5
                if t[ma202] == '(':
                    if t[ma202+1] == 'F' or (t[ma202+ 1] == 'A' and t[ma202+ 2] == 'b')  or (t[ma202+ 1] == 'D' and t[ma202+1] == 'e') or t[ma202+1] == 'T':
                        # print(x[i][0])
                        fma202=fma202+ 1
                        flagma202=1
                        
            if 'CE202' in t:
                ce202=t.index('CE202')
                ce202=ce202 + 5
                if t[ce202] == '(':
                    if t[ce202+1] == 'F' or (t[ce202+1] == 'A' and t[ce202+2] == 'b')  or (t[ce202+1] == 'D' and t[ce202+1] == 'e') or t[ce202+1] == 'T':
                        fce202=fce202+1
                        flagce202=1
                        
            if 'CE204' in t:
                ce204=t.index('CE204')
                ce204=ce204 + 5
                if t[ce204] == '(':
                    if t[ce204+1] == 'F' or (t[ce204+1] == 'A' and t[ce204+2] == 'b')  or (t[ce204+1] == 'D' and t[ce204+1] == 'e') or t[ce204+1] == 'T':
                        fce204=fce204+ 1
                        flagce204= 1
                        
            if 'CE206' in t:
                ce206=t.index('CE206')
                ce206=ce206 + 5
                if t[ce206] == '(':
                    if t[ce206+1] == 'F' or (t[ce206+1] == 'A' and t[ce206+2] == 'b')  or (t[ce206+1] == 'D' and t[ce206+1] == 'e') or t[ce206+1] == 'T':
                        fce206=fce206+ 1
                        flagce206= 1
                        
            if 'CE208' in t:
                ce208=t.index('CE208')
                ce208=ce208 + 5
                if t[ce208] == '(':
                    if t[ce208+1] == 'F' or (t[ce208+1] == 'A' and t[ce208+2] == 'b')  or (t[ce208+1] == 'D' and t[ce208+1] == 'e') or t[ce208+1] == 'T':
                        fce208=fce208+ 1
                        flagce208= 1
                        
            if 'CE232' in t:
                ce232=t.index('CE232')
                ce232=ce232 + 5
                if t[ce232] == '(':
                    if t[ce232+1] == 'F' or (t[ce232+1] == 'A' and t[ce232+2] == 'b')  or (t[ce232+1] == 'D' and t[ce232+1] == 'e') or t[ce232+1] == 'T':
                        fce232=fce232+ 1
                        flagce232= 1
                        
            if 'CE234' in t:
                ce234=t.index('CE234')
                ce234=ce234 + 5
                if t[ce234] == '(':
                    if t[ce234+1] == 'F' or (t[ce234+1] == 'A' and t[ce234+2] == 'b')  or (t[ce234+1] == 'D' and t[ce234+1] == 'e') or t[ce234+1] == 'T':
                        fce234=fce234+ 1
                        flagce234 = 1 
                        
            ############################## ELECTRICAL AND ELECTRONICS ENGINEERING[Full Time] #######################################

            if 'HS200' in t:
                hs200=t.index('HS200')
                hs200=hs200 + 5
                if t[hs200] == '(':
                    if t[hs200+1] == 'F' or (t[hs200+1] == 'A' and t[hs200+2] == 'b')  or (t[hs200+1] == 'D' and t[hs200+1] == 'e') or t[hs200+1] == 'T':
                        fhs200=fhs200+1
                        flaghs200=1
                       

            if 'EE202' in t:
                ee202=t.index('EE202')
                ee202=ee202 + 5
                if t[ee202] == '(':
                    if t[ee202+1] == 'F' or (t[ee202+1] == 'A' and t[ee202+2] == 'b')  or (t[ee202+1] == 'D' and t[ee202+1] == 'e') or t[ee202+1] == 'T':
                        fee202=fee202+1
                        flagee202=1
                  

            if 'EE204' in t:
                ee204=t.index('EE204')
                ee204=ee204 + 5
                if t[ee204] == '(':
                    if t[ee204+1] == 'F' or (t[ee204+1] == 'A' and t[ee204+2] == 'b')  or (t[ee204+1] == 'D' and t[ee204+1] == 'e') or t[ee204+1] == 'T':
                        fee204=fee204+1
                        flagee204=1
                      

            if 'EE206' in t:
                ee206=t.index('EE206')
                ee206=ee206 + 5
                if t[ee206] == '(':
                    if t[ee206+1] == 'F' or (t[ee206+1] == 'A' and t[ee206+2] == 'b')  or (t[ee206+1] == 'D' and t[ee206+1] == 'e') or t[ee206+1] == 'T':
                        fee206=fee206+1
                        flagee206=1
                      

            if 'EE208' in t:
                ee208=t.index('EE208')
                ee208=ee208 + 5
                if t[ee208] == '(':
                    if t[ee208+1] == 'F' or (t[ee208+1] == 'A' and t[ee208+2] == 'b')  or (t[ee208+1] == 'D' and t[ee208+1] == 'e') or t[ee208+1] == 'T':
                        fee208=fee208+1
                        flagee208=1
                       

            if 'EE232' in t:
                ee232=t.index('EE232')
                ee232=ee232 + 5
                if t[ee232] == '(':
                    if t[ee232+1] == 'F' or (t[ee232+1] == 'A' and t[ee232+2] == 'b')  or (t[ee232+1] == 'D' and t[ee232+1] == 'e') or t[ee232+1] == 'T':
                        fee232=fee232+1
                        flagee232=1
                 

            if 'EE234' in t:
                ee234=t.index('EE234')
                ee234=ee234 + 5
                if t[ee234] == '(':
                    if t[ee234+1] == 'F' or (t[ee234+1] == 'A' and t[ee234+2] == 'b')  or (t[ee234+1] == 'D' and t[ee234+1] == 'e') or t[ee234+1] == 'T':
                        fee234=fee234+1
                        flagee234=1
                      

                        
            ############################## MECHANICAL ENGINEERING[Full Time]  #######################################

            if 'ME202' in t:
                me202=t.index('ME202')
                me202=me202 + 5
                if t[me202] == '(':
                    if t[me202+1] == 'F' or (t[me202+1] == 'A' and t[me202+2] == 'b')  or (t[me202+1] == 'D' and t[me202+1] == 'e') or t[me202+1] == 'T':
                        fme202=fme202+1
                        flagme202=1
                    

            if 'ME204' in t:
                me204=t.index('ME204')
                me204=me204 + 5
                if t[me204] == '(':
                    if t[me204+1] == 'F' or (t[me204+1] == 'A' and t[me204+2] == 'b')  or (t[me204+1] == 'D' and t[me204+1] == 'e') or t[me204+1] == 'T':
                        fme204=fme204+1
                        flagme204=1
                   

            if 'ME206' in t:
                me206=t.index('ME206')
                me206=me206 + 5
                if t[me206] == '(':
                    if t[me206+1] == 'F' or (t[me206+1] == 'A' and t[me206+2] == 'b')  or (t[me206+1] == 'D' and t[me206+1] == 'e') or t[me206+1] == 'T':
                        fme206=fme206+1
                        flagme206=1
                    

            if 'ME220' in t:
                me220=t.index('ME220')
                me220=me220 + 5
                if t[me220] == '(':
                    if t[me220+1] == 'F' or (t[me220+1] == 'A' and t[me220+2] == 'b')  or (t[me220+1] == 'D' and t[me220+1] == 'e') or t[me220+1] == 'T':
                        fme220=fme220+1
                        flagme220=1
                        
    
            if 'ME232' in t:
                me232=t.index('ME232')
                me232=me232 + 5
                if t[me232] == '(':
                    if t[me232+1] == 'F' or (t[me232+1] == 'A' and t[me232+2] == 'b')  or (t[me232+1] == 'D' and t[me232+1] == 'e') or t[me232+1] == 'T':
                        fme232=fme232+1
                        flagme232=1
                        
            ################### COMPUTER SCIENCE & ENGINEERING ####################################
                       

            if 'CS202' in t:
                cs202=t.index('CS202')
                cs202=cs202 + 5
                if t[cs202] == '(':
                    if t[cs202+1] == 'F' or (t[cs202+1] == 'A' and t[cs202+2] == 'b')  or (t[cs202+1] == 'D' and t[cs202+1] == 'e') or t[cs202+1] == 'T':
                        fcs202=fcs202+ 1
                        flagcs202= 1
                  

            if 'CS204' in t:
                cs204=t.index('CS204')
                cs204=cs204 + 5
                if t[cs204] == '(':
                    if t[cs204+1] == 'F' or (t[cs204+1] == 'A' and t[cs204+2] == 'b')  or (t[cs204+1] == 'D' and t[cs204+1] == 'e') or t[cs204+1] == 'T':
                        fcs204=fcs204+1
                        flagcs204=1
                      

            if 'CS206' in t:
                cs206=t.index('CS206')
                cs206=cs206 + 5
                if t[cs206] == '(':
                    if t[cs206+1] == 'F' or (t[cs206+1] == 'A' and t[cs206+2] == 'b')  or (t[cs206+1] == 'D' and t[cs206+1] == 'e') or t[cs206+1] == 'T':
                        fcs206=fcs206+1
                        flagcs206=1
                      

            if 'CS208' in t:
                cs208=t.index('CS208')
                cs208=cs208 + 5
                if t[cs208] == '(':
                    if t[cs208+1] == 'F' or (t[cs208+1] == 'A' and t[cs208+2] == 'b')  or (t[cs208+1] == 'D' and t[cs208+1] == 'e') or t[cs208+1] == 'T':
                        fcs208=fcs208+1
                        flagcs208=1
                       

            if 'CS232' in t:
                cs232=t.index('CS232')
                cs232=cs232 + 5
                if t[cs232] == '(':
                    if t[cs232+1] == 'F' or (t[cs232+1] == 'A' and t[cs232+2] == 'b')  or (t[cs232+1] == 'D' and t[cs232+1] == 'e') or t[cs232+1] == 'T':
                        fcs232=fcs232+1
                        flagcs232=1
                 

            if 'CS234' in t:
                cs234=t.index('CS234')
                cs234=cs234 + 5
                if t[cs234] == '(':
                    if t[cs234+1] == 'F' or (t[cs234+1] == 'A' and t[cs234+2] == 'b')  or (t[cs234+1] == 'D' and t[cs234+1] == 'e') or t[cs234+1] == 'T':
                        fcs234=fcs234+1
                        flagcs234=1
                        
             ############################## INDUSTRIAL ENGINEERING[Full Time] #######################################
            if 'ME218' in t:
                me218=t.index('ME218')
                me218=me218 + 5
                if t[me218] == '(':
                    if t[me218+1] == 'F' or (t[me218+1] == 'A' and t[me218+2] == 'b')  or (t[me218+1] == 'D' and t[me218+1] == 'e') or t[me218+1] == 'T':
                        fme218=fme218+1
                        flagme218=1

            if 'IE202' in t:
                ie202=t.index('IE202')
                ie202=ie202 + 5
                if t[ie202] == '(':
                    if t[ie202+1] == 'F' or (t[ie202+1] == 'A' and t[ie202+2] == 'b')  or (t[ie202+1] == 'D' and t[ie202+1] == 'e') or t[ie202+1] == 'T':
                        fie202=fie202+1
                        flagie202=1
            
            if 'ME222' in t:
                me222=t.index('ME222')
                me222=me222 + 5
                if t[me222] == '(':
                    if t[me222+1] == 'F' or (t[me222+1] == 'A' and t[me222+2] == 'b')  or (t[me222+1] == 'D' and t[me222+1] == 'e') or t[me222+1] == 'T':
                        fme222=fme222+1
                        flagme222=1

            if 'MA208' in t:
                ma208=t.index('MA208')
                ma208=ma208 + 5
                if t[ma208] == '(':
                    if t[ma208+1] == 'F' or (t[ma208+1] == 'A' and t[ma208+2] == 'b')  or (t[ma208+1] == 'D' and t[ma208+1] == 'e') or t[ma208+1] == 'T':
                        fma208=fma208+1
                        flagma208=1

            if 'IE232' in t:
                ie232=t.index('IE232')
                ie232=ie232 + 5
                if t[ie232] == '(':
                    if t[ie232+1] == 'F' or (t[ie232+1] == 'A' and t[ie232+2] == 'b')  or (t[ie232+1] == 'D' and t[ie232+1] == 'e') or t[ie232+1] == 'T':
                        fie232=fie232+1
                        flagie232=1
                        
            ############################## ELECTRONICS & COMMUNICATION ENGG[Full Time] #######################################
           
            if 'EC202' in t:
                ec202=t.index('EC202')
                ec202=ec202 + 5
                if t[ec202] == '(':
                    if t[ec202+1] == 'F' or (t[ec202+1] == 'A' and t[ec202+2] == 'b')  or (t[ec202+1] == 'D' and t[ec202+1] == 'e') or t[ec202+1] == 'T':
                        fec202=fec202+1
                        flagec202=1

            if 'EC206' in t:
                ec206=t.index('EC206')
                ec206=ec206 + 5
                if t[ec206] == '(':
                    if t[ec206+1] == 'F' or (t[ec206+1] == 'A' and t[ec206+2] == 'b')  or (t[ec206+1] == 'D' and t[ec206+1] == 'e') or t[ec206+1] == 'T':
                        fec206=fec206+1
                        flagec206=1

            if 'EC208' in t:
                ec208=t.index('EC208')
                ec208=ec208 + 5
                if t[ec208] == '(':
                    if t[ec208+1] == 'F' or (t[ec208+1] == 'A' and t[ec208+2] == 'b')  or (t[ec208+1] == 'D' and t[ec208+1] == 'e') or t[ec208+1] == 'T':
                        fec208=fec208+1
                        flagec208=1
            
            if 'EC230' in t:
                ec230=t.index('EC230')
                ec230=ec230 + 5
                if t[ec230] == '(':
                    if t[ec230+1] == 'F' or (t[ec230+1] == 'A' and t[ec230+2] == 'b')  or (t[ec230+1] == 'D' and t[ec230+1] == 'e') or t[ec230+1] == 'T':
                        fec230=fec230+1
                        flagec230=1
                        
            ######################### APPLIED ELECTRONICS & INSTRUMENTATION ENGINEERING[Full Time] #########################################
           
           
            if 'MA204' in t:
                ma204=t.index('MA204')
                ma204=ma204 + 5
                if t[ma204] == '(':
                    if t[ma204+1] == 'F' or (t[ma204+1] == 'A' and t[ma204+2] == 'b')  or (t[ma204+1] == 'D' and t[ma204+1] == 'e') or t[ma204+1] == 'T' or t[ma204+1] == 'i':
                        fma204=fma204+1
                        flagma204=1
                   
                       

            if 'AE202' in t:
                ae202=t.index('AE202')
                ae202=ae202 + 5
                if t[ae202] == '(':
                    if t[ae202+1] == 'F' or (t[ae202+1] == 'A' and t[ae202+2] == 'b')  or (t[ae202+1] == 'D' and t[ae202+1] == 'e') or t[ae202+1] == 'T':
                        fae202=fae202+1
                        flagae202=1

            if 'EC204' in t:
                ec204=t.index('EC204')
                ec204=ec204 + 5
                if t[ec204] == '(':
                    if t[ec204+1] == 'F' or (t[ec204+1] == 'A' and t[ec204+2] == 'b')  or (t[ec204+1] == 'D' and t[ec204+1] == 'e') or t[ec204+1] == 'T':
                        fec204=fec204+1
                        flagec204=1
                       
            if 'AE204' in t:
                ae204=t.index('AE204')
                ae204=ae204 + 5
                if t[ae204] == '(':
                    if t[ae204+1] == 'F' or (t[ae204+1] == 'A' and t[ae204+2] == 'b')  or (t[ae204+1] == 'D' and t[ae204+1] == 'e') or t[ae204+1] == 'T':
                        fae204=fae204+1
                        flagae204=1


            if 'EE216' in t:
                ee216=t.index('EE216')
                ee216=ee216 + 5
                if t[ee216] == '(':
                    if t[ee216+1] == 'F' or (t[ee216+1] == 'A' and t[ee216+2] == 'b')  or (t[ee216+1] == 'D' and t[ee216+1] == 'e') or t[ee216+1] == 'T':
                        fee216=fee216+1
                        flagee216=1
                       
            if 'EC232' in t:
                ec232=t.index('EC232')
                ec232=ec232 + 5
                if t[ec232] == '(':
                    if t[ec232+1] == 'F' or (t[ec232+1] == 'A' and t[ec232+2] == 'b')  or (t[ec232+1] == 'D' and t[ec232+1] == 'e') or t[ec232+1] == 'T':
                        fec232=fec232+1
                        flagec232=1
                 

            if 'AE232' in t:
                ae232=t.index('AE232')
                ae232=ae232 + 5
                if t[ae232] == '(':
                    if t[ae232+1] == 'F' or (t[ae232+1] == 'A' and t[ae232+2] == 'b')  or (t[ae232+1] == 'D' and t[ae232+1] == 'e') or t[ae232+1] == 'T':
                        fae232=fae232+1
                        flagae232=1
                     


        # Civil engineering    
        if flaghs210 == 0:
            phs210=phs210+1
            
        if flagma202 == 0:
            pma202=pma202+1
            
        if flagce202 == 0:
            pce202=pce202+1
            
        if flagce204 == 0:
            pce204=pce204+1   
            
        if flagce206 == 0:
            pce206= pce206+1 
            
        if flagce208 == 0:
            pce208= pce208+1 
        
        if flagce232 == 0:
            pce232= pce232+1 
        
        if flagce234 == 0:
            pce234= pce234+1 
        
        
        # electrical
        if flaghs200 == 0:
            phs200=phs200+1
        if flagee202 == 0:
            pee202=pee202+1
        if flagee204 == 0:
            pee204=pee204+1
        if flagee206 == 0:
            pee206=pee206+1
        if flagee208 == 0:
            pee208=pee208+1
        if flagee232 == 0:
            pee232=pee232+1
        if flagee234 == 0:
            pee234=pee234+1

        # Mechanical
        if flagme202 == 0:
            pme202=pme202+1
        if flagme204 == 0:
            pme204=pme204+1
        if flagme206 == 0:
            pme206=pme206+1 
        if flagme220 == 0:
            pme220=pme220+1
        if flagme232 == 0:
            pme232=pme232+1
            
        #computer science
        if flagcs202 == 0:
            pcs202=pcs202+1
        if flagcs204 == 0:
            pcs204=pcs204+1
        if flagcs206 == 0:
            pcs206=pcs206+1
        if flagcs208 == 0:
            pcs208=pcs208+1
        if flagcs232 == 0:
            pcs232=pcs232+1
        if flagcs234 == 0:
            pcs234=pcs234+1
            
        # industrial
        if flagme218 == 0:
            pme218 = pme218 + 1
        if flagie202 == 0:
            pie202 = pie202 + 1
        if flagme222 == 0:
            pme222 = pme222 + 1
        if flagma208 == 0:
            pma208 = pma208 + 1
        if flagie232 == 0:
            pie232 = pie232 + 1
            
        # electronics and communication
        if flagec202 == 0:
            pec202 = pec202 + 1
        if flagec206 == 0:
            pec206 = pec206 + 1
        if flagec208 == 0:
            pec208 = pec208 + 1
        if flagec230 == 0:
            pec230 = pec230 + 1
        
        #Applied Electronics
       
        if flagma204 == 0:
            pma204=pma204+1
        if flagae202 == 0:
            pae202=pae202+1
        if flagec204 == 0:
            pec204=pec204+1
        if flagae204 == 0:
            pae204=pae204+1
        if flagee216 == 0:
            pee216=pee216+1
        if flagec232 == 0:
            pec232=pec232+1
        if flagae232 == 0:
            pae232=pae232+1
        
        #civil engineering
        dhs210= (phs210*100)/count
        dma202= (pma202*100)/count
        dce202= (pce202*100)/count
        dce204= (pce204*100)/count
        dce206= (pce206*100)/count
        dce208= (pce208*100)/count
        dce232= (pce232*100)/count
        dce234= (pce234*100)/count
        
        # electrical and elctronics pass percentage
        dhs200= (phs200*100)/count        
        dee202= (pee202*100)/count
        dee204= (pee204*100)/count
        dee206= (pee206*100)/count
        dee208= (pee208*100)/count
        dee232= (pee232*100)/count
        dee234= (pee234*100)/count
        
        # mechanical pass percentage
        dme202= (pme202*100)/count        
        dme204= (pme204*100)/count
        dme206= (pme206*100)/count 
        dme220= (pme220*100)/count 
        dme232= (pme232*100)/count 
        
        #computer science
        dcs202= (pcs202*100)/count
        dcs204= (pcs204*100)/count
        dcs206= (pcs206*100)/count
        dcs208= (pcs208*100)/count
        dcs232= (pcs232*100)/count
        dcs234= (pcs234*100)/count
        
        # industrial pass percentage
        dme218= (pme218*100)/count
        die202= (pie202*100)/count
        dme222= (pme222*100)/count
        dma208= (pma208*100)/count
        die232= (pie232*100)/count
        
        # electronics and communication pass percentage
        dec202 = (pec202*100)/count
        dec206 = (pec206*100)/count
        dec208 = (pec208*100)/count
        dec230 = (pec230*100)/count
        
        # applied electronics pass percentage
        dma204= (pma204*100)/count
        dae202= (pae202*100)/count
        dec204= (pec204*100)/count
        dae204= (pae204*100)/count
        dee216= (pee216*100)/count
        dec232= (pec232*100)/count
        dae232= (pae232*100)/count

        
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
        
print("CIVIL ENGINEERING ")
print("                       ")
percentage(start_ce,count_ce)
print("PROBABILITY DISTRIBUTIONS, TRANSFORMS AND NUMERICAL METHODS ")
display(pma202,fma202,dma202)
print("                       ")
print("STRUCTURAL ANALYSIS I")
display(pce202,fce202,dce202)
print("                       ")
print("CONSTRUCTION TECHNOLOGY")
display(pce204,fce204,dce204)
print("                       ")
print("FLUID MECHANICS II")
display(pce206,fce206,dce206)
print("                       ")
print("GEOTECHNICAL ENGINEERING I")
display(pce208,fce208,dce208)
print("                       ")
print("MATERIALS TESTING LAB I")
display(pce232,fce232,dce232)
print("                       ")
print("FLUID MECHANICS LAB")
display(pce234,fce234,dce234)
print("                       ")
print("LIFE SKILLS")
display(phs210,fhs210,dhs210)

print("-----------------------")
print("                       ")

print("MECHANICAL ENGINEERING ")
print("                       ")
percentage(start_me,count_me)
print("PROBABILITY DISTRIBUTIONS, TRANSFORMS AND NUMERICAL METHODS ")
display(pma202,fma202,dma202)
print("                       ")
print("ADVANCED MECHANICS OF SOLIDS")
display(pme202,fme202,dme202)
print("                       ")
print("THERMAL ENGINEERING")
display(pme204,fme204,dme204)
print("                       ")
print("FLUID MACHINERY")
display(pme206,fme206,dme206)
print("                       ")
print("MANUFACTURING TECHNOLOGY")
display(pme220,fme220,dme220)
print("                       ")
print("THERMAL ENGINEERING LAB")
display(pme232,fme232,dme232)
print("                       ")
print("LIFE SKILLS")
display(phs210,fhs210,dhs210)

print("-----------------------")
print("                       ")

print("ELECTRICAL ENGINEERING ")
print("                       ")
percentage(start_ee,count_ee)
print("PROBABILITY DISTRIBUTIONS, TRANSFORMS AND NUMERICAL METHODS ")
display(pma202,fma202,dma202)
print("                       ")
print("SYNCHRONOUS AND INDUCTION MACHINES")
display(pee202,fee202,dee202)
print("                       ")
print("DIGITAL ELECTRONICS AND LOGIC DESIGN")
display(pee204,fee204,dee204)
print("                       ")
print("MATERIAL SCIENCE")
display(pee206,fee206,dee206)
print("                       ")
print("MEASUREMENTS AND INSTRUMENTATION")
display(pee208,fee208,dee208)
print("                       ")
print("ELECTRICAL MACHINES LAB I")
display(pee232,fee232,dee232)
print("                       ")
print("CIRCUITS AND MEASUREMENTS LAB")
display(pee234,fee234,dee234)
print("                       ")
print("BUSINESS ECONOMICS")
display(phs200,fhs200,dhs200)
print("                       ")


print("INDUSTRIAL ENGINEERING ")
print("                       ")
percentage(start_ie,count_ie)
print("INTRODUCTION TO STOCHASTIC MODELS")
display(pma208,fma208,dma208)
print("                       ")
print("ELEMENTS OF MACHINE DESIGN")
display(pme218,fme218,dme218)
print("                       ")
print("OBJECT ORIENTED PROGRAMMING & NUMERICAL METHODS THERMAL ENGINEERING II")
display(pie202,fie202,die202)
print("                       ")
print("THERMAL ENGINEERING II")
display(pme222,fme222,dme222)
print("                       ")
print("MANUFACTURING TECHNOLOGY")
display(pme220,fme220,dme220)
print("                       ")
print("THERMAL ENGINEERING LAB")
display(pme232,fme232,dme232)
print("                       ")
print("OBJECT ORIENTED PROGRAMMING LAB")
display(pie232,fie232,die232)
print("                       ")
print("LIFE SKILLS")
display(phs210,fhs210,dhs210)
print("                       ")
 
print("ELECTRONICS ENGINEERING ")
print("                       ")
percentage(start_ec,count_ec)
print("PROBABILITY, RANDOM PROCESSES AND NUMERICAL METHODS")
display(pma204,fma204,dma204)
print("                       ")
print("SIGNALS & SYSTEMS")
display(pec202,fec202,dec202)
print("                       ")
print("ANALOG INTEGRATED CIRCUITS")
display(pee204,fee204,dee204)
print("                       ")
print("COMPUTER ORGANIZATION")
display(pec206,fec206,dec206)
print("                       ")
print("ANALOG COMMUNICATION ENGINEERING")
display(pee208,fee208,dee208)
print("                       ")
print("ANALOG INTEGRATED CIRCUITS LAB")
display(pec232,fec232,dec232)
print("                       ")
print("LOGIC CIRCUIT DESIGN LAB")
display(pec230,fec230,dec230)
print("                       ")
print("BUSINESS ECONOMICS")
display(phs200,fhs200,dhs200)
print("                       ")



print("COMPUTER SCIENCE AND ENGINEERING ")
print("                                ")
percentage(start_cs,count_cs)
print("PROBABILITY DISTRIBUTIONS, TRANSFORMS AND NUMERICAL METHODS ")
display(pma202,fma202,dma202)
print("                       ")
print("COMPUTER ORGANIZATION AND ARCHITECTURE")
display(pcs202,fcs202,dcs202)
print("                       ")
print("OPERATING SYSTEMS")
display(pcs204,fcs204,dcs204)
print("                       ")
print("OBJECT ORIENTED DESIGN AND PROGRAMMING")
display(pcs206,fcs206,dcs206)
print("                       ")
print("PRINCIPLES OF DATABASE DESIGN")
display(pcs208,fcs208,dcs208)
print("                       ")
print("FREE AND OPEN SOURCE SOFTWARE LAB")
display(pcs232,fcs232,dcs232)
print("                       ")
print("DIGITAL SYSTEMS LAB")
display(pcs234,fcs234,dcs234)
print("                       ")
print("BUSINESS ECONOMICS")
display(phs200,fhs200,dhs200)
print("                       ")


print("APPLIED ELECTRONICS AND ENGINEERING ")
print("                                ")
percentage(start_ae,count_ae)
print("PROBABILITY, RANDOM PROCESSES AND NUMERICAL METHODS ")
display(pma204,fma204,dma204)
print("                                ")
print("COMPUTER PROGRAMMING")
display(pae202,fae202,dae202)
print("                                ")
print("ANALOG INTEGRATED CIRCUITS")
display(pec204,fec204,dec204)
print("                                ")
print("SENSORS AND TRANSDUCERS")
display(pae204,fae204,dae204)
print("                                ")
print("ELECTRICAL ENGINEERING")
display(pee216,fee216,dee216)
print("                                ")
print("BUSINESS ECONOMICS")
display(phs200,fhs200,dhs200)
print("                                ")
print("ANALOG INTEGRATED CIRCUITS LAB")
display(pec232,fec232,dec232)
print("                                ")
print("TRANSDUCERS AND INSTRUMENTATION LAB")
display(pae232,fae232,dae232)
print("                                ")
