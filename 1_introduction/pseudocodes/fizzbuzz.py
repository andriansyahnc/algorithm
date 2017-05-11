import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int,
                        help="Limit the fizzbuzz to Xth counter", required=True)
    return parser.parse_args()


def fizzbuzz():
    args = get_args()
    limit = args.limit
    
    for x in range(1, limit):
        print_number = True
        data = ""
        if x % 3 == 0:
            data = data + "Fizz"
            print_number = False
        if x % 5 == 0:
            data = data + "Buzz"
            print_number = False
        if print_number is True:
            data = data + str(x)
        
        print(data)
        

if __name__ == "__main__":
    fizzbuzz()
