import sys
import fileinput

def fall_asleep(N, t, tol = 1.0e6):
    if N == 0:
        print("Case #" + str(t) + ":", "INSOMNIA")
        return
    track_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    i = 1
    while track_digits != []:
        num = i*N
        i += 1
        for j in str(num):
            if j in track_digits:
                track_digits.remove(j)
    print("Case #" + str(t) + ":", str(num))
    #print('          'Numbers counted:', str(i))

def grand_func(N_list, T):
    t = 1
    for N in N_list:
        if t <= T:
            fall_asleep(int(N), t)
            t += 1
        else:
            return

#File can be found on the Google Code Jam website
#Here we import the file locally
filepath = 'C:\\Users\\Sigi Peschke\\Python_File_Read_To\\2016-Google-Code-Jam-Counting-Sheep-Input.in'
file = open(filepath, 'r')
T = 100 #Need to make this an input as well
grand_func(file, T)
file.close()
