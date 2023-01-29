data=[15, 30, 15, 30, 30, 30, 30, 40]
def upValue(value_a,value_b,print_v=0):
    if(value_a==value_b):
        if(print_v==1): print('Deuce')
        return 0
    elif(value_a>value_b):
        if(print_v==1): print('Ventaja P1')
        return 1
    else:
        if(print_v==1): print('Ventaja P2')
        return 2
        
def main(array):
    pos_1=[0,1,4,6,7]
    pos_2=[-1,-1,2,3,5]
    for i in range(0,5):
        if(pos_2[i]==-1):
            print(f'{data[pos_1[i]]} - Love')
        else:
            print(f'{data[pos_1[i]]} - {data[pos_2[i]]}')

    suma_1=data[0]+data[1]+data[4]
    suma_2=data[2]+data[3]+data[5]
    upValue(suma_1+data[6],suma_2)
    aux=upValue(suma_1+data[7],suma_2,1)
    print("Ha ganado el P1" if aux==1 else ('Ha ganado el P2' if aux==2 else 'Empate entre P1 y P2'))


if __name__=='__main__':
    main(data)