#!/usr/bin/python3
# coding: utf-8
import subprocess
import sys, getopt
from datetime import datetime

def scanner(url):
	target = url
	# 生成输出文件名
	output_target = url.split('//')[1].split('/')[0].replace(':','_')
	timestamp = datetime.timestamp(datetime.now())
	output_file = f'results/report_{output_target}_{timestamp}.html'
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