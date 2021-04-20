def main():
    #write your code below this line
    first = int(input(""))
    second = int(input(""))
    
    if (first>second):
      print(str(first) + " is greater than " + str(second) +".")
    elif (first<second):
      print(str(first) + " is smaller than " + str(second) + ".")
    else:
      print(str(first) + " is equal to " + str(second) + ".")



if __name__ == '__main__':
    main()
