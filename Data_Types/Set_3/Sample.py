lounges = { 
    "Lounge_A": {"WiFi", "Comfortable Seating", "Free Drinks", "Private Rooms"}, 
    "Lounge_B": {"WiFi", "Comfortable Seating", "Luxury Showers", "Free Drinks"}, 
    "Lounge_C": {"Private Rooms", "Luxury Showers", "Free Drinks", "Spa Services"}, 
}

common = set.intersection(*lounges.values())
all_amenities = set.union(*lounges.values())
unique = {amenity for amenity in all_amenities if sum(amenity in amenities for amenities in lounges.values()) == 1}

print(common, unique)