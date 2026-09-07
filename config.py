from pathlib import Path


# =========================
# Path
# =========================

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

OUTPUT_DIR = BASE_DIR / "outputs"
CHECKPOINT_DIR = OUTPUT_DIR / "checkpoints"
RESULT_DIR = OUTPUT_DIR / "results"


# =========================
# CSI
# =========================

NUM_RX = 3
NUM_SUBCARRIERS = 52
CSI_FEATURE_DIM = NUM_RX * NUM_SUBCARRIERS  # 156

TARGET_FPS = 10


# =========================
# Reproducibility
# =========================

RANDOM_SEED = 42