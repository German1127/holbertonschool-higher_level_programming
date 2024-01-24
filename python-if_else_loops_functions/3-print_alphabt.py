#!/usr/bin/python3
for x in range(ord("a"), ord("z")):
    if x == ord("e") or x == ord("q"):
        continue
    else:
        print("{}".format(chr(x)), end="")
