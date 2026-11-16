class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> list[str]:
        n = len(currentState)
        result = []

        for i in range(n-1):
            if currentState[i]=="+" and currentState[i+1]=="+":
                new_state = currentState[:i]+"--"+currentState[i+2:]

                result.append(new_state)

        return result


        