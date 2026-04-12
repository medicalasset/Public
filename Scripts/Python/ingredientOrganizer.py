## Requires the filename be sampleInput.txt

import csv

def main():

    ## Clearing/creating output file
    with open("sampleOutput.txt", "w") as outputFile:
        outputFile.write("")

    with open("sampleInput.txt", newline="") as file:
         fileReader = csv.reader(file, delimiter=",", quotechar='|')
         conditionedInput = []
         for line in fileReader:
             with open("sampleOutput.txt", "a") as outputFile:
                 ## Stripping the leading space from each ingredient
                 ## otherwise the sorted method is inconsistent
                 for ingredient in line:
                     conditionedInput.append(ingredient.lstrip())
                 sortedInput = sorted(conditionedInput)
                 for ingredient in sortedInput:
                     outputFile.write(ingredient + "\n")
                 
                 

if __name__ == "__main__":

    main()
