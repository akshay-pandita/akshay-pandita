import math
def convert(s, num_rows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    len_str = len(s)
    len_lst = int(len_str/2)
    ciel_lst = math.ceil(len_lst)
    temp_lst = []
    for _ in range(num_rows):
        new_lst = []
        for _ in range(ciel_lst):
            new_lst.append(0)
        temp_lst.append(new_lst)

    tracker = 1
    lst_tracker = 0
    col_tracker = 0
    mis_elem_tracker = 1
    skip_col = False
    for i in range(len_str):
        if num_rows >= 3:
            if i < tracker * 2 * (num_rows - 1):
                if lst_tracker <= num_rows - 1 and not skip_col:
                    if skip_col is False:
                        temp_lst[lst_tracker][col_tracker] = s[i]
                        print ("Index is %s, lst is %s" % (i, temp_lst))
                        lst_tracker = lst_tracker + 1
                else:
                    skip_col = True
                    lst_tracker = num_rows - mis_elem_tracker - 1
                    if lst_tracker != 0:
                        col_tracker = col_tracker + 1
                        temp_lst[lst_tracker][col_tracker] = s[i]
                        print("Index is %s, lst is %s" % (i, temp_lst))
                        mis_elem_tracker = mis_elem_tracker + 1
                    else:
                        mis_elem_tracker = 1
            else:
                tracker = tracker + 1
                skip_col = False
                lst_tracker = 0
                col_tracker = col_tracker + 1
                temp_lst[lst_tracker][col_tracker] = s[i]
                print("Index is %s, lst is %s" % (i, temp_lst))
                lst_tracker = lst_tracker + 1
                mis_elem_tracker = 1

    print ("We are here")
    final_str = ""
    for i in range(len(temp_lst)):
        for j in temp_lst[i]:
            if j !=0:
                final_str=final_str+j
    return final_str

if __name__ == "__main__":
    final_str = convert("PAYPALISHIRING", 4)
    print ("Final str is %s" % final_str)
    # new_final = ""
    # for i in range(len(final_str)):
    #   if final_str[i] != 0:
    #     new_final = new_final + final_str[i]
    # print (new_final)

