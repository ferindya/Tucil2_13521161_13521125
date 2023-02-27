import math
import random
import time
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Algoritma Brute Force untuk mencari pasangan titik terdekat
def findDistanceBruteForce(points):
    n = len(points)
    min_dist = float('inf')
    closest_pair = None
    
    for i in range(n):
        for j in range(i+1, n):
            d = findDistance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (points[i], points[j])
    
    return closest_pair, min_dist

# Algoritma Divide and Conquer untuk mencari pasangan titik terdekat
def findDistanceDivideConquer(points):
    n = len(points)
    if n <= 3:
        return findDistanceBruteForce(points)
    
    # Sort points berdasarkan koordinat X
    points = sorted(points, key=lambda x: x[0])
    
    # Divide points menjadi 2 bagian
    mid = n // 2
    left = points[:mid]
    right = points[mid:]
    
    # Mencari pasangan terdekat di setiap bagian secara rekursif
    left_pair, left_dist = findDistanceDivideConquer(left)
    right_pair, right_dist = findDistanceDivideConquer(right)
    
    # Mencari pasangan titik terdekat di kedua bagian
    if left_dist < right_dist:
        closest_pair = left_pair
        min_dist = left_dist
    else:
        closest_pair = right_pair
        min_dist = right_dist
    
    # Mencari pasangan titik terdekat yang melintasi garis tengah
    strip = []
    for point in points:
        if abs(point[0] - points[mid][0]) < min_dist:
            strip.append(point)
    strip = sorted(strip, key=lambda x: x[1])
    
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= min_dist:
                break
            d = findDistance(strip[i], strip[j])
            if d < min_dist:
                min_dist = d
                closest_pair = (strip[i], strip[j])
    
    return closest_pair, min_dist

# Fungsi untuk menghitung jarak antara 2 titik dalam ruang 3D
def findDistance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

# Generate secara random 10 titik dalam ruang 3D
num_points = int(input("Masukkan jumlah titik pada ruang 3D (n) : "))
points = [(random.uniform(-10, 10), random.uniform(-10, 10), random.uniform(-10, 10)) for i in range(num_points)]

# Mencari pasangan titik terdekat menggunakan algoritma Brute Force
start_time = time.time()
bf_pair, bf_dist = findDistanceBruteForce(points)
bf_time = (time.time() - start_time) * 100
bf_ops = num_points**2/2

# Mencari pasangan titik terdekat menggunakan algoritma Divide and Conquer
start_time = time.time()
dc_pair, dc_dist = findDistanceDivideConquer(points)
dc_time = (time.time() - start_time) * 100
dc_ops = num_points * math.log(num_points, 2)

# Mencetak pasangan titik terdekat beserta nilai jarak untuk algoritma brute force dan divide and conquer
print("---------------------[[ALGORITMA BRUTE FORCE]]---------------------")
print("Pasangan titik terdekat : ", bf_pair)
print("Nilai jarak : ", bf_dist)
print("Banyaknya operasi perhitungan rumus Euclidean : ", bf_ops)
print("Waktu Eksekusi : ", bf_time)

print("---------------------[[ALGORITMA DIVIDE AND CONQUER]]---------------------")
print("Pasangan titik terdekat : ", dc_pair)
print("Nilai jarak :", dc_dist)
print("Banyaknya operasi perhitungan rumus Euclidean : ", dc_ops)
print("Waktu Eksekusi : ", dc_time)

# Visualisasi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], s=10)
ax.scatter([dc_pair[0][0], dc_pair[1][0]], [dc_pair[0][1], dc_pair[1][1]], [dc_pair[0][2], dc_pair[1][2]], s=50, c='r')
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')
plt.show()