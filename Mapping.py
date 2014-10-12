# function to map 6 channel signals to control missile
def Mapping(data):
    thresEMG = 6000
    thresGonio = 2500
    countMinReq = round(0.3 * len(data[0]))
    status = []
    
    # Processing EMG data on channel 0 and 1
    for i in range(2):
        count = 0
        for j in range(len(data[i])):
            #print type(data[i][j])
            if (int(data[i][j]) >= thresEMG):
                count += 1
        #print count
        status.append(count - countMinReq)
        #status[i] = (count - countMinReq)
            
    
    # Processing Goniometer data on channel 2,3,4,5
    # we want average between 2 and 3, 4 and 5
    for i in range(2,6):
        sum = 0
        for j in range(len(data[i])):
            sum += int(data[i][j])
        avg = sum / len(data[i])
        #print sum
        status.append(thresGonio - avg)
        #status[i] = (avg - thresGonio)
            
    return status
        
        