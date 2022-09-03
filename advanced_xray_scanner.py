#!/usr/bin/python3
# coding: utf-8
import subprocess
import sys, getopt

def scanner(url):
	target = url
	cmd = ["./xray", "webscan", "--browser-crawler", target, "--html-output", "results/report__datetime__.html"]
	rsp=subprocess.Popen(cmd)
	output, error = rsp.communicate()
	print(output)


def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hi:",["input_file="])
	except getopt.GetoptError:
		print(sys.argv[0] + ' -i <input_file>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print(sys.argv[0] + ' -i <input_file>')
			sys.exit()
		elif opt in ("-i", "--input_file"):
			input_file = arg
	urls = open(input_file)
	for text in urls.readlines():
		url = text.strip()
		if not url =='':
			scanner(url)


if __name__=='__main__':
	main(sys.argv[1:])