#!/bin/bash
#This script will create a file on the currently logged in user's desktop labeled
#score_report.txt

#Created by Moses J. Arocha

score=0
total_score=6

credit_check=`cat /etc/pam.d/common-password | grep -o "credit" | wc -l`
retry_check=`cat /etc/pam.d/common-password | grep -o "retry" | wc -l`
minlen_check=`cat /etc/pam.d/common-password | grep "minlen" | wc -l`
difok_check=`cat /etc/pam.d/common-password | grep "difok" | wc -l`

IFS=';' read updates security_updates < <(/usr/lib/update-notifier/apt-check 2>&1)


echo "Cyber Patriot Score Report: "  > ~/Desktop/score_report.txt
echo " " >> ~/Desktop/score_report.txt

if [[ $updates -eq 0 ]]; then
    ((score++))
    echo "You have performed updates to the system" >> ~/Desktop/score_report.txt
else
    echo "There are updates still left" >> ~/Desktop/total_score.txt
fi

if [[ $security_updates == 0 ]]; then
    ((score++))
    echo "You have performed security updates to the system " >> ~/Desktop/score_report.txt
else
    echo "There are security updates still left" >> ~/Desktop/score_report.txt
fi

if [[ $credit_check -eq 4 ]]; then
    ((score++))
    echo "You have successfully added character requirements" >> ~/Desktop/score_report.txt
fi 

if [[ $retry_check -eq 1 ]]; then
    ((score++))
    echo "You have successfully set a maximum number of login attempts" >> ~/Desktop/score_report.txt
fi
if [[ $minlen_check -eq 1 ]]; then
    ((score++))
    echo "You have successfully set a minimum password length" >> ~/Desktop/score_report.txt
fi
if [[ $difok_check -eq 1 ]]; then
    ((score++))
    echo "You have sucessfully set character password rememberance length" >> ~/Desktop/score_report.txt
fi

echo " " >> ~/Desktop/score_report.txt
echo "Your Score Total:$score/$total_score" >> ~/Desktop/score_report.txt

