def wgbtindoors(wet=0, black=0, dry=0) -> float:
    return 0.7 * wet + 0.2 * black + dry * 0.1


def wbgtoutdoors(wet=0, black=0) -> float:
    return 0.7 * wet + 0.3 * black
