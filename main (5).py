def                                 linearsearchproduct(productlist,targetproduct):
  indices=[]

  for index,product in              enumerate(productlist):
    if product == targetproduct:
      indices.append(index)

  return indices



product=["shoes","boot","loafer","shoes","sandel","shoes"]
target = "shoes"
target = 'apple'
result=linearsearchproduct(product,target)
print(result)
      
    
  