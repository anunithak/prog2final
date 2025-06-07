from file_handler import FileHandler, AdvancedFileHandler, plot_dice

# Test FileHandler
f1 = FileHandler("file1.txt")
f2 = FileHandler("file2.txt")

print("Reading file1:", f1.read_lines())
print("Reading file2:", f2.read_lines())

# Test __add__
f3 = f1 + f2
print("Combined file content:", f3.read_lines())

# Test AdvancedFileHandler
adv = AdvancedFileHandler("file1.txt")
multi = adv.concat_files("file1.txt", "file2.txt", "file3.txt")
print("Multi-concat content:", multi.read_lines())

# Test plot
plot_dice(n=100)

if __name__ == "__main__":
    rolls = list(dice_generator(seed=40, n=5))
    print("Generated rolls:", rolls)
