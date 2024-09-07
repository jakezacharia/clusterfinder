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
            if dist <= currentCircle.r + c.r:
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

  test_cases = [
  [Circle(1,3,0.7), Circle(2,3,0.4), Circle(3,3,0.9)],
  [Circle(1.5,1.5,1.3), Circle(4,4,0.7)],
  [Circle(0.5,0.5,0.5), Circle(1.5,1.5,1.1), Circle(0.7,0.7,0.4), Circle(4,4,0.7)],
  [Circle(2,2,5), Circle(2,2,3)],
  [Circle(3,1,4), Circle(2,4,0.9), Circle(2,1.5,5)],
  [Circle(1,1,1), Circle(3,1,1), Circle(5,1,1), Circle(7,1,1)],
  [Circle(1,1,1), Circle(0.5,1,0.5)]
  ]


  for i, case in enumerate(test_cases, start=1):
      print(f"TEST CASE {i}")
      for circle in case:
          print(str(circle))
      cluster_detect(case)


if __name__ == "__main__":
  main()