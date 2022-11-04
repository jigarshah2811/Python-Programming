"""
Indexes = [False, False, False, False]
["SET", index] --> sets that index to True
["GET", index] --> gets this index if index is True, OR gets "nearest" index (> this index) that is True 

"""
import collections

nearest = collections.defaultdict(int)

def set(index):
  
  
  # Mark all prior indexes based on this index
  for i in range(index, 0, -1):
    if i not in nearest:        # If the previous indexes doesn't have any nearest set, set this index as nearest
        nearest[i] = index
    elif nearest[i] > index:    # If the previous indexes have far nearest, set this index as nearest
      nearest[i] = index
    else:                       # If the previous indexes already have nearest index better (nearest) then this, nothing
        pass
  print(f"After set[{index}]: {nearest}")

def get(index):
  return nearest.get(index, -1)

inputs = [["GET", 2], ["SET", 2], ["GET", 1], ["SET", 1], ["GET", 1]]

def main():
    print("starting")
    res = []

    for input in inputs:
        match input[0]:
            case "GET":
                output = get(input[1])
                res.append(output)

            case "SET":
                output = set(input[1])
                res.append(output)
    
    print(res)

if __name__ == "__main__":
    main()