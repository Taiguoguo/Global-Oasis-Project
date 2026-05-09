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
