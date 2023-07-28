# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    numberOfStamps = int(input())
    
    countries = set()
    
    for coutry in range(numberOfStamps):
        new = input()
        countries.add(new) #the add mehtod only adds it to the set if it a new entry 
                            #so the length of the set is by default the total distinct number of countries
    
    length = len(list(countries))
    print(length)
    