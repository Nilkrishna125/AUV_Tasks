#!/usr/bin/bash


find /home/nilkrishna/input_folder -type f -perm 777 | while read -r files


do
	chmod 755 $files
done

	
