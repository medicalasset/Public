## Requires the filename be sampleInput.txt

## TODO: Create cli parameters for input/ouput file names

import csv
import argparse

def main():

    ## OPTIONAL arguments for file names
    parser = argparse.ArgumentParser(
                    prog='Ingredient Organizer',
                    description='Organizes values from a csv')
    parser.add_argument('--input_file', default='sampleInput.txt')
    parser.add_argument('--output_file', default='sampleOutput.txt')
    args = parser.parse_args()

    ## Clearing/creating output file
    with open(args.output_file, "w") as outputFile:
        outputFile.write("")

    with open(args.input_file, newline="") as file:
         fileReader = csv.reader(file, delimiter=",", quotechar='|')
         conditionedInput = []
         for line in fileReader:
             with open(args.output_file, "a") as outputFile:
                 ## Stripping the leading space from each ingredient
                 ## otherwise the sorted method is inconsistent
                 for ingredient in line:
                     conditionedInput.append(ingredient.lstrip())
                 sortedInput = sorted(conditionedInput)
                 for ingredient in sortedInput:
                     outputFile.write(ingredient + "\n")


if __name__ == "__main__":

    main()
