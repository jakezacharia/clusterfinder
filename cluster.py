import math

# define circle class so we can pass a list of circles to the function
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def __str__(self):
        return f"\n(●)circle at ({self.x}, {self.y}) with radius {self.r}"

def distance_check(currentCircle: Circle, circles: list, visited: set):
    # add the current circle to visited list
    visited.add(currentCircle)
    # for all items in circles list, and if not in visited set, find distance using euclidean equation w/ current circle + item c in circles
    for c in circles:
        if c not in visited:
            dist = math.sqrt((c.x - currentCircle.x)**2 + (c.y - currentCircle.y)**2)
            if dist < currentCircle.r + c.r:
                # check if one circle is within another
                if dist + min(currentCircle.r, c.r) < max(currentCircle.r, c.r):
                    continue
                # recursively call function
                distance_check(c, circles, visited)

def cluster_detect(circles):
    # 1 or 0 circles will never equal a cluster
    if len(circles) < 2:
        return False
    # declare visited set, initalize empty
    visited = set()
    # call distance check with base values
    distance_check(circles[0], circles, visited)
    # use length of visited to check against original length of circles list
    if len(visited) == len(circles):
        print("TRUE - is a cluster\n")
        return True
    print("FALSE - not a cluster\n")
    return False

def main():
  # test case 1
  case1 = [Circle(1,3,0.7), Circle(2,3,0.4), Circle(3,3,0.9)]
  print("\nTEST CASE 1")
  print(str(case1[0]), str(case1[1]), str(case1[2]))
  cluster_detect(case1)

  # test case 2
  case2 = [Circle(1.5,1.5,1.3), Circle(4,4,0.7)]
  print("TEST CASE 2")
  print(str(case2[0]), str(case2[1]))
  cluster_detect(case2)

  # test case 3
  case3 = [Circle(0.5,0.5,0.5), Circle(1.5,1.5,1.1), Circle(0.7,0.7,0.4), Circle(4,4,0.7)]
  print("TEST CASE 3")
  print(str(case3[0]), str(case3[1]), str(case3[2]), str(case3[3]))
  cluster_detect(case3)

  # test case 4 (circle within a circle, should return false)
  case4 = [Circle(2,2,5), Circle(2,2,3)]
  print("TEST CASE 4 - Circle within a circle : expected result FALSE")
  print(str(case4[0]), str(case4[1]))
  cluster_detect(case4)

  # test case 5 (out of order version)
  case5 = [Circle(3,1,4), Circle(2,4,0.9), Circle(2,1.5,5)]
  print("TEST CASE 5 - Circles out of sequence, still connected : expected result TRUE")
  print(str(case5[0]), str(case5[1]), str(case5[2]))
  cluster_detect(case5)

if __name__ == "__main__":
  main()