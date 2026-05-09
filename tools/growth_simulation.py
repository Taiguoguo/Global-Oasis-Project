import matplotlib.pyplot as plt
import numpy as np

# 1. 模拟 365 天的时间线
days = np.arange(0, 365)

# 2. 定义四种环境的生长函数 (生长高度模型)
# 板块1：最优环境 (指数增长后趋于稳定)
growth_ideal = 100 * (1 - np.exp(-0.02 * days)) 
# 板块2：保水但供水不规律 (生长减半)
growth_nanoclay_only = 50 * (1 - np.exp(-0.015 * days))
# 板块3：保水差但精准供水 (生长不稳)
growth_smart_only = 30 * (1 - np.exp(-0.01 * days))
# 板块4：原始沙漠 (极低生长或中途干枯)
growth_desert = 5 * (1 - np.exp(-0.005 * days))

# 3. 创建 2x2 的展示画布
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('100m² Oasis Project: 365-Day Growth Comparison', fontsize=16)

# 板块1：左上
axs[0, 0].plot(days, growth_ideal, color='green', linewidth=2)
axs[0, 0].set_title("Plot A: Nanoclay + AI (Success)")
axs[0, 0].set_ylabel("Growth Height (cm)")
axs[0, 0].fill_between(days, growth_ideal, color='green', alpha=0.1)

# 板块2：右上
axs[0, 1].plot(days, growth_nanoclay_only, color='blue', linewidth=2)
axs[0, 1].set_title("Plot B: Nanoclay Only")

# 板块3：左下
axs[1, 0].plot(days, growth_smart_only, color='orange', linewidth=2)
axs[1, 0].set_title("Plot C: Smart Irrigation Only")
axs[1, 0].set_xlabel("Time (Days)")
axs[1, 0].set_ylabel("Growth Height (cm)")

# 板块4：右下
axs[1, 1].plot(days, growth_desert, color='red', linewidth=2)
axs[1, 1].set_title("Plot D: Raw Desert (Control)")
axs[1, 1].set_xlabel("Time (Days)")

# 统一调整网格和布局
for ax in axs.flat:
    ax.set_ylim(0, 110)
    ax.grid(True, linestyle=':', alpha=0.6)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
