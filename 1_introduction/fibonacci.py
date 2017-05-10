import argparse

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--limit', type=int,
                        help="Limit the fizzbuzzwoof to Xth counter", required=True)
    return parser.parse_args()

def fibonacci():
    args = get_args()
    limit = args.limit

    first = 1
    second = 1

    if limit == 1 or limit == 2:
        print(1)
    else:
        for x in range(3, limit+1):
            temp = second
            second = first + second
            first = temp
        print(second)

if __name__ == "__main__":
    fibonacci()