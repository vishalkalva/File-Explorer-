import os 

class FileExplorer:
    def __init__(self):
        self.current_path = os.getcwd()

explorer = FileExplorer()
print(explorer.current_path)


#just working on it
