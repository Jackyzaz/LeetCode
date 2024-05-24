def angleClock(hour: int, minutes: int) -> float:
    H_angle = (hour%12*30)
    HM_angle = (minutes/60*30)
    M_angle = minutes/60*360
    return abs(((M_angle-H_angle-HM_angle) + 180 )% 360 -180)

print(angleClock(hour=1,minutes=57))