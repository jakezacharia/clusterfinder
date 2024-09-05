import math

# ===================================
#notes
# how can we use a set of circles?
# can create a circle class, then use a loop when checking connection n times, where n is the number of circles
# can calc distance from circle 1 -> circle 2 ; if false, end here. if true, then calculate circle 2 -> circle 3, etc.
# if all distances are true, then the circles are connected
# if one distance is false, then the circles are not connected and you can terminate loop here to save compute time
# ===================================

# define circle class so we can pass a list of circles to the function
class Circle:
  def __init__(self, x, y, r):
    self.x = x
    self.y = y
    self.r = r

  def __str__(self):
    return f"\n>circle at ({self.x}, {self.y}) with radius {self.r}"

# calculate distance between two circles using euclidean distance formula
def distance(circle1, circle2):
  # calculate distance between two circles
  dist = math.sqrt((circle2.x - circle1.x)**2 + (circle2.y - circle1.y)**2)
  print("distance between circles: ", dist)
  print("sum of radii: ", circle1.r + circle2.r)
  # we only return dist if the sum of the radii is greater/equal to than the distance between the two circles aka they are connected
  return dist <= circle1.r + circle2.r

# passing a list of circles to the function
def clusterDetect(circles):
  # loop through the list of circles
  for i in range(len(circles) - 1):
    # if the distance between two circles is false, then the circles are not connected
    if not distance(circles[i], circles[i+1]):
      # we can return false here to save compute time and declare that the provided test case is not a cluster
      print("not a cluster\n")
      return False
  # loop continues until the end of the list of circles, if all distances are true, then the circles are connected and the test case is declared a cluster
  print("is a cluster\n")
  return True

def main():

  # test case 1
  case1 = [Circle(1,3,0.7), Circle(2,3,0.4), Circle(3,3,0.9)]
  print("TEST CASE 1\n")
  print(str(case1[0]), str(case1[1]), str(case1[2]))
  clusterDetect(case1)

  # test case 2
  case2 = [Circle(1.5,1.5,1.3), Circle(4,4,0.7)]
  print("TEST CASE 2")
  print(str(case2[0]), str(case2[1]))
  clusterDetect(case2)


if __name__ == "__main__":
  main()