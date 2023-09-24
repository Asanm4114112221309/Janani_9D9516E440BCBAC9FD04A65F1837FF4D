def linearSearchProduct(productList, targetProduct):
  indices =[]

  for index, Product in enumerate(productList):
    if Product == targetProduct:
      indices.append(index)

  return indices


Products = ["shoes","boot","loafer","shoes","sandal","shoes"]
target = "shoes"
target2 = 'apple'
result = linearSearchProduct(Products, target)
print(result)