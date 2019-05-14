def sort(input_list):
  a0 = 0                # first item id
  d0 = len(input_list)  # number of items
  for n in range(d0, 1, -1):
    for i in range(0, n - 1):
      if input_list[i] > input_list[i + 1]:
        tmp = input_list[i]
        input_list[i] = input_list[i + 1]
        input_list[i + 1] = tmp

  return input_list
