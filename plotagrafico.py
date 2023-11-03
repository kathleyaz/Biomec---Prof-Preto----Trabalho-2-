import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Seus pontos
x = [0.0040106999, 0.0013577836, 0.7795888759, 0.7783916484, -0.0015136248, -0.0009480126, 0.7801485176, 0.7823768551, 0.0002223853, -0.0032767154, 0.7859380907, 0.7797204682]
y = [0.0015723430, 1.4664854805, 1.4656860934, -0.0011725950, -0.0004110288, 1.4654112552, 1.4676494054, -0.0016201118, 0.0008604155, 1.4643818642, 1.4664276940, 0.0007359357]
z = [-0.0030787174, -0.0002735983, 0.0018643970, 0.0016910910, 0.4560298087, 0.4498028609, 0.4457739916, 0.4491580505, 0.9077355917, 0.9040679833, 0.9016854725, 0.9015623184]

# Cria uma figura 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plota os pontos
ax.scatter(x, y, z, c='r', marker='o')

# Rótulos dos eixos
ax.set_xlabel('Eixo X')
ax.set_ylabel('Eixo Y')
ax.set_zlabel('Eixo Z')

# Exibe o gráfico
plt.show()
