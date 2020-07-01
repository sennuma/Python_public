url = "https://raw.githubusercontent.com/maskot1977/ipython_notebook/master/toydata/location.txt"
import urllib.request
import matplotlib.pyplot as plt
import math

urllib.request.urlretrieve(url, "location.txt")
col1, col2, col3 = [], [], []
for i, line in enumerate(open("location.txt")):
    if i == 0:
        continue
    c = line.split(",")
    col1.append(c[0])
    col2.append(float(c[1]))
    col3.append(float(c[2]))


def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


dist = []
for i, city1 in enumerate(zip(col1, col3, col2)):
    for j, city2 in enumerate(zip(col1, col3, col2)):
        if i >= j:
            continue
        dist.append(distance(city1[1], city1[2], city2[1], city2[2]))

# plt.figure(figsize=(10, 8))
# plt.scatter(col3, col2, alpha=0.5)
# plt.title("Prefectual capitals in Japan")
# plt.xlabel("Logitude")
# plt.ylabel("Latitude")
# plt.grid(True)
# for city, x, y in zip(col1, col3, col2):
#     plt.text(x, y, city, alpha=0.5, size=12)
# plt.show()

# "plot a chart about the distances btw JPC's"
# plt.hist(dist, bins=20)
# plt.title("Distance distribution between prefectual capitals")
# plt.xlabel("Distance")
# plt.show()

# "plot a chart with lines drawn btw JPC's"
# plt.figure(figsize=(12, 8))
# plt.title("Prefectual capitals in Japan")
# plt.xlabel("Longitude")
# plt.ylabel("Latitude")
# plt.grid(True)
# for city1, x1, y1 in zip(col1, col3, col2):
#     for city2, x2, y2 in zip(col1, col3, col2):
#         if city1 >= city2:
#             continue
#         plt.plot([x1, x2], [y1, y2], "k-", alpha=0.2)
# plt.scatter(col3, col2)
# for city, x, y in zip(col1, col3, col2):
#     plt.text(x, y, city, alpha=0.3, size=12)
# plt.show()
