import gzip
import glob
import os.path
source_dir = "/Users/nickburrell/Documents/GitHub/loader/input"
dest_dir = "/Users/nickburrell/Documents/GitHub/loader/output"

for src_name in glob.glob(os.path.join(source_dir, '*.gz')):
    base = os.path.basename(src_name)
    dest_name = os.path.join(dest_dir, base[:-3])
    with gzip.open(src_name, 'rb') as infile:
        with open(dest_name, 'wb') as outfile:
            for line in infile:
                outfile.write(line)