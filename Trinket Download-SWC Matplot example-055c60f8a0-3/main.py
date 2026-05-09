import matplotlib.pyplot as plt
import numpy as np

# 1. 创建 3D 舞台
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# 2. 定义这 1 平米沙地的空间 (x, y 为表面, z 为深度)
x, y = np.meshgrid(np.linspace(0, 1, 10), np.linspace(0, 1, 10))

# 3. 模拟水分分布 (这部分你可以根据爸爸的实验数据改)
# 假设越深的地方水分越少
z = -0.5 * (x**2 + y**2) # 这里只是一个模拟曲线

# 4. 画出 3D 曲面图 (这就是你爸爸说的地制/沙质分布)
surf = ax.plot_surface(x, y, z, cmap='YlGnBu', edgecolor='none', alpha=0.8)

# 5. 重点：标注爸爸担心的“板结硬块”
# 我们可以手动加一个红色的点，代表监测到的硬块
ax.scatter([0.5], [0.5], [-0.3], color='red', s=100, label='Compaction Zone (Hard)')

# 设置坐标轴标签
ax.set_title("3D Sand Moisture & Hardness Model (1m²)")
ax.set_xlabel("Surface X (m)")
ax.set_ylabel("Surface Y (m)")
ax.set_zlabel("Depth Z (m)")
ax.legend()

plt.show()