lst=["deal","dog","deer"]
pfx="de"
for i in lst:
    if i[:len(pfx)]==pfx:
        print(i)
