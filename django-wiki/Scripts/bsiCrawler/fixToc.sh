#OIFS="$IFS"
#IFS=$'\n'
for f in mdEn/C/*; do
	echo $f;
	#sed -i 's/description/[toc]/' $f
done
IFS="$OIFS"
