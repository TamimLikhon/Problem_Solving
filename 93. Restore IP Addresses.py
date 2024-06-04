def is_valid_ip(ip_str):
  try:
    return int(ip_str.split(".")[0]) <= 255 and all(0 <= int(part) <= 255 for part in ip_str.split("."))
  except ValueError:
    return False

s = "101023"
all_ip = []
for i in range(len(s) - 2):
  for j in range(i + 2, len(s)):
    for k in range(j + 2, len(s)):
      ip_str = s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:]
      if is_valid_ip(ip_str):
        all_ip.append(ip_str)

print(all_ip)
