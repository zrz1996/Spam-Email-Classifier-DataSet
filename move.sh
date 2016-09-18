#! /bin/sh

filelist=`ls ./emailPlain/`
for file in $filelist
do
	fname=`basename $file .txt`
	label=`grep $fname SPAMTrain.label`
	if [[ $label == 1* ]]; then
		cp ./emailPlain/$file ./ham/$file
	else
		cp ./emailPlain/$file ./spam/$file
	fi
done
