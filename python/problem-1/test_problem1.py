from problem_1 import add_up_k

def test_problem_1():
    k = 10
    # addlist = [2,3,4,9]  #will fail
    addlist = [4, 19, 6, 9, 1] # will pass

    assert add_up_k(k, addlist)