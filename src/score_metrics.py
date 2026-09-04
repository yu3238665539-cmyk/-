import csv
from pathlib import Path

import numpy as np
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"

runs = [
    ("Dunhuang flying apsarasa", "20260902", "first_run"),
    ("Dunhuang flying apsarasa", "20260903", "seed_2"),
    ("Mogao Cave 285 worshipping bodhisattva", "20260904", "bodhisattva_seed_1"),
    ("Mogao Cave 285 worshipping bodhisattva", "20260905", "bodhisattva_seed_2"),
        ("Mogao Cave 272 devas", "20260906", "devas_seed_1"),
    ("Mogao Cave 272 devas", "20260907", "devas_seed_2"),
    ("Mogao Cave 322 Bhaisajyaguru mural", "20260908", "bhaisajyaguru_seed_1"),
    ("Mogao Cave 322 Bhaisajyaguru mural", "20260909", "bhaisajyaguru_seed_2"),
    ("Mogao Cave 172 Buddhist Paradise of Amitabha", "20260911", "amitabha_targeted_seed_1"),
    ("Mogao Cave 172 Buddhist Paradise of Amitabha", "20260912", "amitabha_targeted_seed_2"),
    ("Dunhuang historical narrative scene", "20260913", "taizong_scene_seed_1"),
    ("Dunhuang historical narrative scene", "20260914", "taizong_scene_seed_2"),
    ("Portrait detail from The Governor’s Wife Offering, Mogao Cave 130", "20260915", "lady_wang_seed_1"),
    ("Portrait detail from The Governor’s Wife Offering, Mogao Cave 130", "20260916", "lady_wang_seed_2"),
    ("Tiger Jataka, Mogao Cave 254, Northern Wei", "20260917", "tiger_jataka_seed_1"),
    ("Tiger Jataka, Mogao Cave 254, Northern Wei", "20260918", "tiger_jataka_seed_2"),
    ("Mural Avolokitesvara, Tang Dynasty, Dunhuang", "20260919", "avolokitesvara_seed_1"),
    ("Mural Avolokitesvara, Tang Dynasty, Dunhuang", "20260920", "avolokitesvara_seed_2"),
    ("Story of the Five Hundred Robbers, Mogao Cave 285, Western Wei", "20260921", "five_hundred_robbers_seed_1"),
    ("Story of the Five Hundred Robbers, Mogao Cave 285, Western Wei", "20260922", "five_hundred_robbers_seed_2"),
    ("Uyghur princesses, Mogao Cave 409", "20260923", "uyghur_princesses_seed_1"),
    ("Uyghur princesses, Mogao Cave 409", "20260924", "uyghur_princesses_seed_2"),
    ("Mogao mural of Vinayaka, Cave 285, Western Wei", "20260925", "vinayaka_seed_1"),
    ("Mogao mural of Vinayaka, Cave 285, Western Wei", "20260926", "vinayaka_seed_2"),
    ("Lotus Sutra tableau, Mogao Cave 217, High Tang", "20260927", "lotus_sutra_seed_1"),
    ("Lotus Sutra tableau, Mogao Cave 217, High Tang", "20260928", "lotus_sutra_seed_2"),
    ("Pipa player mural, Mogao Cave 220", "20260929", "pipa_seed_1"),
    ("Pipa player mural, Mogao Cave 220", "20260930", "pipa_seed_2"),
    ("Architecture detail from Mogao Cave 217, Tang Dynasty", "20261001", "architecture_seed_1"),
    ("Architecture detail from Mogao Cave 217, Tang Dynasty", "20261002", "architecture_seed_2"),
]

rows = []

for sample, seed, folder in runs:
    run_dir = RESULTS / folder
    reference = np.asarray(Image.open(run_dir / "reference.png").convert("RGB"))
    restored = np.asarray(Image.open(run_dir / "restored.png").convert("RGB"))
    mask = np.asarray(Image.open(run_dir / "mask.png").convert("L")) > 0

    y, x = np.where(mask)
    y1, y2 = y.min(), y.max() + 1
    x1, x2 = x.min(), x.max() + 1

    reference_roi = reference[y1:y2, x1:x2]
    restored_roi = restored[y1:y2, x1:x2]

    psnr = peak_signal_noise_ratio(reference_roi, restored_roi, data_range=255)
    ssim = structural_similarity(
        reference_roi,
        restored_roi,
        multichannel=True,
        data_range=255,
    )
    full_psnr = peak_signal_noise_ratio(reference, restored, data_range=255)
    full_ssim = structural_similarity(
        reference,
        restored,
        multichannel=True,
        data_range=255,
    )

    rows.append({
        "sample": sample,
        "seed": seed,
        "run_folder": folder,
                "full_image_psnr": round(np.asarray(full_psnr).item(), 3),
        "full_image_ssim": round(np.asarray(full_ssim).item(), 4),
    "masked_region_psnr": round(np.asarray(psnr).item(), 3),
"masked_region_ssim": round(np.asarray(ssim).item(), 4),
    })

output = RESULTS / "traditional_metrics.csv"
with output.open("w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

for row in rows:
    print(row)

print("Saved:", output)