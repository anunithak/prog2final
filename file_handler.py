import os
import random
import matplotlib.pyplot as plt



def deco(color: str):
    # ANSI Color Decorator 
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m",
    }

    def wrapper(func):
        def inner(*args, **kwargs):
            print(colors.get(color, ""), end="")
            result = func(*args, **kwargs)
            print(colors["reset"], end="")
            return result

        return inner

    return wrapper



class FileHandler:
    def __init__(self, filepath):
        self._filepath = filepath

    
    @property
    def filepath(self):
        # Property Getter and Setter
        return self._filepath

    @filepath.setter
    def filepath(self, new_path):
        if os.path.exists(new_path):
            self._filepath = new_path
        else:
            raise FileNotFoundError("File does not exist.")

   
    def file_generator(self):
         #Generator to Read File Line by Line
        with open(self._filepath, "r") as f:
            for line in f:
                yield line.strip()

    
    def read_lines(self):
        #Read File and Store Lines Using List Comprehension
        return [line for line in self.file_generator()]

    
    def __str__(self):
        return f"FileHandler for: {self._filepath}"

   
    def __add__(self, other):
         #__add__ Method to Concatenate Two Files
        new_path = "concatenated.txt"
        with open(new_path, "w") as f:
            with open(self._filepath, "r") as f1:
                f.write(f1.read())
            with open(other.filepath, "r") as f2:
                f.write(f2.read())
        return FileHandler(new_path)

   
    @staticmethod
    def count_lines(filepath):
        with open(filepath, "r") as f:
            return sum(1 for _ in f)

    
    @classmethod
    def from_file(cls, path):
        #Class Method to Create Instance from a File
        return cls(path)



class AdvancedFileHandler(FileHandler):

   
    def __str__(self):
        return f"[Advanced] FileHandler for: {self._filepath}"

    
    def concat_files(self, *paths):
        # Method to Concatenate Multiple Files
        new_path = "multi_concat.txt"
        with open(new_path, "w") as out:
            for path in paths:
                with open(path, "r") as f:
                    out.write(f.read())
        return AdvancedFileHandler(new_path)





def dice_generator(seed=40, n=10):
    random.seed(seed)
    for _ in range(n):
        yield random.randint(1, 6)



@deco("blue")
def plot_dice(n=10):
    values = list(dice_generator(n=n))
    plt.hist(values, bins=range(1, 8), edgecolor="black", align="left")
    plt.title(f"Histogram of {n} Dice Rolls")
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.xticks(range(1, 7))
    plt.grid(True)
    plt.show()
