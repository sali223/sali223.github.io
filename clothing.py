
clothing_items = [
    "jeans", "t-shirt", "socks", "t-shirt", "dress", "hat", "sweater", "", "pants", "scarf", "jeans"
]

def clean_clothing_list(clothing_list):
    cleaned_list = list(set(clothing_list))
    
    cleaned_list = [item for item in cleaned_list if item.strip() != ""]
  
    cleaned_list = [item for item in cleaned_list if len(item) > 2]
    
    
    cleaned_list.sort()

    return cleaned_list


cleaned_clothing_items = clean_clothing_list(clothing_items)


print("Cleaned Clothing List:")
for item in cleaned_clothing_items:
    print(item)
