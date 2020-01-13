import copy

def sort(input_list):
  output_list = copy.deepcopy(input_list)
  a0 = 0                # first item id
  d0 = len(output_list) # number of items
  for n in range(d0, 1, -1):
    for i in range(0, n - 1):
      if output_list[i] > output_list[i + 1]:
        tmp = output_list[i]
        output_list[i] = output_list[i + 1]
        output_list[i + 1] = tmp

  return output_list
