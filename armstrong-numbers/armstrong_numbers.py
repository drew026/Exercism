def is_armstrong_number(number):
    arm_num = 0
    arm_list = str(number)
    for char in arm_list:
        arm_num = arm_num + (int(char) ** len(arm_list))
    if arm_num == number:
        return True
    else:
        return False
    
    
