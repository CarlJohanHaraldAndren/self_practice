import math
def circle_area(r):
    area=math.pi*r**2
    return area

def circle_circumference(r):
    circumference=2*math.pi*r
    return circumference

def cylinder_area(r,h):
    cap=circle_area(r)
    side_area=circle_circumference(r)*h
    total_area=2*cap+side_area
    return total_area

print(cylinder_area(2,4))


