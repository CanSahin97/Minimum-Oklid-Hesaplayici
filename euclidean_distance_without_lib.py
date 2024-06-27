def euclideanDistance(point1, point2):
    return ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**(1/2)

# Noktaların tanımlanması
points = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafenin bulunması
min_distance = distances[0]
for distance in distances[1:]:
    if distance < min_distance:
        min_distance = distance

print("Noktalar:", points)
print("Hesaplanan mesafeler:", distances)
print("Minimum mesafe:", min_distance)
