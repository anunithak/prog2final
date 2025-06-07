from file_handler import dice_generator

rolls = list(dice_generator(seed=40, n=5))
print("Generated rolls:", rolls)
