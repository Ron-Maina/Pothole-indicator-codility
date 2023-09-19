def Pothole_indicator(R):
    sub_arr =  []
    pothole_indicator = 0

    for num in R:
        if num != 0:
            sub_arr.append(num)
        else:
            if sub_arr:
                print(sub_arr)
                RK = max(sub_arr)*len(sub_arr)
                if RK > pothole_indicator:
                    pothole_indicator = RK
                sub_arr = []
    if sub_arr:
        print(sub_arr)
        RK = max(sub_arr)*len(sub_arr)
        if RK > pothole_indicator:
            pothole_indicator = RK
        sub_arr = []

    print(f'Pothole Indicator: {pothole_indicator}')
Pothole_indicator([1, 4, 1, 0, 5, 2, 3, 0, 8])
