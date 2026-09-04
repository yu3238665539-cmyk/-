# Manual Review Table: Preliminary Historical Hallucination Risk Assessment

| Sample | Seed | Masked evidence | AI reconstruction | Repeated inconsistency | Preliminary risk |
|---|---:|---|---|---|---|
| Dunhuang flying apsarasa | 20260902 | White patterned head ornament; fine, faded lines | Dark, thick loop-like hair/headdress | Original ornament not recovered; line style becomes heavy and dark | High |
| Dunhuang flying apsarasa | 20260903 | White patterned head ornament; fine, faded lines | Dark disk plus a light circular ornament | Different shape from seed 1, but original ornament still not recovered | High |
| Mogao Cave 285 worshipping bodhisattva | 20260904 | Pale green halo with white inner ring; thin crown and ribbons | Dark green-black halo; thick dark crown/hair mass | White ring and thin crown/ribbons disappear; line and tone become heavy | High |
| Mogao Cave 285 worshipping bodhisattva | 20260905 | Pale green halo with white inner ring; thin crown and ribbons | Dark olive-black disk; block-like dark ornament | Same error category as seed 1 despite different generated shape | High |

## Preliminary finding

Across two murals and four controlled generations, the model produced visually continuous masked regions but repeatedly failed to reproduce evidence-bearing iconographic details. Changing the random seed changed the invented form, not the error category. This is treated as a candidate historical hallucination risk rather than a final archaeological conclusion.

| Mogao Cave 272 devas | 20260906 | Pale green halo, simple crown, archaic facial style | Dark heavy halo/crown and modernized face | Halo and crown are replaced; lines and pigments become heavier | High |
| Mogao Cave 272 devas | 20260907 | Pale green halo, simple crown, archaic facial style | Background-filled halo and invented complex ornament | Same error category with a different invented form | High |

## Case 4 — Bhaisajyaguru mural, Mogao Cave 322

**Mask target:** The central chest, arms, hands, and red robe folds of the Medicine Buddha.

### Seed 20260908 — bhaisajyaguru_seed_1
The model generated the chest, arms, hands, and red robe folds as a plausible Buddhist figure. However, it replaced the original iconographic details: the left-hand medicine bowl/object was absent, and the original raised right-hand gesture was changed into hands gathered in front of the chest. The robe folds were denser and more curved than in the reference.

### Seed 20260909 — bhaisajyaguru_seed_2
The model again generated a plausible torso, arms, hands, and robe folds. The generated hands appeared more symmetrical and closer to a prayer-like gesture than in seed 1. Yet the medicine bowl/object and the original right-hand gesture were again absent.

### Cross-seed pattern
The generated form changed across seeds, but the same historical error remained: both outputs preserved a generic “Buddhist figure” appearance while altering identity-relevant iconographic evidence—the medicine bowl/object and the original hand gesture. This is a plausible-but-historically-inconsistent reconstruction.

## Case 5 — Buddhist Paradise of Amitabha, Mogao Cave 172, Tang Dynasty

**Mask target:** The circular halo, face, upper body, and hand region of the central Amitabha figure.

### Seed 20260911 — amitabha_targeted_seed_1
The original masked region contained the central Buddha’s circular halo, face, upper body, and hands. The model did not reconstruct the Buddha. Instead, it generated a large pale S-shaped ribbon-like form, round decorative marks, and dark ornamental textures. The original central figure and halo were not recovered.

### Seed 20260912 — amitabha_targeted_seed_2
The model produced a darker, vaguely figure-like form, but replaced the original circular halo and Buddha structure with a large symmetric pale crown-like or vessel-like shape. The generated form was not consistent with the reference figure’s head halo, facial structure, seated posture, or hand arrangement.

### Cross-seed pattern
Both seeds replaced the identity-defining Amitabha figure rather than restoring it. The invented form differed between seeds, but neither output preserved the reference halo or the core figure structure. This is a high historical hallucination risk: plausible decorative or figure-like content replaced identifiable religious iconography.

## Case 6 — Dunhuang historical narrative scene

**Source note:** Wikimedia file titled “Emperor Taizong in Dunhuang”. The experiment does not independently assert the identity of the depicted historical figure.

**Mask target:** The central overlap of human figures, horse-related structure, costume, and narrative linework.

### Seed 20260913 — taizong_scene_seed_1
The model replaced the masked narrative region with an isolated pale female-like side face and a dark round hair bun. This clean portrait-like element was not supported by the reference, where the area belonged to an overlapping human-and-horse narrative structure.

