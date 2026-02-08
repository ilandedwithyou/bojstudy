N = int(input())

def findPrime(N):
    is_prime = [1] * (N + 1)
    is_prime[0] = 0
    is_prime[1] = 0

    for i in range(2, int(N**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, N + 1, i):
                is_prime[j] = 0

    primes = []
    for i in range(2, N + 1):
        if is_prime[i]:
            primes.append(i)

    return primes

def findSequence(primes, N):
    left = 0
    right = 0
    sums = 0

    while(1):
        if sums >= N:
            sums -= primes[left]
            left += 1
        else:
            if right == len(primes): 
                break
            sums += primes[right]
            right += 1

        if sums == N:
            answer += 1

    return answer

primes = findPrime(N)
answer = findSequence(primes, N)

print(answer)