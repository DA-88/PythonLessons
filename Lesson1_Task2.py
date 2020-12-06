t = int(input("Seconds: "))
print("Result: %02d:%02d:%02d" % (t // 3600, (t % 3600) // 60, (t % 3600) % 60))
