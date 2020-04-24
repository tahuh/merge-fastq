#!/usr/bin/python
"""
Merge FASTQ files in Paired End manner

Author : tahuh
"""
from __future__ import print_function
import argparse
import gzip

def fmt_chk(f):
	h= open(f, "rb")
	b = h.read(2)
	h.close()
	if b == "\x1f\x8b":
		return gzip.open(f)
	else:
		return open(f)

def write_outfile(content_str, handle, gzip=False):
	if gzip == True:
		handle.write(content_str.encode())
	else:
		handle.write(content_str)

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--read1", type=str, action="append", help="Read1 file. Can be applied many", required=True)
parser.add_argument("-I", "--read2", type=str, action="append", help="Read2 file. Can be applied many", required=True)
parser.add_argument("-o", "--out1", type=str, help="Output file1", required=True)
parser.add_argument("-O", "--out2", type=str, help="Output file2",required=True)
parser.add_argument("-g", "--gzip", help="Output gzip file",default=False,action="store_true")

args = parser.parse_args()

if len(args.read1) != len(args.read2):
	print("--read1 and --read2 has different number of files")
	exit(-1)

if args.gzip:
	o1 = gzip.open(args.out1, "wb")
	o2 = gzip.open(args.out2, "wb")
else:
	o1 = open(args.out1)
	o2 = open(args.out2)

print ("start....")
for f1, f2 in zip(args.read1, args.read2):
	print("%s | %s"%(f1,f2))
	h1 = fmt_chk(f1)
	h2 = fmt_chk(f2)
	for line1 in h1:
		line2 = h2.next()
		write_outfile(line1, o1, gzip=args.gzip)
		write_outfile(line2, o2, gzip=args.gzip)
	h1.close()
	h2.close()
o1.close()
o2.close()
print("done...")
