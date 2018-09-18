#player byrjar í (1,1) og getur þá farið bara north.
    #getur ekki slegið inn s,e og w.
#fá player til að slá inn direction.
    #player slær inn N 
    # komið í (1,2) getur þá slegið inn n, e, s
        # ef slegið inn vitlaust 
        # print(Not a valid direction!)
# (N)orth or (E)ast or (S)outh.
# 'n' or 'N'
# 's' or 'S'
# 'w' or 'W'
# 'e' og 'E'
#n => a + 0 
#n => b + 1
#s => a - 0
#s => b -1
#W => a -1
#w => b - 0
#e => a + 1
#e => b +0
# byrjar i 1,1
# (1,1) => n
# (1,2) = > n, e, s
# (1,3) => s og e
# (2,1) => n
# (2,2) => s og w
# (2,3) => w og e
# (3,1) => Victory!, ekki spurd um direction
# (3,2) => n og s
# (3,3) => w og s
north = '(N)orth'
east = '(E)ast'
west = '(W)est'
south = '(S)outh'
travel = 'You can travel: '
a = 1
b = 1

while a < 4:
    while b < 4:
        location = str(a) + str(b)
        
        if location == '11':
            print(travel + north + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                 b= 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'nN':
                    b = 2
                else:
                    print("Not a valid direction!")

        elif location == '12':
            print(travel + north + ' or ' + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 3 
            elif direction in 'sS':
                b = 1
            elif direction in 'eE':
                a = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'nN':
                    b = 3 
                elif direction in 'sS':
                    b = 1
                elif direction in 'eE':
                    a = 2
                else:
                    print("Not a valid direction!")

        elif location == '13':
            print(travel + east + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'eE':
                a = 2
            elif direction in 'sS':
                b = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'eE':
                    a = 2
                elif direction in 'sS':
                    b = 2
                else:
                    print("Not a valid direction!")

        elif location == '21':
            print(travel + north + '.')
            direction = str(input("Direction: "))
            if direction in 'nN':
                b = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'nN':
                    b = 2
                else:
                    print("Not a valid direction!")

        elif location == '22':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 1
            elif direction in 'wW':
                a = 1
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'sS':
                    b = 1
                elif direction in 'wW':
                    a = 1
                else:
                    print("Not a valid direction!")

        elif location == '23':
            print(travel + east + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'eE':
                a = 3
            elif direction in 'wW':
                a = 1
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'eE':
                    a = 3
                elif direction in 'wW':
                    a = 1
                else:
                    print("Not a valid direction!")

        elif location == '33':
            print(travel + south + ' or ' + west + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 2
            elif direction in 'wW':
                a = 2
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'sS':
                    b = 2
                elif direction in 'wW':
                    a = 2
                else:
                    print("Not a valid direction!")

        elif location == '32':
            print(travel + north + ' or ' + south + '.')
            direction = str(input("Direction: "))
            if direction in 'sS':
                b = 1
            elif direction in 'nN':
                b = 3
            else:
                print("Not a valid direction!")
                direction = str(input("Direction: "))
                if direction in 'sS':
                    b = 1
                elif direction in 'nN':
                    b = 3
                else:
                    print("Not a valid direction!")
                
        else:
            print('Victory!')
            b = 5
            a = 5