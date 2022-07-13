#quadratic equation solution
#ax^2+bx+c=0
import cmath
import math
import streamlit as st
# import keyboard as kd
st.title("Find the solutions:-")





def sol(a,b,c):
    determinant = (b**2) - (4*a*c)
    
    if(determinant<0):
        print("Roots are complex numbers:-")
        x1 = (-b + cmath.sqrt(determinant))/(2*a)
        x2 = (-b - cmath.sqrt(determinant))/(2*a)
        # print("x1 = {} and x2 = {}".format(x1,x2))
        st.write("value of x1 : {:.2f}".format(x1))
        st.write("value of x2 : {:.2f}".format(x2))
#     elif(determinant==0):
#         print("Roots are real and equal")
#         x1 = (-b + math.sqrt(determinant))/(2*a)
#         print("both x1 and x2 are {}".format(x1))
    else:
        #min = "content" if a>b else "content"
        text = "Roots are real and unequal" if(determinant>0) else "Roots are real and equal"
        print("{}:-".format(text))
        x1 = (-b + math.sqrt(determinant))/(2*a)
        x2 = (-b - math.sqrt(determinant))/(2*a)
        # print("x1 = {} and x2 = {}".format(x1,x2))
        st.write("value of x1 : {:.2f}".format(x1))
        st.write("value of x2 : {:.2f}".format(x2))
        

def takeInput():
    st.subheader("standard quadratic equation is => ax^2+bx+c=0 :-")
    
    a = st.number_input("Enter value of a :",value=1)
    b = st.number_input("Enter value of b :",value=1)
    c = st.number_input("Enter value of c :",value=1)
   
    if st.button("Enter"):
        sol(a,b,c)
    
takeInput()



#-x^2+45x-324=0
#x2 x 2 -4x + 4 = 0
#sol => x1 = 36, x2 = 9
        