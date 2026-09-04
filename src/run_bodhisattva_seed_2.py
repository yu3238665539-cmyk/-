import json
from pathlib import Path

import torch
from diffusers import StableDiffusionInpaintPipeline
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / "data/raw/Mural_Worshipping_Bodhisattva.jpg"
output_dir = ROOT / "results/bodhisattva_seed_2"
output_dir.mkdir(parents=True, exist_ok=True)

# 固定为 512×512，适配 SD 2 inpainting；原图始终保留，不会被覆盖。
reference = Image.open(source).convert("RGB").resize((512, 512))
mask = Image.new("L", (512, 512), 0)
ImageDraw.Draw(mask).rectangle((192, 192, 320, 320), fill=255)

masked = reference.copy()
masked.paste((0, 0, 0), mask=mask)

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "sd2-community/stable-diffusion-2-inpainting",
    torch_dtype=torch.float16,
    use_safetensors=True,
).to("cuda")

generator = torch.Generator(device="cuda").manual_seed(20260905)
result = pipe(
    prompt=(
        "an ancient Chinese Dunhuang cave mural, Buddhist bodhisattva, "
        "weathered mineral pigments, historical fresco, highly detailed"
    ),
    negative_prompt="modern objects, text, watermark, photograph, 3d render",
    image=masked,
    mask_image=mask,
    num_inference_steps=25,
    guidance_scale=7.5,
    generator=generator,
).images[0]

reference.save(output_dir / "reference.png")
mask.save(output_dir / "mask.png")
masked.save(output_dir / "masked.png")
result.save(output_dir / "restored.png")

triptych = Image.new("RGB", (1536, 512))
triptych.paste(reference, (0, 0))
triptych.paste(masked, (512, 0))
triptych.paste(result, (1024, 0))
triptych.save(output_dir / "triptych.png")

metadata = {
    "source": "Dunhuang mural Buddhist bodhisattvaa; Wikimedia Commons public-domain source",
    "model": "sd2-community/stable-diffusion-2-inpainting",
    "mask": "central 128x128 square at coordinates (192, 192, 320, 320)",
    "seed": 20260905,
    "prompt": "ancient Chinese Dunhuang cave mural, Buddhist bodhisattva, weathered mineral pigments, historical fresco, highly detailed",
    "steps": 25,
    "guidance_scale": 7.5,
}
(output_dir / "metadata.json").write_text(
    json.dumps(metadata, ensure_ascii=False, indent=2),
    encoding="utf-8",
)

print(f"Finished. Results: {output_dir}")