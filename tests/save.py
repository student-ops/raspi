path = "../data/gateway_data.txt"
    

numbers =[1,1.0,1,1]

with open(path, mode='w') as f:
          for s in range(len(numbers)):
                    print("count "+str(s))
                    f.write(str(numbers[s]))
          f.write("\n")