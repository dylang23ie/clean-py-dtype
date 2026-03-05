prices = [100, 123.45, "154", 152]

prices.append(100)
print(prices, type(prices))

for item in prices:
    print(item, type(item))

print("-------------")

print(prices[0])
print(prices[3])
print(prices[-1])

print(prices[2:-1])