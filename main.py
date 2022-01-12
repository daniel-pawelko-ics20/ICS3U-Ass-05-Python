#!/usr/bin/env python3

# Created by: Daniel Pawelko
# Created on: Jan 2022
# Multiplication table


def main():
    # main function for multiplication table

    # process/output
    for first_num in range(10):
        for second_num in range(10):
            print(f"{first_num} x {second_num} = {first_num * second_num}")

    # done
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
