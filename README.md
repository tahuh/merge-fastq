# merge-fastq
Merge FASTQ reads

## Requirements
python 2.7 or higher (python3 available)

## Usage

### FOR Paired End read 
```
usage: mergefastq_pe.py [-h] -i READ1 -I READ2 -o OUT1 -O OUT2 [-g]

optional arguments:
  -h, --help            show this help message and exit
  -i READ1, --read1 READ1
                        Read1 file. Can be applied many
  -I READ2, --read2 READ2
                        Read2 file. Can be applied many
  -o OUT1, --out1 OUT1  Output file1
  -O OUT2, --out2 OUT2  Output file2
  -g, --gzip            Output gzip file


Example usage to merge 3 paired end reads into one paired end reads

python mergefastq_pt.py \
--read1 A.read1.fastq.gz \
--read2 A.read2.fastq.gz \
--read1 B.read1.fastq.gz \
--read2 B.read2.fastq.gz \
--read1 C.read1.fastq.gz \
--read2 C.read2.fastq.gz \
--out1 ALL.read1.fastq.gz \
--out2 ALL.read2.fastq.gz \
--gzip
```

### FOR Single End read
```
usage: mergefastq_se.py [-h] -i READ -o OUT [-g]

optional arguments:
  -h, --help            show this help message and exit
  -i READ, --read READ  Read1 file. Can be applied many
  -o OUT, --out OUT     Output file1
  -g, --gzip            Output gzip file


Example usage to merge 3 paired end reads into one paired end reads

python mergefastq_pt.py \
--read A.fastq.gz \
--read B.fastq.gz \
--read C.fastq.gz \
--out ALL.fastq.gz \
--gzip
```
## License
MIT

## Author
Thomas Sunghoon Heo
