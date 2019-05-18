mkdir labels
for d in $(find ./ -maxdepth 1 -type d)
do
  #Do something, the directory is accessible with $d:
  for f in $(find $d -maxdepth 1 -type d)
  do
    a=$(ls $f | grep "annotations.txt" | wc -l)
    if [ $a -gt 0 ]
    then
	echo $f
	cp convert_annotations.py $f
	cd $f
	python3 convert_annotations.py
	rm convert_annotations.py
	mv labels/* ../../labels/
	cd ../../
    fi
  done
done 
