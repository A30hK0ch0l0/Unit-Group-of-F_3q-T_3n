#!/usr/bin/env python
# coding: utf-8

# # Python Code for Generating Unit Group of F_{3^q}T_{3(3k+1)}

# In[ ]:


# For $G=T_{3n}=\{x,y|x^n=y^3=1,x^y=x^t\}$,
# that $n=3k+1$, insert $k>0$ and $t>1$, below and excute.
k =
t =

import timeit
import time
import platform
from functools import reduce
from decimal import Decimal

Start = timeit.default_timer()

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

def lcm(a, b):
    c = max(a, b)
    greater = c
    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        greater += c
    return lcm

def get_gcd_for(your_list):
    return reduce(lambda x, y: gcd(x, y), your_list)

def get_lcm_for(your_list):
    return reduce(lambda x, y: lcm(x, y), your_list)

def dec(n):
    a = '%.1E' % n
    return a

n = 3 * k + 1
ink_l = k
ink_u = ink_l + 1
for k in range (ink_l, ink_u):
    #print('n=', n)
    Main_Boolean = True
    a = t**3
    b = a-1
    e = b%n
    if (e != 0):
        print('There is No Group by These Numbers!')
        Main_Boolean = False
        break
    
    l = t-1
    q = gcd(n,l)
    if (q != 1):
        print('There is No Group that Satisfies Our Restrictions!')
        Main_Boolean = False
        break
    
    if (Main_Boolean):
        
        Conj_Boolean = True
        Conj_Array = []

        pn = platform.node()
        pp = platform.platform()

        sumConLen = 0
        sumTime = 0
        maxLen = 0

        PreString = ""
        MidString = ""
        FinString = ""

        PreString += """% Copy this code into Latex environment"""
        PreString += """ and compile with XeLaTeX %

        \\documentclass[a4paper]{amsart}

        \\usepackage{mathrsfs}
        \\usepackage{hyperref}

        \setlength\parindent{0pt}

        \\newcommand{\\f}{\mathbb{F}}
        \\newcommand{\\ti}{\\times}
        \\newcommand{\op}{\oplus}

        \\renewcommand{\d}{\Delta}
        \\renewcommand{\\u}{\mathscr{U}}

        \\begin{document} \n \n"""


        m = 3*n

        MidString += "$ \\begin{array}{*5l} \\\\ $\n"
        MidString += "$ k & = & "+str(k)+" \\\\ $\n"
        MidString += "$ n & = & 3k+1 & = & "+str(n)+" \\\\ $\n"
        MidString += "$ G & = & T_{3n} & = & T_{"+str(m)+"} \\\\ $\n"
        MidString += "$ RG & = & \\f_{3^q}T_{"+str(m)+"} \\\\ $\n"
        MidString += "$ RG & = & R(G/H) & \op & \d(G,H) \\\\ $\n"
        MidString += "$ \\f_{3^q}T_{"+str(m)+"} & = &"
        MidString += "  \\f_{3^q}(C_3) & \op & \d(G,H) \\\\ $\n"
        MidString += "$ \\u(\\f_{3^q}T_{"+str(m)+"}) & = &"
        MidString += "  \\u(\\f_{3^q}(C_3)) & \\ti & \\u(\d(G,H)) \\\\ $\n"
        MidString += "$ \\u(\\f_{3^q}(C_3)) & = "
        MidString += "& C_3^{2q} \\ti C_{3^{q}-1} \\\\ $\n"
        MidString += "$ \end{array} \\\\ \\\\ $\n \n"

        cons = {}
        totalCon = []
        init = 1
        lenCons = []
        while True:
            initTemp = 0
            index = 0
            con = []
            con.append(init)
            tempCon_1 = (con[index] * 3)%n
            tempCon_2 = (tempCon_1  * t)%n
            tempCon_3 = (tempCon_2  * t)%n
            tempCon   = min(tempCon_1, tempCon_2, tempCon_3)
            while tempCon != con[0]:
                tempCon_1  = (con[index] * 3)%n
                tempCon_2  = (tempCon_1  * t)%n
                tempCon_3  = (tempCon_2  * t)%n
                tempCon    = min(tempCon_1, tempCon_2, tempCon_3)
                index += 1
                if tempCon != con[0]:
                    con.append(tempCon)
            for i in con:
                totalCon.append(i)

            for i in range(init,n-1):
                tempI_1 = (i+1)%n
                tempI_2 = (tempI_1  * t)%n
                tempI_3 = (tempI_2  * t)%n
                tempI   = min(tempI_1, tempI_2, tempI_3)
                if tempI not in totalCon:
                    initTemp = tempI
                    break

            sumConLen += len(con)
    #       print ( sumConLen )

            cons[init] = con
            lenCons.append(len(con))
            if not initTemp: 
                break
            else:
                init = initTemp
    #   for index1, i in cons.items():
    #       print(index1 )
    #       print(i)
        maxLen = max(lenCons)
        for i in lenCons:
            if maxLen % i != 0:
                Conj_Array.append(k)
                Conj_Boolean = False
                break
        """if not Conj_Boolean:
            break"""

        kmm = get_lcm_for(lenCons)

        counter = 0
        facArray = sorted(factors(kmm))
    #   print (factors(kmm))
    #   print (facArray)
        for f in facArray:
            counter += 1
            temp_string    = "\gcd(q, "+str(kmm)+")="+str(f)
            temp_string_1  = " \\\\ \n\d(G,H) = "
            temp_string_2  = " \\\\ \n\\u(\\f_{3^{q}} T_{"+str(m)+"})="
            temp_string_2 += " C_3^{2q} \\ti C_{3^{q}-1} \\ti "
            indexa = [0] * (kmm + 1)
            for i in lenCons:
                bmm = gcd(f,i)
                indexa[int(i/bmm)] += bmm
            for i in range(len(indexa)):
                if indexa[i]:
                    tts = "^{"+str(indexa[i])+"}"
                    tti = "_{"+str(int(i))+"}"
                    if indexa[i] == 1:
                        tts = ""
                    elif indexa[i] == 0:
                        break
                    if i == 1:
                        tti = ""
                    temp_string_1 += "M_3(F"+tti+")"+tts+" \op "
                    temp_string_2 += "GL_3(F"+tti+")"+tts+" \\ti "
            temp_string_1 = temp_string_1[:-4]
            temp_string_2 = temp_string_2[:-5]
            temp_string  += temp_string_1 + temp_string_2

            if counter == len(facArray):
                MidString += "$ " + temp_string + " $\n \n"
            else:
                MidString += "$ " + temp_string + " \\\\ $\n \n"
        MidString +="""\\newpage""" + "\n \n"

        if not Conj_Boolean:
            FinString += "Conjecture is " + str(Conj_Boolean)
            FinString += " for k in " + str(Conj_Array) + " \\\\ \n"
            FinString += "Please confirm me what number (k), "
            FinString += "and characteristic you test \\\\ \n"
            FinString += "\href{mailto:Ali.Ashja@Modares.ac.ir}"
            FinString += "{Ali.Ashja@Modares.ac.ir} \\\\ \n \n"

        FinString += """\end{document}"""

        localtime = time.asctime( time.localtime(time.time()) )

        Stop = timeit.default_timer()

        Time_Total = Stop - Start

        Duration = dec(Time_Total).replace("E-0", "E-").replace("E+0", "E+")

        PreString += "Computed in " + str(Duration) + "\' sec at "
        PreString += str(localtime) + " by " + pn + " \\\\ \n"
        PreString += "% running " + pp + " % \\\\ \\\\ \n \n"

        TexString = PreString + MidString + FinString

        TexName = "U(F_3^q T_" + str(m) + ")"

        f = open(TexName + ".tex","w+")
        f.write(TexString)
        f.close()

        print (TexString)

