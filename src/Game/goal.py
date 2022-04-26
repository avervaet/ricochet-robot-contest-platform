class Goal:
    
    def __init__(self, color:str, pattern:str):
        self.color = color
        self.pattern = pattern
        self.name = f"{self.color}{self.pattern}"