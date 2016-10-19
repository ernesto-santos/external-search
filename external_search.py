#!/usr/bin/python

import os
import datetime
import glob
import sys
import shutil

def split_and_sort(input_file, lines_per_chunk, temp_dir):
	temp_file_counter = 0
	c_buffer = []
	line_counter = 0

	with open(input_file) as f:
		for line in f:
		 	s_line = line.rstrip('\n')

			c_buffer.append(s_line)
			line_counter += 1

			if (line_counter >= lines_per_chunk):
				c_buffer.sort()

				temp_file_counter += 1
				temp_file = open(temp_dir + '/temp_file_' + str(temp_file_counter) + '.txt', 'w')

				for c_item in c_buffer:
					temp_file.write(c_item + '\n')

				temp_file.close()

				c_buffer = []
				line_counter = 0

	return temp_file_counter

def merge_sorted(output_file, lines_per_chunk, temp_dir):
	if os.path.exists(output_file):
		os.remove(output_file)

	t_filenames = glob.glob(temp_dir + '/*.txt')

	amount_lines_per_read = int(lines_per_chunk / len(t_filenames))

	while True:
		c_buffer = []
		has_data = False

		for t_filename in t_filenames:
			w_buffer = []
			l_counter = 0

			with open(t_filename) as t_in:
				for line in t_in:
					s_line = line.rstrip('\n')

					if s_line:
						if (l_counter <= amount_lines_per_read):
							c_buffer.append(s_line)
						else:
							w_buffer.append(s_line)

						l_counter += 1
						has_data = True

			t_in.close()

			t_out = open(t_filename, 'w')

			for w_item in w_buffer:
				t_out.write(w_item + '\n')

			t_out.close()


		c_buffer.sort()

		o_file = open(output_file, 'a')

		for c_item in c_buffer:
			o_file.write(c_item + '\n')

		o_file.close()

		if not has_data:
			break

if __name__ == '__main__':
	# Parameters
	input_file = './file.txt'
	output_file = './file_py_out.txt'
	lines_per_chunk = 100000

	# Diretorio temporario
	temp_dir = './external_search_' + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

	if not os.path.exists(temp_dir):
		os.makedirs(temp_dir)

	# Call the functions
	temp_file_counter = split_and_sort(input_file, lines_per_chunk, temp_dir)
	merge_sorted(output_file, lines_per_chunk, temp_dir)

	if os.path.exists(temp_dir):
		shutil.rmtree(temp_dir)
