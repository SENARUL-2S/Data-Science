# # function jevabe toiri kore

# def is_even(i): # def=> keyword, is_even=> function name , here i=> parameter  

#     # docstring 
#     """
#     this function return if a given number is odd or even
#     input- any valid integer
#     output-odd or even
#     create on 11-02-25
#     """ 
#     if i%2==0:
#      return 'even'
#     else:
#        return 'odd'
# # function jevabe use kore
# for i in range(1,11):
#    x=is_even(i)
#    print(x)

# function ar documentation je vabe dekhe
# print(is_even.__doc__)
# print(print.__doc__)
# print(type.__doc__)


# # 2 points of view
# def is_even(i):
#     if type(i)==int:
#       if i%2==0:
#        return 'even'
#       else:
#        return 'odd'
#     else: 'pagol naki tumi'
      
# for i in range(1,11):
#    x=is_even(i) # here i=> argument
#    print(x)


# types of function 
 # defult argument - mane kew jodi akta argument pass kore tahole se autometic arek ta niya nibe 

# def power(a=1,b=1): # akhane a b ar man deya tai ara argument
#   return a**b
# x=power(2)
# y=power()
# z=power(2,3)
# print(x,y,z)

# positional argument - mane a te 2 jabe ar b te 3 jabe 

#  keyword argument -position ar proyojon hoina 
#s=power(b=3, a=2)  # mane a jekhanei thak a=2 ar b=3


# *args to pass any number of non-keyword arguments
# def mul(*args): # args = senarul dile o kaj korbe just name
#     product=1

#     for i in args:
#         product=product*i
    
#     return product
# print(mul(1,2,3)) # mainly this is a tuple
# print(mul(1,2,3,4,5,6)) # tar mane joto gula number dei sob mul kore dibe


# **kwargs to pass any number of keyword arguments
# this is a disctnaries  baniye dey

# def display(**kwargs):
#     for (key,value) in kwargs.items():
#         print(key,'->',value)

# display(bangladesh='dhaka',pakistan='kolombo') # joto mon add korte parbo


# how function executed OR operate in memory/RAM 

# def is_even(i):
   
#       if i%2==0:
#        return 'even'
#       else:
#       return 'odd'
     
# print(is_even(7))

#check python tutor
# global frame jekhane function execute hoi abong sokol variable akhane toiri hoi- 
 
#function choto independent program ar moto kaj kore and function ar kaj ses hoyar sathe sathe room/function ar block delete hoye jai
# function ar life time  call theke return porjonto
# mane ram a koto khon active thake :call theke return porjonto


#jodi function a return na lagai tahole se autometic (return value = none) rerurn korbe

# vvi python tutor 

# def is_even(i):
   
#       if i%2==0:
#        print('even')
#       else:
#        print('odd')
     
# print(is_even(7))

# # or
# l=[1,2,3]
# s=l.append(4) 
# print(s) # None 
# print(l) # 1,2,3,4

