# https://stackoverflow.com/questions/33923/what-is-tail-recursion
# https://www.baeldung.com/cs/tail-vs-non-tail-recursion
"""
    Program to convert decimal to binary demonstrating
    basic recursion. This function is also tail recursive.

    A function is tail-recursive if it ends by returning 
    the value of the recursive call. Keeping the caller's 
    frame on stack is a waste of memory because there's 
    nothing left to do once the recursive call returns its 
    value. So, instead of allocating a new frame for the
    call, we can reuse the existing one.

    In traditional recursion, the typical model is that you 
    perform your recursive calls first, and then you take 
    the return value of the recursive call and calculate the 
    result. In this manner, you don't get the result of your 
    calculation until you have returned from every recursive 
    call.

    In tail recursion, you perform your calculations first, and 
    then you execute the recursive call, passing the results of 
    your current step to the next recursive step. This results 
    in the last statement being in the form of 
    (return (recursive-function params)). Basically, the return 
    value of any given recursive step is the same as the return 
    value of the next recursive call.

    The consequence of this is that once you are ready to perform 
    your next recursive step, you don't need the current stack frame 
    any more. This allows for some optimization. In fact, with an 
    appropriately written compiler, you should never have a stack 
    overflow snicker with a tail recursive call. Simply reuse the 
    current stack frame for the next recursive step. Scheme does
    this but Common Lisp does not.

    To benefit from tail-call optimization, a function need not be 
    recursive. It can call any function, as long as the only thing 
    to do after the call is to return the called function’s value.
"""
def decimal_to_binary(decimal):
    # Base case / stopping condition
    if decimal == 0:
        return 0
    else:
        # Inductive step: Do some work to shrink the problem space
        return (decimal % 2 + 10 * decimal_to_binary(int(decimal // 2)))

if __name__ == '__main__':
    print(decimal_to_binary(4))