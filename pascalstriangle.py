def generate_triangle(exponent, triangle=[]):
  for row in range(exponent):
    currentrow = []
    currentrow.append(1)
    if row == 0:
      pass
    elif row == 1:
      currentrow.append(1)
    else:
      for i in triangle[row-1]:
        val = triangle[row-1][i-1]+triangle[row-1][i]
        currentrow.append(val)
      currentrow.append(1)
    triangle.append(currentrow)
  return triangle
triangle = []
