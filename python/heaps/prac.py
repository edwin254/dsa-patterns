# implement a python decorator that takes a file pointer as argument a logs function call arguments
# e.g 
@log(file_pointer)
def my_max(a,b,c ):
    return max(a,b,c)

#implement log decorator
@log
def my_max(a,b,c ):
    return max(a,b,c)

