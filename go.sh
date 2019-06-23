#!/bin/bash
echo -e '\033[0;36m#############	\033[91m| \033[0mAuto Push fake Rank mirror-h.org';
echo -e '\033[0;36m# \033[93m|PUSH| \033[0;36m#	\033[91m| \033[92m@Author : MR.W4HYU';
echo -e '\033[0;36m# \033[93m|DONG| \033[0;36m#	\033[91m| \033[92m@Github : https://github.com/RADEN-ies'; 
echo -e '\033[0;36m#############	\033[91m| \033[92m@Version : 1.0';
echo '';
echo -e 'Pilih Opsi:';
echo -e '\033[91m[\033[0m1\033[91m] \033[92mSubdomain created';
echo -e '\033[91m[\033[0m2\033[91m] \033[92mSubmiter mirror-h';
echo '';
read -p "LANJUT: " here
if [ $here -eq 1 ];
	then
		clear && chmod +x subdo.php && php subdo.php
elif [ $here -eq 2 ];
	then
		clear && chmod +x mirror-h.py && python2 mirror-h.py
fi
