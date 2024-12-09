# Writeup for hidden-data-p1
## TShark Command
```
.\tshark.exe -r hidden-data-p1.pcapng -Y "usb.src == 1.8.1" -T "fields" -e usbhid.data > hidden-data-p1.txt
```

## Fix encoding
Convert from UTF-16 to UTF-8

## Run Python script
### Program Output
```
Decoded ASCII output: byuctf{usb_d4t4_1s_s0_c00l}
```


# Writeup for hidden-data-p2
## TShark Command
```
.\tshark.exe -r hidden-data-p2.pcapng -Y "usb.src == 1.25.1" -T "fields" -e usbhid.data > hidden-data-p2.txt
```

## Fix encoding
Convert from UTF-16 to UTF-8

## Run Python
### Program Output
```
Decoded ASCII output: byuctf{D0nt_F0rg3t_B4cksp4c3s}
```




# Writeup for hidden-data-p3
## TShark Command
```
.\tshark.exe -r hidden-data-p3.pcapng -Y "usb.src == 1.22.1 || usb.src == 1.22.2" -T "fields" -e usbhid.data > hidden-data-p3.txt
```

### Program Output
```
Decoded ASCII output: byuctf[wh4t_4_w31rd_usb]
```




# Writeup for mouse-hunt-p1
## TShark Command
```
.\tshark.exe -r C:\Users\willi\Documents\BYU_Courses\Fall_2024\ECEN_522r_HardwardHacking\ECEN-522R-Final-Project\captures\mouse-hunt-p1.pcapng -Y "usb.src == 1.34.1" -T "fields" -e usbhid.data > C:\Users\willi\Documents\BYU_Courses\Fall_2024\ECEN_522r_HardwardHacking\ECEN-522R-Final-Project\writeups\mouse-hunt-p1.txt
```




# Real used
```
.\tshark.exe -r C:\Users\willi\Documents\BYU_Courses\Fall_2024\ECEN_522r_HardwardHacking\ECEN-522R-Final-Project\captures\hidden-data-p1.pcapng -Y "usb.src == 1.8.1" -T "fields" -e usbhid.data > C:\Users\willi\Documents\BYU_Courses\Fall_2024\ECEN_522r_HardwardHacking\ECEN-522R-Final-Project\writeups\hidden-data-p1.txt
```