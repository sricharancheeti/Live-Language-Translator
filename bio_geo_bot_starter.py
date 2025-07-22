# 🌍🧬 BioGeoBot Data Exploration

# === 1. Install Required Packages ===
# pip install datasets matplotlib pandas

# === 2. Explore Satellite Dataset ===
from datasets import load_dataset
import matplotlib.pyplot as plt
import random
import requests

from Bio import SeqIO

# Load the RGB change detection dataset
data = load_dataset("blanchon/OSCD_RGB", split="train")




# Pick a sample
sample = random.choice(data)

# Show available keys
print("Sample keys:", sample.keys())

# Show the images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(sample["image1"])
axes[0].set_title("Image 1 (Before)")
axes[0].axis("off")

axes[1].imshow(sample["image2"])
axes[1].set_title("Image 2 (After)")
axes[1].axis("off")

axes[2].imshow(sample["mask"], cmap="gray")
axes[2].set_title("Change Mask")
axes[2].axis("off")

plt.tight_layout()
plt.show()


# Load a protein sequence dataset


accessions = ["P04637", "P69905", "P62805"]  
output = "sample_proteins.fasta"

with open(output, "w") as fasta_out:
    for acc in accessions:
        url = f"https://rest.uniprot.org/uniprotkb/{acc}.fasta"
        resp = requests.get(url)
        if resp.status_code == 200 and resp.text.startswith(">"):
            fasta_out.write(resp.text)
            print(f"✅ Downloaded {acc}")
        else:
            print(f"❌ Failed to download {acc}: {resp.status_code}")




fasta_path = "sample_proteins.fasta"
sequences = [str(rec.seq) for rec in SeqIO.parse(fasta_path, "fasta")]

# Quick overview
for rec in SeqIO.parse(fasta_path, "fasta"):
    print(rec.id, len(rec.seq))

lengths = [len(seq) for seq in sequences]
print(f"Lengths: min {min(lengths)}, max {max(lengths)}, avg {sum(lengths)/len(lengths):.2f}")

plt.hist(lengths, bins=10, color="skyblue", edgecolor="black")
plt.xlabel("Sequence length")
plt.ylabel("Count")
plt.title("Protein Lengths")
plt.show()