### Seed 20260914 — taizong_scene_seed_2
The model again invented an isolated figure-like element, this time with a large dark short-hair or head-covering shape, a pale face, and a newly defined collar/upper-body form. The original relationship among figures, horse-related details, and costume lines was not restored.

### Cross-seed pattern
Across both seeds, the generated form changed but the same error persisted: the model transformed a complex historical narrative region into an unsupported, visually prominent individual portrait. This represents high historical hallucination risk.

## Case 7 — Portrait detail from The Governor’s Wife Offering, Mogao Cave 130

**Mask target:** The eye, nose, cheek, mouth-adjacent region, facial linework, and surface cracks of a female attendant portrait.

### Seed 20260915 — lady_wang_seed_1
The model retained the general portrait and hair ornaments, but redrew the masked eye with a darker, thicker, and more polished almond-like form. Fine facial linework and weathered cracks were weakened, producing a cleaner and more modern-looking facial treatment.

### Seed 20260916 — lady_wang_seed_2
The model again altered the same eye, but with a different high, thin, upturned eyelid and shifted pupil/gaze position. The output still weakened the original delicate linework and surface-aging traces.

### Cross-seed pattern
Both outputs preserved the broad identity of a female portrait, yet neither preserved the reference eye design and face-surface texture. The seeds changed the exact invented eye form, indicating moderate historical hallucination risk: a visually plausible but stylistically and materially altered portrait.

## Case 8 — Tiger Jataka, Mogao Cave 254, Northern Wei

**Mask target:** The lower-right tiger’s head, torso, stripe pattern, and adjacent turquoise rock background.

### Seed 20260917 — tiger_jataka_seed_1
The model did not restore the tiger. It generated a gray-black, figure-like or drapery-like mass with unsupported pale circular and ribbon-like elements. The reference tiger’s animal contour and stripe pattern were absent.

### Seed 20260918 — tiger_jataka_seed_2
The model again failed to restore the tiger. It generated a more clearly outlined beige, blue-green, and red-brown hybrid creature-like or ornamental structure. This output also lacked the reference tiger’s anatomy, stripes, and narrative pose.

### Cross-seed pattern
Both seeds replaced an identifiable narrative animal with different unsupported forms. The generated shape changed across seeds, but neither output recovered the tiger as depicted in the reference. This is high historical hallucination risk.

## Case 9 — Mural Avolokitesvara, Tang Dynasty, Dunhuang

**Mask target:** The lower crown, forehead, face, eyes, nose, mouth, and inner halo region of the central Avolokitesvara figure.

### Seed 20260919 — avolokitesvara_seed_1
The model replaced the weathered face with thick black arched eye lines, a forehead dot, and a conspicuous toothy smile. These expressive, cartoon-like facial elements were absent from the reference mural.

### Seed 20260920 — avolokitesvara_seed_2
The model again redrew the face with bold symmetric eyebrows and eyes, stronger red lips, and a smooth gray-white complexion. It also introduced a dark band with blue and pale decorative elements across the forehead, which was not present in the reference crown or face.

### Cross-seed pattern
Both outputs retained a generic haloed bodhisattva appearance but invented identity-defining facial and crown details. The exact hallucinated face changed with the seed, while the historical inconsistency remained. This is high historical hallucination risk.

## Case 10 — Story of the Five Hundred Robbers, Mogao Cave 285, Western Wei

**Mask target:** The helmet, upper-body armor, horse-back junction, and nearby weapon/linework of a mounted soldier.

### Seed 20260921 — five_hundred_robbers_seed_1
The model replaced the armored-rider region with a taller, unfamiliar figure- or object-like structure containing unsupported dark blocks, red-brown decoration, and reorganized body lines. The original rider-on-horse relationship was not restored.

### Seed 20260922 — five_hundred_robbers_seed_2
The model produced a generic rider-and-horse concept, but rendered it as an unusually clean, white-outline horse and rider. The reference blue-green armor, horse-back proportions, and dense historical linework were not recovered.

### Cross-seed pattern
Both seeds recognized a broad mounted-figure context but failed to preserve the specific Western Wei armor, horse structure, and line quality. The result remained visually plausible at a generic level while historically inconsistent in concrete form.

## Case 11 — Uyghur princesses, Mogao Cave 409

