def all_primes(start, end):
        return list(sorted(set(range(start,end+1)).difference(set((p * f) for p in range(2, int(end ** 0.5) + 2) for f in range(2, (end/p) + 1)))))
        
 
x=all_primes(20,40)

print 'X is :', x        