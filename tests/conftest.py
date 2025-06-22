import sys
import types
from pathlib import Path

# Provide a minimal stub for the Vectorworks `vs` module so modules can be
# imported outside of Vectorworks during testing.
sys.modules.setdefault('vs', types.SimpleNamespace())

# Ensure the repository root is on sys.path so test modules can import scripts
# located there.
repo_root = Path(__file__).resolve().parents[1]
if str(repo_root) not in sys.path:
    sys.path.insert(0, str(repo_root))
