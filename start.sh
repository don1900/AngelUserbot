#!/bin/bash


echo """
 _   _      _ _______       _   
| | | |    | | | ___ \     | |  
| |_| | ___| | | |_/ / ___ | |_ 
|  _  |/ _ \ | | ___ \/ _ \| __|
| | | |  __/ | | |_/ / (_) | |_ 
\_| |_/\___|_|_\____/ \___/ \__|
                                
"""
rm -rf InVade
git clone https://github.com/don1900/AngelUserbot
cd AngelUserbot
python3 -m angelbot
