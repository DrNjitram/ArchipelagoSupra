region_list = {}

with open("Supraland Access Sheet - Regions and Connections.csv") as f:
    raw_data_regions = f.readlines()

for line in raw_data_regions:
    print(line.strip().split(","))