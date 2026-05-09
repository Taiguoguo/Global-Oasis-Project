# Global-Oasis-Project
A Python-powered automated soil moisture management system for desert restoration. Validating in the UAE with a vision to scale to China and globally. Features self-healing logic and quad-sensor monitoring.

# Planned Visuals (计划展示):
- 阿联酋实地部署图 (Field deployment in UAE)
- 4路传感器电路架构图 (Schematic of the 4-sensor matrix)
- 自动修复逻辑流程图 (Flowchart of self-healing logic)

# Hardware Rationales (硬件选型依据)
# Corrosion Resistance: The capacitive design was specifically chosen to address the severe corrosion issues common in saline desert soils, ensuring long-term sensor stability.
# Low Power Consumption: The ESP32’s advanced low-power (Deep Sleep) modes are ideal for the long-term, autonomous monitoring required in remote oasis locations.

# Research & SimulationBefore developing the core engine, in-depth modeling and analysis were conducted using Python. 
These research tools are located in the /tools directory:Field Layout Design (tools/visualize_layout.py)Description: Simulates the spatial deployment of sensors and irrigation lines across a 100m² experimental plot. It ensures optimal coverage using a 5-sensor matrix (4 regional detectors + 1 central reference).365-Day Growth Simulation (tools/growth_simulation.py)Description: Compares four technical combinations through mathematical modeling. The simulation confirms that the synergy between AI-driven self-healing irrigation and Nanoclay yields the highest growth efficiency, achieving approximately 20x greater stability compared to raw desert conditions.