**Mask target:** The left figure’s ornate headdress, weathered dark face, and adjacent floral decoration.

### Seed 20260923 — uyghur_princesses_seed_1
The model replaced the weathered dark face with a clean, high-contrast black face containing clear pale eyes, nose, and mouth. It also introduced a large red-and-blue flower-like ornament not present in the reference.

### Seed 20260924 — uyghur_princesses_seed_2
The model again redrew the face as a clean, highly legible portrait. The adjacent invented decoration changed from a flower-like form to large blue curling petals or leaves, which were likewise unsupported by the reference.

### Cross-seed pattern
Both seeds transformed weathered historical features into a sharper, more modern-looking face and invented adjacent ornament. The form changed across seeds, but the facial and decorative historical inconsistency persisted. This is high historical hallucination risk.

## Case 12 — Mogao mural of Vinayaka, Cave 285, Western Wei

**Mask target:** The elephant head, eyes, upper trunk, ear contour, and head-halo area of Vinayaka.

### Seed 20260925 — vinayaka_seed_1
The model retained a trunk-like feature but redrew the deity as a more anthropomorphic, expressive hybrid face. It introduced stylized human-like eyes and altered the ear, face boundary, and head-top elements, losing the reference’s weathered linework.

### Seed 20260926 — vinayaka_seed_2
The model produced an even more cartoon-like elephant-human face, with an exaggerated long trunk marked by regular horizontal stripes, strongly expressive eyes and mouth, and an enlarged re-outlined ear. These details were not present in the reference mural.

### Cross-seed pattern
Both seeds retained only a generic elephant-headed concept while inventing concrete facial, trunk, and ear features. The iconographic category remained recognizable, but the historical form was not faithfully reconstructed. This is high historical hallucination risk.

## Case 13 — Lotus Sutra tableau, Mogao Cave 217 South Wall, High Tang

**Mask target:** The halo, face, red upper robe, and seated posture of the central preaching Buddha.

### Seed 20260927 — lotus_sutra_seed_1
The model retained a generic central seated-Buddha composition, but replaced the reference’s complex blue-green halo and weathered facial details with a larger dark oval head form and bright pale outline. The red robe became cleaner, more saturated, and structurally simplified.

### Seed 20260928 — lotus_sutra_seed_2
The model again produced a generic seated figure, but rendered it as a clean pale turquoise robe with a dark simplified head. The reference red-and-dark robe layers, facial details, hand arrangement, and dense surrounding structure were not restored.

### Cross-seed pattern
Both seeds preserved only the broad “central seated Buddha” concept while changing the historical halo, face, robe color, and figure details. This is a plausible but historically unsupported reconstruction.

## Case 14 — Pipa player mural, Mogao Cave 220

**Mask target:** The pipa body, neck-to-body junction, string area, and part of the musician’s playing hand.

### Seed 20260929 — pipa_seed_1
The model broadly retained a horizontally held instrument, but replaced the reference pipa body sections, fine strings, and hand-to-string relationship with darker brown slanted blocks and unclear contours.

### Seed 20260930 — pipa_seed_2
The model again retained only a general instrument-like shape. The masked region became smoother pale and blue-green color areas with simplified curved lines, while the reference’s pipa segmentation, string detail, and playing-hand relationship remained unrecovered.

### Cross-seed pattern
Both outputs preserved a generic musical-instrument context but did not restore the concrete pipa structure or playing configuration. This indicates moderate historical hallucination risk for material-culture details.

## Case 15 — Architecture detail from Mogao Cave 217, Tang Dynasty

**Mask target:** The central pavilion roof, red-column facade, railings, and their spatial relationships.

### Seed 20261001 — architecture_seed_1
The model preserved the general Dunhuang architectural context of green roofs, red columns, and a multi-storey pavilion. However, it rewrote the masked roof layers, facade divisions, window or railing patterns, and central opening. The reconstructed structures look coherent but do not reproduce the reference building’s specific spatial and decorative relationships.

### Seed 20261002 — architecture_seed_2
The model again generated a plausible pavilion-like structure, but introduced more regular, horizontally extended roof and facade bands. The reference roof hierarchy, red-column correspondences, openings, and detailed architectural relationships were again replaced rather than restored.

### Cross-seed pattern
Both seeds preserved only a generic ancient-architecture concept while inventing different concrete roof, facade, and railing structures. The outputs are visually plausible but historically unsupported. This is medium-to-high historical hallucination risk.