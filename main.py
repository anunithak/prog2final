from file_handler import FileHandler, AdvancedFileHandler, plot_dice


f1 = FileHandler("file1.txt")
f2 = FileHandler("file2.txt")

print("Reading file1:", f1.read_lines())
print("Reading file2:", f2.read_lines())


f3 = f1 + f2
print("Combined file content:", f3.read_lines())


adv = AdvancedFileHandler("file1.txt")
multi = adv.concat_files("file1.txt", "file2.txt", "file3.txt")
print("Multi-concat content:", multi.read_lines())


plot_dice(n=100)
plot_dice(n=10)
plot_dice(n=1000)
plot_dice(n=10000)
