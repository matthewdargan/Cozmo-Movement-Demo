def parseMessage(message: str):
    """
    Takes a cozmo message in the form "name;char1;char2;x;y" and returns a list of the form 
    [name, char1, char2, x (as a whole number), y (as a whole number)].

    name = unique name for your cozmo
    char1 = 'F' or 'B'
    char2 = 'L' or 'R'
    x = a whole number representing the number of millimeters to move either forward or backward
    y = a whole number representing the number of millimeters to move either left or right
    """

    separated = message.split(';')
    separated[3] = int(separated[3]) # ensure x is a whole number
    separated[4] = int(separated[4]) # ensure y is a whole number

    if len(separated) > 5:
        raise ValueError('Wrong number of elements passed in with the message string.')
    else:
        return separated

if __name__ == "__main__":
    assert parseMessage('Denise;F;L;200;300') == ['Denise', 'F', 'L', 200, 300]