def recover_original_array(pref):
  n = len(pref)
  original_arr = [0] * n
  original_arr[0] = pref[0]
  for i in range(1, n):
    original_arr[i] = pref[i] - pref[i-1]
  return original_arr

pref = [5,2,0,3,1]
original_arr = recover_original_array(pref)
print(original_arr)
