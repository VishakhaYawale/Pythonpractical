import statistics
def average(1st):
    return sum(1st)/len(1st)

    def mean(1st)
        return sum(1st)/len(1st)

        def median(1st)
            1st.sort()
            1st_len=len(1st)
            if(1st_len % 2 == 0)
                median1=1st[1st_len//2]
                median2=1st[1st_len//2-1]
                median=(median1+median2)/2
                return median
            else:
                median=1st[1st_len//2]
                return median
            1st=[6,8,1,2,5,9]
            print("Element i list:",1st)
            print()
            print("Average of List:{:.3f}".format(average(1st)))
            print("Mean of List:{:.3f}".format(mean(1st)))
            print("Median of List:{}".format(median(1st)))
            print("Standard deviation:{:.3f}".format(statistics.stdev(1st)))