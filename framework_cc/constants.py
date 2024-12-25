"""Constants for Framework Control Center."""

from pathlib import Path
from typing import Dict, Any

# Directories
LIBS_DIR = Path("libs")
CONFIGS_DIR = Path("configs")
LOGS_DIR = Path("logs")
ASSETS_DIR = Path("assets")

# Files
RYZENADJ_EXECUTABLE = LIBS_DIR / "ryzenadj.exe"
HARDWARE_DLL_PATH = LIBS_DIR / "LibreHardwareMonitorLib.dll"
PROFILES_CONFIG = CONFIGS_DIR / "profiles.json"
SETTINGS_CONFIG = CONFIGS_DIR / "settings.json"

# URLs
RYZENADJ_DOWNLOAD_URL = "https://github.com/FlyGoat/RyzenAdj/releases/download/v0.13.0/ryzenadj-win64.zip"
LHM_DOWNLOAD_URL = "https://github.com/LibreHardwareMonitor/LibreHardwareMonitor/releases/download/v0.9.4/LibreHardwareMonitor-net472.zip"

# Hardware monitoring settings
SENSOR_IDS = {
    'cpu_temp': ('Cpu', 'Temperature', 'Core (Tctl/Tdie)'),  # Capteur de température CPU
    'cpu_load': ('Cpu', 'Load', 'CPU Total'),  # Charge CPU totale
    'ram_usage': ('Memory', 'Load', 'Memory'),  # Utilisation de la RAM
    'igpu_temp': ('GpuAmd', 'Temperature', 'GPU VR SoC'),  # Température iGPU (780M)
    'igpu_load': ('GpuAmd', 'Load', 'GPU Core'),  # Charge iGPU (780M)
    'dgpu_temp': ('GpuAmd', 'Temperature', 'GPU Core'),  # Température dGPU (7700S)
    'dgpu_load': ('GpuAmd', 'Load', 'GPU Core')  # Charge dGPU (7700S)
}

# RyzenAdj configuration
RYZENADJ_PARAMS = [
    ("stapm-limit", "stapm_limit"),
    ("fast-limit", "fast_limit"),
    ("slow-limit", "slow_limit"),
    ("stapm-time", "stapm_time"),
    ("slow-time", "slow_time"),
    ("tctl-temp", "tctl_temp"),
    ("vrmmax-current", "vrmmax_current"),
    ("vrmgfx-current", "vrmgfx_current")
]

# Required DLLs
REQUIRED_DLLS = [
    'libryzenadj.dll',
    'WinRing0x64.dll',
    'WinRing0x64.sys',
    'inpoutx64.dll'
]

# Cache configuration
METRICS_CACHE_TTL = 1.0  # seconds
PROFILE_CACHE_TTL = 300  # 5 minutes

# UI Colors
COLORS = {
    "primary": "#FF7043",
    "hover": "#F4511E",
    "background": "#262626",
    "text": "#FFFFFF"
}

# Supported laptop models
SUPPORTED_MODELS: Dict[str, Dict[str, Any]] = {
    "13_AMD": {
        "name": "13_AMD",
        "display_name": "Framework 13 AMD",
        "processors": ["AMD Ryzen 7 7840U"],
        "tdp": {
            "min": 15,
            "max": 28
        },
        "has_dgpu": False,
        "max_refresh_rate": 60
    },
    "13_INTEL": {
        "name": "13_INTEL",
        "display_name": "Framework 13 Intel",
        "processors": ["Intel Core i7-1370P", "Intel Core i5-1340P"],
        "tdp": {
            "min": 15,
            "max": 28
        },
        "has_dgpu": False,
        "max_refresh_rate": 60
    },
    "16_AMD": {
        "name": "16_AMD",
        "display_name": "Framework 16 AMD",
        "processors": ["AMD Ryzen 7 7840HS", "AMD Ryzen 9 7940HS"],
        "tdp": {
            "min": 35,
            "max": 65
        },
        "has_dgpu": True,
        "gpu": "AMD Radeon RX 7700S",
        "max_refresh_rate": 165
    }
} 