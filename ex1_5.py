def checkpara (paradot):
    """Check if the number of closed paratheses is equal to the number of open parathenses"""
    if paradot.count('(')==paradot.count(')'):
        return True
    else:
        return False
