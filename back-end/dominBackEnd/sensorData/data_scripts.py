
class Scripts(object):

    def speed_bump(data):

        # raise Exception(float(data["vehicle_acceleration"]) <= 0.9)

        if (float(data["vehicle_acceleration"]) <= 0.9):
            return "Pot hole"
        return None
    



def get_event(data):

    if (Scripts.speed_bump(data)):
        return Scripts.speed_bump(data)
    
    return None
