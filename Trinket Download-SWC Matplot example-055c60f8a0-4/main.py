import matplotlib.pyplot as plt

# 1. 设置画布大小，代表 10m x 10m 的土地
fig, ax = plt.subplots(figsize=(8, 8))

# 2. 绘制 100 平米的边界
outer_boundary = plt.Rectangle((0, 0), 10, 10, color='wheat', alpha=0.3, label='100m² Desert Plot')
ax.add_patch(outer_boundary)

# 3. 标注传感器位置 (假设每 2.5 米放一个，像网格一样分布)
sensors_x = [2.5, 2.5, 7.5, 7.5, 5.0]
sensors_y = [2.5, 7.5, 2.5, 7.5, 5.0]
ax.scatter(sensors_x, sensors_y, color='red', s=100, marker='X', label='Sensors (Moisture)')

# 4. 绘制主水管 (从左侧水箱出发，横穿中间)
ax.plot([0, 10], [5, 5], color='blue', linewidth=3, linestyle='--', label='Main Irrigation Line')

# 5. 标注水箱和水泵位置 (左下角)
ax.scatter([0], [5], color='darkblue', s=300, marker='s', label='Water Tank & Pump')

# 6. 装饰图片
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)
ax.set_aspect('equal')
ax.grid(True, linestyle=':', alpha=0.6)

plt.title("100m² Oasis Project Layout (Year 10 Research)", fontsize=14)
plt.xlabel("Width (meters)")
plt.ylabel("Length (meters)")
plt.legend(loc='upper right', fontsize='small')

# 标注一下坐标
for i, (x, y) in enumerate(zip(sensors_x, sensors_y)):
    ax.text(x+0.2, y+0.2, f'S{i+1}', fontsize=9)

plt.show()
