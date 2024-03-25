items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"
key_index = {"type": 0, "color": 1, "name": 2}  # Mapping of ruleKey to index
count = 0      
for item in items:
    if item[key_index[ruleKey]] == ruleValue:
        count += 1

print(count)


