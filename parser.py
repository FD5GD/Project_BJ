def time_millis(time):
    if time is None:
        return None
    out = ""
    hours = time // 3600000
    minutes = (time % 3600000) // 60000
    seconds = (time % 60000) // 1000
    millis = time % 1000
    out += str(hours) + ":" if hours else ""
    out += "0" if hours and minutes < 10 else ""
    out += str(minutes) + ":" if hours or minutes else ""
    out += "0" if (hours or minutes) and seconds < 10 else ""
    out += str(seconds) + "."
    out += "00" if millis < 10 else "0" if millis < 100 else ""
    out += str(millis)
    return out
