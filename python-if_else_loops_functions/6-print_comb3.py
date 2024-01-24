#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i == j:
            continue
        print(f"{i}{j}", end=", ")