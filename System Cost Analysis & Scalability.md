# 📋 Bill of Materials (BOM) | 物料清单

本项目旨在实现低成本、高效率的荒漠化治理。
*This list covers the core hardware costs for the 100m² modular experimental unit.*


| Component (组件) | Specifications (规格) | Qty | Unit Price | Total | Role (作用) |
| :--- | :--- | :---: | :--- | :--- | :--- |
| **ESP32 MCU** | ESP-WROOM-32 (Dual Core) | 1 | ~35 AED | 35 AED | 核心控制与 WiFi 传输 |
| **Moisture Sensor** | Capacitive Soil Sensor v1.2 | 4 | ~15 AED | 60 AED | 4 区域实时湿度采集 |
| **Solar Kit** | 5W Solar Panel + Battery | 1 | ~110 AED | 110 AED | 能源独立，支持深睡眠 |
| **Water Pump** | 12V DC Brushless | 1 | ~45 AED | 45 AED | 执行灌溉决策 |
| **Misc** | Wires, Enclosure, PVC | 1 | ~100 AED | 100 AED | 环境保护与物理连接 |
| **TOTAL** | | | | **~350 AED** | **约合 $95 USD** |

---

### 💡 经济性分析 (Economic Rationales)

*   **Low Initial Investment (低初期投入)**: 
    单单元成本仅需约 **350 AED**。对于阿联酋的大规模荒漠化治理，这种低成本方案极具可扩展性。
    *Initial cost is only ~350 AED per unit, making it highly scalable.*

*   **Autonomous Maintenance (自主维护)**: 
    通过 **Python 自愈逻辑**，预计可减少约 **60% 的现场维护次数**，大幅降低长期运营的人力成本。
    *Self-healing logic reduces O&M costs by ~60%.*

*   **Efficiency Gains (效率提升)**: 
    结合纳米粘土 (Nanoclay)，目标是减少 **40% 的灌溉用水**。
    *Targeting a 40% reduction in water usage.*

    # 项目核心优势 (Project Core Advantage):
    - 通过选用低成本、工业级的通用组件，本方案实现了极高的经济可行性，极大地降低了荒漠化治理的准入门槛。By adopting low-cost, industrial-grade general-purpose components, this solution achieves high economic feasibility, significantly lowering the barriers to entry for desert restoration.
    - 成本控制 (Cost Control):由于采用了 ESP32 这种集成 WiFi 和蓝牙的高性能微控制器，单个监测模块的硬件成本得以控制在 $80 - $100 之间。By utilizing the ESP32, a high-performance microcontroller with integrated WiFi and Bluetooth, the hardware cost per monitoring module is maintained between $80 and $100.
    - 大规模部署 (Large-scale Deployment):这种高性价比的架构配合 Python 自动化控制逻辑，使得系统非常适合在全球干旱地区进行成千上万个单元的大规模部署。This cost-effective architecture, combined with Python automation logic, makes the system ideal for large-scale deployment across thousands of units in arid regions worldwide.
