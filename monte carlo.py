import random

def estimate_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        distance = x ** 2 + y ** 2
        if distance <= 1:
            inside_circle += 1
    pi_estimate = (inside_circle / num_samples) * 4
    return pi_estimate



#pi_estimate = estimate_pi(100000000)
#print(pi_estimate)

##for lenovo t480 with intel i5-8350
#10 samples is 0.1s
#100 sameples is 0.1s
#1000 samples is 0.1s
#10k samples is 0.1s
#100k samples is 0.2s
#1MM samples is 0.2s
#10MM samples is 8s
#100MM samples is 80s
#______________________

def fib(num):
    fibonacci = [0,1,1,2,3,5,8] 
    while len(fibonacci) < num:
        f_next = fibonacci[-2]+fibonacci[-1]
        fibonacci.append(f_next)
    
    #print(fibonacci)
    print(fibonacci[-1])
fib(200000)

##for lenovo t480 with intel i5-8350
#fib 10 takes 0.1s
#fib 100 takes 0.1s
#fib 1,000 takes 0.1s
#fib 10,000 takes 0.1s
#fib 100,000 takes 0.5s
