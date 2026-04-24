from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent
SPLIT_DIR = ROOT / "assets" / "_split_parts"

TARGETS = {
    "f2-19-map-compare.png": ROOT / "assets" / "f2-19-map-compare.png",
    "locate-slam.mp4": ROOT / "assets" / "videos" / "locate-slam.mp4",
}

def MergeOne(name: str, target: Path) -> bool:
    parts = sorted(SPLIT_DIR.glob(f"{name}.part-*"))
    if not parts:
        return False
    target.parent.mkdir(parents=True, exist_ok=True)
    with target.open("wb") as fout:
        for part in parts:
            with part.open("rb") as fin:
                shutil.copyfileobj(fin, fout)
    print(f"已合并: {target.relative_to(ROOT)}  ({len(parts)} 个分片)")
    return True

if __name__ == "__main__":
    any_merged = False
    for name, target in TARGETS.items():
        any_merged = MergeOne(name, target) or any_merged
    if not any_merged:
        print("未找到需要合并的分片。")
    else:
        print("完成。现在可以直接打开 index.html。")
