def same_ends(list):
    if list:
        if list[0] == list[-1]:
            return True
        else:
            return False
    else:
        return False