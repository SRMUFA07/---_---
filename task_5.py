def duo(n):
    digits = '0123456789AB'
    if n < 12:
        return digits[n]
    return duo(n//12) + digits[n % 12]
    
res = []
for n in range(144, 10000):
    s = duo(n)
    if n % 12 == 0:
        s += s[-3:]
    else:
        s = duo(n % 12 * 3) + s 
            
            
    if int(s, 12) < 58000:
        res.append((int(s, 12), n))
        
    print(sorted(res, reverse = True)[0])