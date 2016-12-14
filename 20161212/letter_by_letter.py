#!/usr/local/bin/python3

s1 = "floor"
s2 = "brake"

print(s1)
for i in range(len(s1)):
    if s1[i] != s2[i]:
        print(s2[:i+1] + s1[i+1:])
