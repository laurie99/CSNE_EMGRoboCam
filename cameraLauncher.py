# function to control the device by the channel signals
import usb

def cameraLauncher(status):
    device = usb.core.find(idVendor=0x2123, idProduct=0x1010)

    if device is None:
        print "Device not found"
    #if device.is_kernel_driver_active(0) is True:
    #    device.detach_kernel_driver(0)
    device.set_configuration()

    # check the Goniometer first
    Gonio = [status[3], status[5]]
    #Gonio = [(status[2]+status[3])/2, (status[4]+status[5])/2]
    print Gonio

    if Gonio[0] >= 0 or Gonio[1] >= 0:
        if Gonio[0] >= 0 and Gonio[0] > Gonio[1]:
            print "turn Down"
            device.ctrl_transfer(0x21,0x09,0,0,[0x02,0x01,0x00,0x00,0x00,0x00,0x00,0x00])
        if Gonio[1] >= 0 and Gonio[0] <= Gonio[1]:
            print "turn Up"
            device.ctrl_transfer(0x21,0x09,0,0,[0x02,0x02,0x00,0x00,0x00,0x00,0x00,0x00])
    # then check the EMG
    elif status[0] >= 0 or status[1] >= 0:
        if status[0] >= 0 and status[0] > status[1]:
            print "turn Left"
            device.ctrl_transfer(0x21,0x09,0,0,[0x02,0x04,0x00,0x00,0x00,0x00,0x00,0x00])
        if status[1] >= 0 and status[0] <= status[1]:
            print "turn Right"
            device.ctrl_transfer(0x21,0x09,0,0,[0x02,0x08,0x00,0x00,0x00,0x00,0x00,0x00])
    else:
        print "Stop"
        device.ctrl_transfer(0x21,0x09,0,0,[0x02,0x20,0x00,0x00,0x00,0x00,0x00,0x00])

    #print status
    return