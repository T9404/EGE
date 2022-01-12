for x in range(17, 1000):
    if ( hex(x)[2:][-1] == '2'  ) and ( len(hex(x)[2:]) == 2) :
        if ( oct(x)[2:][-2] == '4' ) and ( len(oct(x)[2:]) == 3):
            if ( bin(x)[2:][:2] == '10' ) and ( len(bin(x)[2:]) == 8):
                print(x)
                break
        
