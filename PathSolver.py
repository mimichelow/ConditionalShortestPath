import csv

from typing import List, Dict


class PathSolver:

    def __init__(self, filename: str = ""):
        self.network = {}
        if filename != "":
            with open(filename, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    stop = row["STOP"]
                    color = row["COLOR"]
                    lines = row["LINES"].split(",")
                    neighbors = row["NEIGHBORS"].split(",")
                    self.network[stop] = {
                        "COLOR": color,
                        "LINES": lines,
                        "NEIGHBORS": neighbors
                    }
        else:
            print(self.network)

    def fillFromDict(self, dict: Dict):
        self.network = dict

    @staticmethod
    def shortestAnswer(answers: List[str]) -> str:
        temp = [x for x in answers if x]
        temp.sort(key=len)
        for path in temp:
            return path
        return ""

    def shortestPath(self, start: str, end: str, color: str = "WHITE") -> str:
        answer = []
        if start == "" or end == "":
            return ""

        # Algoritmo que busca el camino más corto de manera recursiva, auxiliar para caminoMasCorto
        def DFS(node: str, goal: str, visited: List, line: int) -> str:
            # Definimos Casos Base
            if node in visited[0]:
                return ""
            if self.network[node]["COLOR"] == color or self.network[node]["COLOR"] == "WHITE" or color == "WHITE":
                visited[0] += node
            else:
                visited[1] += node

            if goal == node:
                return visited[0]

            # Si la parada es visitable la agrega a visitados[0] de lo contrario a visitados[1], luego va a los
            # vecinos

            candidates = []

            # Si la estación fue parada, vamos a todos los vecinos, de lo contrario vamos solo a los de la misma linea
            if node in visited[0]:
                for nextStop in self.network[node]["NEIGHBORS"]:
                    shared = [path for path in self.network[node]["LINES"] if path in self.network[nextStop]["LINES"]]
                    for way in shared:
                        temp = DFS(nextStop, goal, visited.copy(), way)
                        candidates.append(temp)
            else:
                for nextStop in self.network[node]["NEIGHBORS"]:
                    if line in self.network[nextStop]["LINES"]:
                        temp = DFS(nextStop, goal, visited.copy(), line)
                        candidates.append(temp)
            return PathSolver.shortestAnswer(candidates)

        # Necesitamos partir nuestro viaje en cada una de las lineas del metro a la cual pertenece la parada inicio
        for x in self.network[start]["LINES"]:
            answer.append(DFS(node=start, goal=end, visited=["", ""], line=x))
            # Nuestra respuesta es la más cortas de las respuestas no vacias, si todas son vacias, retorna vacio
        return PathSolver.shortestAnswer(answer)
