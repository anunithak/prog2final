import os
import random
import matplotlib.pyplot as plt

# Step 2: ANSI Color Decorator (for colorizing output)
def deco(color: str):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    def wrapper(func):
        def inner(*args, **kwargs):
            print(colors.get(color, ""), end="")
            result = func(*args, **kwargs)
            print(colors["reset"], end="")
            return result
        return inner
    return wrapper

# Step 3: Base Class
class FileHandler:
    def __init__(self, filepath):
        self._filepath = filepath

    # Step 4: Property Getter and Setter
    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, new_path):
        if os.path.exists(new_path):
            self._filepath = new_path
        else:
            raise FileNotFoundError("File does not exist.")

    # Step 5: Generator to Read File Line by Line
    def file_generator(self):
        with open(self._filepath, 'r') as f:
            for line in f:
                yield line.strip()

    # Step 6: Read File and Store Lines Using List Comprehension
    def read_lines(self):
        return [line for line in self.file_generator()]

    # Step 7: __str__ Method
    def __str__(self):
        return f"FileHandler for: {self._filepath}"

    # Step 8: __add__ Method to Concatenate Two Files
    def __add__(self, other):
        new_path = "concatenated.txt"
        with open(new_path, 'w') as f:
            with open(self._filepath, 'r') as f1:
                f.write(f1.read())
            with open(other.filepath, 'r') as f2:
                f.write(f2.read())
        return FileHandler(new_path)

    # Step 9: Static Method
    @staticmethod
    def count_lines(filepath):
        with open(filepath, 'r') as f:
            return sum(1 for _ in f)

    # Step 10: Class Method to Create Instance from a File
    @classmethod
    def from_file(cls, path):
        return cls(path)

# Step 11: Inherited Class with Extra Functionality
class AdvancedFileHandler(FileHandler):

    # Override __str__
    def __str__(self):
        return f"[Advanced] FileHandler for: {self._filepath}"

    # Method to Concatenate Multiple Files
    def concat_files(self, *paths):
        new_path = "multi_concat.txt"
        with open(new_path, 'w') as out:
            for path in paths:
                with open(path, 'r') as f:
                    out.write(f.read())
        return AdvancedFileHandler(new_path)

# Step 12: Random Generator Function

def dice_generator(seed=40, n=10):
    random.seed(seed)
    for _ in range(n):
        yield random.randint(1, 6)

# Step 13: Decorated Plotting Function
@deco("blue")
def plot_dice(n=10):
    values = list(dice_generator(n=n))
    plt.hist(values, bins=range(1, 8), edgecolor='black', align='left')
    plt.title(f"Histogram of {n} Dice Rolls")
    plt.xlabel("Dice Face")
    plt.ylabel("Frequency")
    plt.xticks(range(1, 7))
    plt.grid(True)
    plt.show()

# Example usage (commented out for testing):
# handler1 = FileHandler("file1.txt")
# handler2 = FileHandler("file2.txt")
# combined = handler1 + handler2
# print(combined)

# adv_handler = AdvancedFileHandler("file1.txt")
# adv_combined = adv_handler.concat_files("file1.txt", "file2.txt", "file3.txt")
# print(adv_combined)

# plot_dice(n=100)

if __name__ == "__main__":
    rolls = list(dice_generator(seed=40, n=5))
    print("Generated rolls:", rolls)
