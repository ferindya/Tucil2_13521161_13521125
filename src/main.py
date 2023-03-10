import math
import random
from time import time
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Algoritma Brute Force untuk mencari pasangan titik terdekat
def findDistanceBruteForce(points):
    n = len(points)
    minDistance = float('inf')
    closestPair = None
    
    for i in range(n):
        for j in range(i+1, n):
            d = findDistance(points[i], points[j])
            if d < minDistance:
                minDistance = d
                closestPair = (points[i], points[j])
    
    return closestPair, minDistance

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
    leftPair, leftDistance = findDistanceDivideConquer(left)
    rightPair, rightDistance = findDistanceDivideConquer(right)
    
    # Mencari pasangan titik terdekat di kedua bagian
    if leftDistance < rightDistance:
        closestPair = leftPair
        minDistance = leftDistance
    else:
        closestPair = rightPair
        minDistance = rightDistance
    
    # Mencari pasangan titik terdekat yang melintasi garis tengah
    strip = []
    for point in points:
        if abs(point[0] - points[mid][0]) < minDistance:
            strip.append(point)
    strip = sorted(strip, key=lambda x: x[1])
    
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] >= minDistance:
                break
            d = findDistance(strip[i], strip[j])
            if d < minDistance:
                minDistance = d
                closestPair = (strip[i], strip[j])
    
    return closestPair, minDistance

# Fungsi untuk menghitung jarak antara 2 titik dalam ruang 3D
def findDistance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

# ASCII ART
print("       \:.             .:/                                                       ")
print("        \``._________.''/                                                        ")
print("         \             /                                                         ")  
print(" .--.--, / .':.   .':. \                                                         ")
print("/__:  /  | '::' . '::' |        === WELCOME TO CLOSEST PAIR OF POINTS PROGRAM ===")
print("   / /   |`.   ._.   .'|                       BY 13521161 & 13521125            ")
print("  / /    |.'         '.|                                                         ")
print(" /___-_-,|.\  \   /  /.|                                                         ")
print("      // |''\.;   ;,/ '|                                                         ")
print("      `==|:=         =:|                                                         ")
print("         `.          .'                                                          ")
print("           :-._____.-:                                                           ")
print("          `''       `''                                                          ")
print("                                                                                 ")

# Generate secara random 100 titik dalam ruang 3D
num_points = int(input("Masukkan jumlah titik pada ruang 3D (n) : "))
points = [(random.uniform(-100, 100), random.uniform(-100, 100), random.uniform(-100, 100)) for i in range(num_points)]

# Mencari pasangan titik terdekat menggunakan algoritma Brute Force
startTime = time()
bruteForcePair, bruteForceDistance = findDistanceBruteForce(points)
bruteForceTime = (time() - startTime) 
bruteForceOp = num_points**2/2

# Mencari pasangan titik terdekat menggunakan algoritma Divide and Conquer
startTime = time()
divideConquerPair, divideConquerDistance = findDistanceDivideConquer(points)
divideConquerTime = (time() - startTime)
divideConquerOp = num_points * math.log(num_points, 2)

# Mencetak pasangan titik terdekat beserta nilai jarak untuk algoritma brute force dan divide and conquer
print("-----------------------------------------------------------------[[ALGORITMA BRUTE FORCE]]----------------------------------------------------------------")
print("Pasangan titik terdekat : ", bruteForcePair)
print("Nilai jarak : ", bruteForceDistance)
print("Banyaknya operasi perhitungan rumus Euclidean : ", bruteForceOp)
print("Waktu Eksekusi : ", bruteForceTime, "detik")
print("                                                                                                                                                          ")
print("-------------------------------------------------------------[[ALGORITMA DIVIDE AND CONQUER]]-------------------------------------------------------------")
print("Pasangan titik terdekat : ", divideConquerPair)
print("Nilai jarak :", divideConquerDistance)
print("Banyaknya operasi perhitungan rumus Euclidean : ", divideConquerOp)
print("Waktu Eksekusi : ", divideConquerTime, "detik")

# Visualisasi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter([p[0] for p in points], [p[1] for p in points], [p[2] for p in points], s=10)
ax.scatter([divideConquerPair[0][0], divideConquerPair[1][0]], [divideConquerPair[0][1], divideConquerPair[1][1]], [divideConquerPair[0][2], divideConquerPair[1][2]], s=50, c='r')
ax.set_xlabel('Sumbu X')
ax.set_ylabel('Sumbu Y')
ax.set_zlabel('Sumbu Z')
plt.show()