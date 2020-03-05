


#13







def Collatz(n): 

    while n != 1: 
       
        print(n, end = ' ') 
  
        # If n is odd  
        if n & 1: 
            n = 3 * n + 1
  
        # If even  
        else: 
            n = n // 2
  
    # Print 1 at the end  
    print(n) 
  

#n = input('Enter a number')
#test_number = int(n)  
 
Collatz(12) 