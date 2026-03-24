import numpy as np

print("=== MATRICES ROTACIONALES ===")

# 🔹 EJERCICIO 1
angulo = 30
theta = np.radians(angulo)

print("\n=== EJERCICIO 1 ===")
print("Ángulo:", angulo)

print("\nPaso 1: Convertir a radianes")
print("theta =", theta)

print("\nPaso 2: Aplicar fórmula")
print("cos(theta) =", np.cos(theta))
print("sin(theta) =", np.sin(theta))

R1 = np.array([[np.cos(theta), -np.sin(theta)],
               [np.sin(theta), np.cos(theta)]])

print("\nResultado:")
print(R1)


# 🔹 EJERCICIO 2
angulo = 45
theta = np.radians(angulo)

print("\n=== EJERCICIO 2 ===")
print("Ángulo:", angulo)

print("\nPaso 1: theta =", theta)
print("cos =", np.cos(theta))
print("sin =", np.sin(theta))

R2 = np.array([[np.cos(theta), -np.sin(theta)],
               [np.sin(theta), np.cos(theta)]])

print("\nResultado:")
print(R2)


# 🔹 EJERCICIO 3
angulo = 90
theta = np.radians(angulo)

print("\n=== EJERCICIO 3 ===")
print("Ángulo:", angulo)

print("\nPaso 1: theta =", theta)
print("cos =", np.cos(theta))
print("sin =", np.sin(theta))

R3 = np.array([[np.cos(theta), -np.sin(theta)],
               [np.sin(theta), np.cos(theta)]])

print("\nResultado:")
print(R3)
