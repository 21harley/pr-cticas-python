def main():
    for i in range(1,101): 
        print("fizz" if i%3==0 and i%5!=0 else ("buss" if i%5==0 and i%3!=0 else ("fizzbuss" if i%3==0 and i%5==0 else i)))

if __name__ == '__main__':
    main()