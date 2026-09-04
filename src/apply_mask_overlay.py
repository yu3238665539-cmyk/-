from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

folders = [
    "first_run",
    "seed_2",
    "bodhisattva_seed_1",
    "bodhisattva_seed_2",
        "devas_seed_1",
    "devas_seed_2",
    "bhaisajyaguru_seed_1",
    "bhaisajyaguru_seed_2",
    "amitabha_seed_1",
    "amitabha_targeted_seed_1",
    "amitabha_targeted_seed_2",
    "taizong_scene_seed_1",
    "taizong_scene_seed_2",
    "lady_wang_seed_1",
    "lady_wang_seed_2",
    "tiger_jataka_seed_1",
    "tiger_jataka_seed_2",
    "avolokitesvara_seed_1",
]

for folder in folders:
    run_dir = RESULTS / folder
    reference = Image.open(run_dir / "reference.png").convert("RGB")
    masked = Image.open(run_dir / "masked.png").convert("RGB")
    mask = Image.open(run_dir / "mask.png").convert("L")
    generated = Image.open(run_dir / "restored.png").convert("RGB")

    raw_path = run_dir / "restored_raw.png"
    if not raw_path.exists():
        generated.save(raw_path)

    restored = reference.copy()
    restored.paste(generated, mask=mask)
    restored.save(run_dir / "restored.png")

    triptych = Image.new("RGB", (reference.width * 3, reference.height))
    triptych.paste(reference, (0, 0))
    triptych.paste(masked, (reference.width, 0))
    triptych.paste(restored, (reference.width * 2, 0))
    triptych.save(run_dir / "triptych.png")

    print("Updated:", folder)
    