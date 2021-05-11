# -*- coding: utf-8 -*-
# ITMO files are intended to write python code for the academic files.
# Check the complete course at https://codeforces.com/edu/course/2
#
# Suffix Array: Step 1
# @author:JuanVidal - JProgrammer (CodeForces)

#%% Starting with the length 1 chars
arr = input()+'$'; l = len(arr); P = []; # Order of the string n (length 2^n)
for i in range(l): P.append((arr[i], i))
P.sort(key=None) # Sorting P0 = list(zip(*P))[1]

c = -1; C = [0]*l; # C = Class of the string n (length 2^n)
for i in range(l):
    if P[i][0] != P[i-1][0]: c+=1
    C[P[i][1]] = c;

#%% Generalizing the algorithm
n = 0;
while (1<<n) < l:
    P = [];
    for i in range(l): P.append((C[i], C[(i+(1<<n))%l], i))
    P.sort(key=lambda x: (x[0], x[1]))
    c = -1; C = [0]*l;
    for i in range(l):
        if P[i][0] != P[i-1][0]: c+=1
        elif P[i][1] != P[i-1][1]: c+=1
        C[P[i][2]] = c;
    if c == (l-1): break
    else: n += 1

print(*list(zip(*P))[2])
