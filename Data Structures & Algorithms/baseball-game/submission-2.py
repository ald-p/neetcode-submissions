class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []

        for operation in operations:              
            if operation == "+":
                last_two = scores[-1] + scores[-2]
                scores.append(last_two)
            elif operation == "D":
                new_score = 2 * scores[-1]
                scores.append(new_score)
            elif operation == "C":
                scores.pop()
            else:
                scores.append(int(operation))

        return sum(scores)
        