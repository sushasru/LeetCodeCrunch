def insert(intervals,newintervals):
    print("Intervals:",intervals)
    print("NewIntervals:",newintervals)
    for index,interval in enumerate(intervals):
        for i in newintervals:
            if interval[0] > i:
                interval[0] == i
                del newintervals[0]
            
            
    print("Intervals:",intervals)
                


intervals = [[1,3],[6,9]]
newinterval = [2,5]
print(intervals[0][0])
insert(intervals,newinterval)
