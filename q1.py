def solve_box_problem():
    box = [0, 860, 15, 1, 1, 3] 
    answer_a = None
    answer_b = None
    line = 1
    
    while True:
        if line == 1:
            box[5] = box[5] * 2
            line = 1 + 5
        elif line == 2:
            box[3] = box[3] * 2
            line = 2 + 3
        elif line == 3:
            box[2] = box[5] + box[2]
            line = 7
        elif line == 4:
            answer_a = box[3]
            line = 1
        elif line == 5:
            box[4] = box[3] + box[4]
            line = 3
        elif line == 6:
            box[3] = box[4] + box[3]
            line = 2
        elif line == 7:
            if box[2] > 100:
                line = 9
            else:
                line = 8
        elif line == 8:
            if box[2] > 50:
                line = 4
            else:
                line = 1
        elif line == 9:
            answer_b = box[3]
            line = 10
        elif line == 10:
            break
            
    return answer_a, answer_b

ans_a, ans_b = solve_box_problem()
print(f"ANSWER - BOX A : {ans_a}")
print(f"ANSWER - BOX B : {ans_b}")