import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int,
                        help="Limit the fizzbuzzwoof to Xth counter", required=True)
    return parser.parse_args()


def fizzbuzzwoof():
    args = get_args()
    limit = args.limit
    
    print_number = True
    data = ""
    if limit % 3 == 0:
        data = data + "Fizz"
        print_number = False
    if limit % 5 == 0:
        data = data + "Buzz"
        print_number = False
    if limit % 7 == 0:
        data = data + "Woof"
        print_number = False
    if print_number is True:
        data = data + str(limit)
    
    print(data)
        

if __name__ == "__main__":
    fizzbuzzwoof()
