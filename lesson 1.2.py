s = int(input("введите время в секундах: "))
hours = str(s//3600)
minutes = str((s%3600)//60)
seconds = str((s%3600)%60)
print(f"{hours}:{minutes}:{seconds}")