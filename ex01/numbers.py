
def print_numbers():
    try: 
        # open de file in read mode
        f = open("numbers.txt", "r")

        # Read the file
        # print(f.read())

        # Todo : split the numbers
        clean_numbers = f.read().split(",")    

        # todo : print the numbers with new line
        for number in clean_numbers:
            print(int(number))

        # Close the file
        f.close()
    except FileNotFoundError:
        print("File not found, please is nesesarly numbers.txt file")
    except:
        print("An error occured")

if __name__ == '__main__':
    print_numbers()