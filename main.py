import csv
from PathSolver import PathSolver
from colorama import Fore

solution = PathSolver("network.csv")
TestCases = []

# Carga los casos en TestCases.csv en formato input="Estacion de inicio,estacion final,color" output= "Resultado
# Esperado" y formatea en un arreglo con un diccionario con el estacion inicial, estacion final,color y resultado
# esperado del caso


with open("TestCases.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        TestCases.append({"start": row["Input"].split(",")[0],
                          "end": row["Input"].split(",")[1],
                          "color": row["Input"].split(",")[2],
                          "output": row["Output"].split(",")})
        if TestCases[-1]["output"] == [""]:
            TestCases[-1]["output"] = []

# Run Test Cases

for case in TestCases:
    caseAnswer = solution.shortestPath(case["start"], case["end"], case["color"])
    if caseAnswer == "":
        if case["output"] == []:
            print(Fore.GREEN + f"Input {case} accepted,there are no valid paths")
        else:
            print(Fore.RED + f"Input {case} rejected, no valid path found but {case['output']} existed")
    else:
        if caseAnswer in case["output"]:
            print(Fore.GREEN + f"Input {case} accepted, answer was {caseAnswer}")
        else:
            print(Fore.RED + f"Input {case} rejected, output was {caseAnswer} but {case['output']} was expected")
