## Requires the filename be sampleInput.txt

## TODO: Create cli parameters for input/ouput file names

import csv

def main():

    output_file = "sampleOutput.txt"
    input_file = "sampleInput.txt"
    ## Clearing/creating output file
    with open(output_file, "w") as outputFile:
        outputFile.write("")

    with open(input_file, newline="") as file:
         fileReader = csv.reader(file, delimiter=",", quotechar='|')
         conditionedInput = []
         for line in fileReader:
             with open(output_file, "a") as outputFile:
                 ## Stripping the leading space from each ingredient
                 ## otherwise the sorted method is inconsistent
                 for ingredient in line:
                     conditionedInput.append(ingredient.lstrip())
                 sortedInput = sorted(conditionedInput)
                 for ingredient in sortedInput:
                     outputFile.write(ingredient + "\n")
                 
                 

if __name__ == "__main__":

    main()
