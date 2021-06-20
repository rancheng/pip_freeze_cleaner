import os
import argparse

parser = argparse.ArgumentParser(description='requirements.txt cleaner')
parser.add_argument('req_file', type=str,
                    help='requirements.txt file path')

def process(req_file):
    print("processing : " + req_file)
    req_out_file = req_file.replace(".txt", "_fixed.txt")
    with open(req_out_file, "w") as reqoutf:
        with open(req_file, "r") as reqf:
            contents = reqf.readlines()
            for content in contents:
                if "@ file" in content:
                    head, sep, tail = content.partition(' @ file')
                    reqoutf.write(head + "\n")
                else:
                    reqoutf.write(content)
    print("done.")
    print("output file: " + req_out_file)

if __name__ == "__main__":
    args = parser.parse_args()
    process(args.req_file)