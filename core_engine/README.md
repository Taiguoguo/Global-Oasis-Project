# Core Engine
This is the "brain" of the Global Oasis Project, primarily responsible for logical computation and system self-healing.

### Core Functions:

1. **Data Fusion**: Integrates readings from 4 ESP32 sensors, using algorithms to remove noise data caused by the high temperatures in the desert.

2. **Decision Making**: Controls dam/irrigation switching based on humidity gradients.

3. **Long-term Self-healing**:

- Automatically detects and disables faulty sensors.

- Automatically resets logic deadlocks.

- Automatically calibrates sensor drift.

### File Descriptions:

- `main.py`: Main system entry point.

- `self_healing.py`: Long-term repair logic.

- `processor.py`: 4-way data processing algorithms.
