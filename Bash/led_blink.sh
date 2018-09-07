gpio mode 0 out
gpio mode 1 out

for i in `seq 1 10`;
do
	gpio write 0 1
	gpio write 1 1
	sleep 0.5
	gpio write 0 0
	gpio write 1 0
	sleep 0.5
done
