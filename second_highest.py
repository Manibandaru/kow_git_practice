lt=[2,3,4,5,5,6,3,4,6]
winner=max(lt[0],lt[1])
runner=min(lt[0],lt[1])
for i in lt:
    if i>winner:
        runner=winner
        winner=i
print(runner)