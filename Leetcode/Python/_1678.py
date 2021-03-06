class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("(al)", "al").replace("()", "o")
        
class Solution:
    def interpret(self, command: str) -> str:
        string = str()
        for idx, char in enumerate(command):
            if char == 'G':
                string += char
            elif char == '(':
                if command[idx+1] == ')':
                    string += 'o'
                elif command[idx+1] == 'a':
                    string += 'al'
                else:
                    pass
            else:
                pass
        return string
   
class Solution:
    def interpret(self, command: str) -> str:
        string = str()
        for idx, char in enumerate(command):
            if char == 'G':
                string += char
            elif char == '(' and command[idx+1] == ')':
                string += 'o'
            elif char == '(' and command[idx+1] == 'a':
                string += 'al'
            else:
                pass
        return string

 class Solution:
    def interpret(self, command: str) -> str:
        
        mapping = [
            ('G','G'),
            ('()','o'),
            ('(al)', 'al')
        ]
        
        parsed = []
        i = 0
    
        while i < len(command):
            
            for _from, _to in mapping:
                
                len_from = len(_from)

                if _from == command[i:i+len_from]:
                    parsed.append(_to)
                    i = i + len_from
                    break
                        
        return "".join(parsed)
