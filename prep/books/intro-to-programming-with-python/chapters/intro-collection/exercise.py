range(7) # 0 - 6 inclusive
range(1, 6) # 1 - 5 inclusive
range(3, 15, 4) # 3 7 11
range(3, 8, -1) # []
range(8, 3, -1) # 8 7 6 5 4 

# Alice	USA
# Francois	Canada
# Inti	Peru
# Monika	Germany
# Sanyu	Uganda
# Yoshitaka	Japan

users = {
  "Alice": "USA",
  "Francois": "Canada",
  "Inti": "Peru",
  "Monika": "Germany",
  "Sanyu": "Uganda",
  "Yoshitaka": "Japan"
}

print(users["Alice"])