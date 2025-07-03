#!/usr/bin/env python3
import requests
from tqdm import tqdm
import sys

def download(url, output):
    response = requests.get(url, stream=True)
    total = int(response.headers.get('content-length', 0))
    with open(output, "wb") as file, tqdm(
        desc=output,
        total=total,
        unit="iB",
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in response.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    try:
        download(args.url, args.output)
        print(f"Download completed: {args.output}")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


# GEREKLİ PAKETLER #
# REQUESTS, TQDM #
