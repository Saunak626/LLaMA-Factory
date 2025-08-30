from datasets import load_dataset

# Login using e.g. `huggingface-cli login` to access this dataset
ds = load_dataset("omni-research/DREAM-1K",cache_dir = './video')