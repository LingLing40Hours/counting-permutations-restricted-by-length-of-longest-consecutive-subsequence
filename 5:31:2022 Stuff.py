Python 3.9.10 (main, Feb 19 2022, 01:53:40) 
[Clang 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> PDraw(6,4,4,False,True)
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> PDraw(6,4,2,False,False)
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> PDraw(6,4,2,False,False)
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> PDraw(6,4,2,False,False)
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> PDraw(6,4,2,False,False)
>>> 1/200/0.000001
5000.0
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> PDraw(6,4,2,False,False)
>>> for n in range(2,10):
	row = '';
	for k in range(k+1):
		Pbash = PBash(n,k,4,False,True);
		row +=str(Pbash)+'\t';
	print(row);

	
Traceback (most recent call last):
  File "<pyshell#13>", line 3, in <module>
    for k in range(k+1):
NameError: name 'k' is not defined
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,4,False,True);
		row +=str(Pbash)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	104	110	
1	6	30	120	336	680	672	
1	7	42	210	808	2430	4824	4788	
1	8	56	336	1640	6560	19584	38976	38800	
1	9	72	504	2976	14870	59280	177240	353344	352206	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = PBash(n,k,4,True,True)+3*UBash(n-2,k-2,4)+2*UBash(n-3,k-3,4)+UBash(n-4,k-4,4)-2*Z0Bash(n-3,k-3,4)-6*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-2*Z0Bash(n-6,k-6,4)+2*Z0Bash(n-2,k-2,4)+2*Z0Bash(n-3,k-3,4)+Z0Bash(n-2,k-2,4)+Z0Bash(n-4,k-4,4)+2*Z0Bash(n-2,k-2,4)
		row +=str(Pcalc)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	22	
1	5	20	60	96	114	
1	6	30	120	328	676	666	
1	7	42	210	800	2418	4800	4760	
1	8	56	336	1632	6540	19524	38852	38684	
1	9	72	504	2968	14842	59168	176900	352680	351554	
>>> PDraw(5,4,4,False,True)
>>> 2*UBash(4,3)-2*Z0Bash(2,1)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    2*UBash(4,3)-2*Z0Bash(2,1)
TypeError: UBash() missing 1 required positional argument: 'j'
>>> 2*UBash(4,3,4)-2*Z0Bash(2,1,4)
8
>>> 2*Z0Bash(3,2,4)+2*Z0Bash(2,1,4)+Z0Bash(3,2,4)+Z0Bash(1,0,4)+2*Z0Bash(3,2,4)
10
>>> 2*Z0Bash(3,2,4)+2*Z0Bash(2,1,4)+Z0Bash(3,2,4)+Z0Bash(1,0,4)
6
>>> 2*Z0Bash(3,2,4)
4
>>> PDraw(5,4,4,True,True)
>>> PBash(5,4,4,False,True)
104
>>> PBash(5,4,4,True,True)
80
>>> n=5;k=4;
>>> 3*UBash(n-2,k-2,4)+2*UBash(n-3,k-3,4)+UBash(n-4,k-4,4)-2*Z0Bash(n-3,k-3,4)-6*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-2*Z0Bash(n-6,k-6,4)
6
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = PBash(n,k,4,True,True)+3*UBash(n-2,k-2,4)+2*UBash(n-3,k-3,4)+UBash(n-4,k-4,4)-2*Z0Bash(n-3,k-3,4)-6*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-2*Z0Bash(n-6,k-6,4)+2*Z0Bash(n-2,k-2,4)+2*Z0Bash(n-3,k-3,4)+Z0Bash(n-2,k-2,4)+Z0Bash(n-4,k-4,4)+2*Z0Bash(n-2,k-2,4)+4*Z0Bash(n-2,k-2,4)
		row +=str(Pcalc)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	22	
1	5	20	60	104	114	
1	6	30	120	336	676	674	
1	7	42	210	808	2426	4824	4784	
1	8	56	336	1640	6556	19580	38964	38788	
1	9	72	504	2976	14866	59272	177212	353288	352154	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,4,False,True);
		row +=str(Pbash)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	104	110	
1	6	30	120	336	680	672	
1	7	42	210	808	2430	4824	4788	
1	8	56	336	1640	6560	19584	38976	38800	
1	9	72	504	2976	14870	59280	177240	353344	352206	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = PBash(n,k,4,True,True)+3*UBash(n-2,k-2,4)+2*UBash(n-3,k-3,4)+UBash(n-4,k-4,4)-2*Z0Bash(n-3,k-3,4)-6*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-2*Z0Bash(n-6,k-6,4)+2*Z0Bash(n-2,k-2,4)+2*Z0Bash(n-3,k-3,4)+Z0Bash(n-2,k-2,4)+Z0Bash(n-4,k-4,4)+2*Z0Bash(n-2,k-2,4)+4*Z0Bash(n-2,k-2,4)+2*Z0Bash(n-3,k-3,4)
		row +=str(Pcalc)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	22	
1	5	20	60	104	114	
1	6	30	120	336	680	674	
1	7	42	210	808	2430	4824	4788	
1	8	56	336	1640	6560	19584	38976	38800	
1	9	72	504	2976	14870	59280	177240	353344	352206	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,4,True,True);
		row +=str(Pbash)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> SBash(8,7,3)
8640
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> SBash(8,7,3)
7318
>>> SBash(8,8,3)
7052
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,4,True,True);
		row +=str(Pbash)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
		row +=str(Pcalc)+'\t';
	print(row);

	
0	2	0	
Traceback (most recent call last):
  File "<pyshell#43>", line 4, in <module>
    Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 382, in SBash
    if p[0] in (1, n) and abs(p[1]-p[0])!=1 and consecutivity(n, p, False, False)<j:
IndexError: list index out of range
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
		row +=str(Pcalc)+'\t';
	print(row);

	
0	2	0	
0	3	6	0	
0	4	12	24	16	
Traceback (most recent call last):
  File "<pyshell#45>", line 4, in <module>
    Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 384, in SBash
    if p[0] in (1, n) and abs(p[1]-p[0])!=1 and consecutivity(n, p, False, False)<j:
IndexError: list index out of range
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
		row +=str(Pcalc)+'\t';
	print(row);

	
0	2	0	
0	3	6	0	
0	4	12	24	16	
Traceback (most recent call last):
  File "<pyshell#47>", line 4, in <module>
    Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 384, in SBash
    if p[0] in (1, n) and k==1:
IndexError: list index out of range
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		row += str(SBash(n,k,3))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#53>", line 4, in <module>
    row += str(SBash(n,k,3))+'\t';
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 394, in SBash
    if consecutivity(n, p, False, False)<j and backToAnywhere(n,p):
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 143, in backToAnywhere
    if p[0] in (1,n):
NameError: name 'p' is not defined
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		row += str(SBash(n,k,3))+'\t';
	print(row)

	
0	2	2	
0	2	2	0	
0	2	2	2	2	
0	2	2	4	8	6	
0	2	2	6	18	30	28	
0	2	2	8	32	86	162	150	
0	2	2	10	50	186	532	1008	962	
0	2	2	12	72	342	1318	3798	7318	7052	
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		row += str(SBash(n,k,3))+'\t';
	print(row)

	
0	2	2	
0	2	2	0	
0	2	2	2	2	
0	2	2	4	8	6	
0	2	2	6	18	30	28	
0	2	2	8	32	86	162	150	
0	2	2	10	50	186	532	1008	962	
0	2	2	12	72	342	1318	3798	7318	7052	
>>> SBash(8,8,3)
962
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		row += str(SBash(n,k,3))+'\t';
	print(row)

	
0	2	0	
0	2	0	0	
0	2	0	0	0	
0	2	0	0	0	0	
0	2	0	0	0	0	0	
0	2	0	0	0	0	0	0	
0	2	0	0	0	0	0	0	0	
0	2	0	0	0	0	0	0	0	0	
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		row += str(SBash(n,k,3))+'\t';
	print(row)

	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(PBash(n-1,k-1,4,False,False)-2*SBash(n-3,k-3,4)+2*ZXyBash(n-1,k-1,4,2,2)-ZBash(n-1,k-1,4)+Z0Bash(n-1,k-1,4));
		row +=str(Pcalc)+'\t';
	print(row);

	
0	2	0	
0	3	6	0	
0	4	12	24	8	
0	5	20	60	80	110	
0	6	30	120	312	660	636	
0	7	42	210	784	2380	4704	4634	
0	8	56	336	1616	6480	19296	38304	38064	
0	9	72	504	2952	14760	58752	175392	349200	347634	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,4,True,True);
		row +=str(Pbash)+'\t';
	print(row);

	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> 0.5*(SBash(10-3,8-3,4)-ZXyBash(10-1,8-1,2,2))
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    0.5*(SBash(10-3,8-3,4)-ZXyBash(10-1,8-1,2,2))
TypeError: ZXyBash() missing 1 required positional argument: 'y'
>>> 0.5*(SBash(10-3,8-3,4)-ZXyBash(10-1,8-1,4,2,2))
248.0
>>> ZxyBash(10,8,4,0,2)
496
>>> 0.5*(SBash(11-3,8-3,4)-ZXyBash(11-1,8-1,4,2,2))
614.0
>>> ZxyBash(11,8,4,0,2)
1228
>>> for x in range(1,5):
	for j in range(2,5):
		for n in range(2,9):
			for k in range(n+1):
				print(str(ZxyBash(n,k,j,0,x))+' = '+str(SBash(n-x-1,k-x-1,j)-ZXyBash(n-1,k-1,j,j-2,x)));

				
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
4 = 4
6 = 6
4 = 4
4 = 4
0 = 0
0 = 0
0 = 0
2 = 2
6 = 6
14 = 14
22 = 22
30 = 30
20 = 20
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
6 = 6
4 = 4
0 = 0
0 = 0
0 = 0
2 = 2
4 = 4
14 = 14
24 = 24
22 = 22
0 = 0
0 = 0
0 = 0
2 = 2
6 = 6
26 = 26
70 = 70
132 = 132
124 = 124
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
6 = 6
6 = 6
0 = 0
0 = 0
0 = 0
2 = 2
4 = 4
14 = 14
28 = 28
26 = 26
0 = 0
0 = 0
0 = 0
2 = 2
6 = 6
26 = 26
78 = 78
152 = 152
150 = 150
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
4 = 4
6 = 6
4 = 4
4 = 4
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
6 = 6
4 = 4
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
4 = 4
14 = 14
24 = 24
22 = 22
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
6 = 6
6 = 6
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
4 = 4
14 = 14
28 = 28
26 = 26
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
6 = 6
4 = 4
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
2 = 2
6 = 6
6 = 6
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 1
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
0 = 0
2 = 2
0 = 0
2 = 2
>>> for x in range(1,5):
	for j in range(2,5):
		for n in range(2,9):
			for k in range(n+1):
				if SBash(n-x-1,k-x-1,j)-ZXyBash(n-1,k-1,j,j-2,x)==1:
					print(x, j, n, k);
					break;

				
1 2 3 3
1 3 3 3
1 4 3 3
2 2 4 4
2 3 4 4
2 4 4 4
3 2 5 5
3 3 5 5
3 4 5 5
4 2 6 6
4 3 6 6
4 4 6 6
>>> SBash(1,1,2)
1
>>> def f(x):
	return 2;

>>> def f(list):
	ans = 0;
	for i in list:
		ans+=i;
	return ans;

>>> f(3)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    f(3)
  File "<pyshell#91>", line 3, in f
    for i in list:
TypeError: 'int' object is not iterable
>>> for x in range(11):
	row='';
	for y in range(11):
		row += str(ZxyBash(6,4,2,x,y))+'\t';
	print(row);

	
6	2	2	0	0	0	0	0	0	0	0	
2	2	0	0	0	0	0	0	0	0	0	
2	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
>>> for x in range(11):
	row='';
	for y in range(11):
		row += str(ZxyBash(12,8,2,x,y))+'\t';
	print(row);

	
75314	8098	990	142	26	6	2	0	0	0	0	
8098	990	142	26	6	2	0	0	0	0	0	
990	142	26	6	2	0	0	0	0	0	0	
142	26	6	2	0	0	0	0	0	0	0	
26	6	2	0	0	0	0	0	0	0	0	
6	2	0	0	0	0	0	0	0	0	0	
2	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	0	
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> Zxy(6,4,2,1,2)
0
>>> Zxy(6,4,2,0,0)
2
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> Z0Draw(6,4,2)
>>> Zcol(6,4,2,0)
2
>>> Zxy(8,6,2,0,0)
2
>>> Z0(3,2,2)
2
>>> Z0(6,3,2)
-2
>>> Zsq(6,3,2)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    Zsq(6,3,2)
NameError: name 'Zsq' is not defined
>>> Zsqu(6,3,2)
-2
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2)) + '\t';
	print(row);

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3)) + '\t';
	print(row);

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZBash(n,k,2)) + '\t';
	print(row);

	
0	
0	1	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZBash(n,k,3)) + '\t';
	print(row);

	
0	
0	1	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
>>> 
=== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ===
>>> Z0(6,3,2)
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    Z0(6,3,2)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 22, in Z0
    return Zcol(n,k,j,0) - sum(Zxy(n,k,j,0,i) for i in range(1,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 36, in Zcol
    return Zcol(n-x+1,k-x+1,j,1);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 35, in Zcol
    return Zsqu(n-1,k-1,j) - sum(Zcol(n-1,k-1,j,i) for i in range(1,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 45, in Zsqu
    return Scol(n-1,k-1,j)-Zcol(n-1,k-1,j,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 62, in Scol
    return 2*P(n-1,k-1,j,False,False) - Sx(n-1,k-1,j,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 9, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 7, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 6, in P
    if (wrap==False and cyclic==False): #Pj1
RecursionError: maximum recursion depth exceeded in comparison
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> Zsqu(6,4,2)
6
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	-4	
0	0	2	2	2	-12	
0	0	2	4	6	4	-60	
0	0	2	6	14	14	30	-332	
0	0	2	8	26	48	58	152	-2164	
0	0	2	10	42	118	218	282	818	-16028	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	0	-4	
0	0	2	2	2	-12	
0	0	2	4	6	4	-60	
0	0	2	6	14	14	30	-332	
0	0	2	8	26	48	58	152	-2164	
0	0	2	10	42	118	218	282	818	-16028	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	-2	
0	0	2	2	2	-14	
0	0	2	4	6	4	-58	
0	0	2	6	14	14	30	-334	
0	0	2	8	26	48	58	152	-2162	
0	0	2	10	42	118	218	282	818	-16030	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZBash(n,k,2))+'\t';
	print(row)

	
0	
0	1	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	-4	
0	2	4	2	-16	
0	2	6	8	6	-72	
0	2	8	18	20	34	-392	
0	2	10	32	62	72	182	-2496	
0	2	12	50	144	266	340	970	-18192	
0	2	14	72	278	772	1414	1920	5614	-149720	
>>> P(2,2,2,False,False)
-2
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	-2	
1	3	2	-10	
1	4	6	4	-44	
1	5	12	14	20	-232	
1	6	20	40	46	108	-1444	
1	7	30	88	164	206	576	-10344	
1	8	42	164	458	840	1130	3292	-83956	
1	9	56	274	1036	2850	5224	7250	21236	-762768	
>>> P(2,2,True,False)
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    P(2,2,True,False)
TypeError: P() missing 1 required positional argument: 'cyclic'
>>> P(2,2,2,True,False)
-2
>>> B(2,2,2)
0
>>> P(1,1,2,False,False)
1
>>> S0(1,1,2)
2
>>> P(2,2,3,True,False)
2
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	0	
1	5	12	14	20	0	
1	6	20	40	46	108	0	
1	7	30	88	164	206	576	0	
1	8	42	164	458	840	1130	3292	0	
1	9	56	274	1036	2850	5224	7250	21236	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	0	
1	5	12	14	20	0	
1	6	20	40	46	108	0	
1	7	30	88	164	206	576	0	
1	8	42	164	458	840	1130	3292	0	
1	9	56	274	1036	2850	5224	7250	21236	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	0	
1	6	18	36	36	84	0	
1	7	28	84	154	182	518	0	
1	8	40	160	448	816	1072	3152	0	
1	9	54	270	1026	2826	5166	7110	20898	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	0	
0	2	8	18	20	34	0	
0	2	10	32	62	72	182	0	
0	2	12	50	144	266	340	970	0	
0	2	14	72	278	772	1414	1920	5614	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	2	
0	0	2	6	14	14	30	-2	
0	0	2	8	26	48	58	152	2	
0	0	2	10	42	118	218	282	818	-2	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,2,0))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	2	
0	0	2	6	14	14	30	-2	
0	0	2	8	26	48	58	152	2	
0	0	2	10	42	118	218	282	818	-2	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,2,0))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	0	
0	0	2	6	14	14	30	0	
0	0	2	8	26	48	58	152	0	
0	0	2	10	42	118	218	282	818	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	0	
0	0	2	6	14	14	30	0	
0	0	2	8	26	48	58	152	0	
0	0	2	10	42	118	218	282	818	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	0	
0	2	8	18	20	34	0	
0	2	10	32	62	72	182	0	
0	2	12	50	144	266	340	970	0	
0	2	14	72	278	772	1414	1920	5614	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	0	
1	5	12	14	20	0	
1	6	20	40	46	108	0	
1	7	30	88	164	206	576	0	
1	8	42	164	458	840	1130	3292	0	
1	9	56	274	1036	2850	5224	7250	21236	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	0	
1	6	18	36	36	84	0	
1	7	28	84	154	182	518	0	
1	8	40	160	448	816	1072	3152	0	
1	9	54	270	1026	2826	5166	7110	20898	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	0	
0	0	2	4	10	0	
0	0	2	4	10	24	0	
0	0	2	4	10	24	58	0	
0	0	2	4	10	24	58	140	0	
0	0	2	4	10	24	58	140	338	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	0	
0	0	2	6	14	14	30	0	
0	0	2	8	26	48	58	152	0	
0	0	2	10	42	118	218	282	818	0	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	-2	
0	0	2	2	2	-14	
0	0	2	4	6	4	-58	
0	0	2	6	14	14	30	-334	
0	0	2	8	26	48	58	152	-2162	
0	0	2	10	42	118	218	282	818	-16030	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	-4	
0	2	4	2	-16	
0	2	6	8	6	-72	
0	2	8	18	20	34	-392	
0	2	10	32	62	72	182	-2496	
0	2	12	50	144	266	340	970	-18192	
0	2	14	72	278	772	1414	1920	5614	-149720	
>>> SBash(8,4,2)
168
>>> S0(8,4,2)
144
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	-2	
1	3	2	-10	
1	4	6	4	-44	
1	5	12	14	20	-232	
1	6	20	40	46	108	-1444	
1	7	30	88	164	206	576	-10344	
1	8	42	164	458	840	1130	3292	-83956	
1	9	56	274	1036	2850	5224	7250	21236	-762768	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	-2	
1	3	0	-6	
1	4	4	0	-24	
1	5	10	10	10	-140	
1	6	18	36	36	84	-960	
1	7	28	84	154	182	518	-7364	
1	8	40	160	448	816	1072	3152	-62784	
1	9	54	270	1026	2826	5166	7110	20898	-591876	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	-4	
0	0	2	4	-20	
0	0	2	4	10	-92	
0	0	2	4	10	24	-484	
0	0	2	4	10	24	58	-2980	
0	0	2	4	10	24	58	140	-21172	
0	0	2	4	10	24	58	140	338	-170892	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	0	6	
1	4	4	0	32	
1	5	10	10	10	180	
1	6	18	36	36	84	1212	
1	7	28	84	154	182	518	9240	
1	8	40	160	448	816	1072	3152	78704	
1	9	54	270	1026	2826	5166	7110	20898	741852	
>>> PBash(2,2,2,True,False)
0
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	4	
1	5	10	10	10	20	
1	6	18	36	36	84	126	
1	7	28	84	154	182	518	938	
1	8	40	160	448	816	1072	3152	7960	
1	9	54	270	1026	2826	5166	7110	20898	74988	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	0	
0	0	2	4	10	8	
0	0	2	4	10	24	56	
0	0	2	4	10	24	58	372	
0	0	2	4	10	24	58	140	2676	
0	0	2	4	10	24	58	140	338	21644	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	4	
1	5	10	10	10	20	
1	6	18	36	36	84	126	
1	7	28	84	154	182	518	938	
1	8	40	160	448	816	1072	3152	7960	
1	9	54	270	1026	2826	5166	7110	20898	74988	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	0	
0	0	2	4	10	8	
0	0	2	4	10	24	56	
0	0	2	4	10	24	58	372	
0	0	2	4	10	24	58	140	2676	
0	0	2	4	10	24	58	140	338	21644	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(O(n,k,2))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#199>", line 4, in <module>
    row+=str(O(n,k,2))+'\t';
NameError: name 'O' is not defined
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Oxy(n,k,2))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#201>", line 4, in <module>
    row+=str(Oxy(n,k,2))+'\t';
TypeError: Oxy() missing 2 required positional arguments: 'x' and 'y'
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	0	
0	0	2	4	10	8	
0	0	2	4	10	24	56	
0	0	2	4	10	24	58	372	
0	0	2	4	10	24	58	140	2676	
0	0	2	4	10	24	58	140	338	21644	
>>> O0(5,3,2)
4
>>> P(4,2,2,True,False)
4
>>> 2*sum(sum(Oxy(5,3,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1))
0
>>> sum(c(s,2)*O0(5-s+1,3-s+1,2) for s in range(2,2*2))
4
>>> 2*int((3-1)/(5-1))*P(5-1,3-1,2,True,False) - 2*sum(sum(Oxy(5,3,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + sum(c(s,2)*O0(5-s+1,3-s+1,2) for s in range(2,2*2))
4
>>> 2*int((3-1)/(5-1))*P(5-1,3-1,2,True,False)
0
>>> P(5-1,3-1,2,True,False)
4
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	0	
0	0	2	8	10	8	
0	0	2	12	30	40	56	
0	0	2	16	62	148	230	372	
0	0	2	20	106	376	946	1580	2676	
0	0	2	24	162	772	2754	7200	12434	21644	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	12	
0	0	2	12	30	40	86	
0	0	2	16	62	148	230	556	
0	0	2	20	106	376	946	1580	3998	
0	0	2	24	162	772	2754	7200	12434	32312	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	12	
0	0	2	12	30	40	86	
0	0	2	16	62	148	230	556	
0	0	2	20	106	376	946	1580	3998	
0	0	2	24	162	772	2754	7200	12434	32312	
>>> int(2*(5-1)/(5-1)*P(5-1,5-1,j,True,False)) - 2*sum(sum(Oxy(5,5,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + sum(c(s,j)*O0(5-s+1,5-s+1,2) for s in range(2,2*2));
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    int(2*(5-1)/(5-1)*P(5-1,5-1,j,True,False)) - 2*sum(sum(Oxy(5,5,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + sum(c(s,j)*O0(5-s+1,5-s+1,2) for s in range(2,2*2));
NameError: name 'j' is not defined
>>> int(2*(5-1)/(5-1)*P(5-1,5-1,j,True,False)) - 2*sum(sum(Oxy(5,5,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + sum(c(s,2)*O0(5-s+1,5-s+1,2) for s in range(2,2*2));
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    int(2*(5-1)/(5-1)*P(5-1,5-1,j,True,False)) - 2*sum(sum(Oxy(5,5,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + sum(c(s,2)*O0(5-s+1,5-s+1,2) for s in range(2,2*2));
NameError: name 'j' is not defined
>>> int(2*(5-1)/(5-1)*P(5-1,5-1,2,True,False)) - 2*sum(sum(Oxy(5,5,2,x,y) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + sum(c(s,2)*O0(5-s+1,5-s+1,2) for s in range(2,2*2));
12
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	4	
1	5	10	10	10	30	
1	6	18	36	60	84	186	
1	7	28	84	210	434	630	1400	
1	8	40	160	544	1552	3440	5168	11880	
1	9	54	270	1170	4338	13158	30366	47178	111942	
>>> P(3,3,2,False,False)
0
>>> S0(3,3,2)
-1
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	1	
0	2	0	
0	2	2	-1	
0	2	4	2	0	
0	2	6	8	6	11	
0	2	8	18	28	34	72	
0	2	10	32	78	152	214	471	
0	2	12	50	168	466	1012	1506	3440	
0	2	14	72	310	1132	3390	7760	11990	28315	
>>> P(2,2,2,False,False)
0
>>> S0(2,2,2)
0
>>> Scol(2,2,2)
1
>>> SBash(1,1,2)
1
>>> SBash(2,2,2)
0
>>> 2*P(1,1,2,False,False)
2
>>> PBash(1,1,2,False,False)
1
>>> Sx(1,1,2,0)
1
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZBash(n,k,2))+'\t';
	print(row)

	
0	
0	1	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZXyBash(n,k,2,0,0)+'\t';
	print(row)
			 
SyntaxError: invalid syntax
>>> 
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZXyBash(n,k,2,0,0))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	3	
0	0	2	2	6	2	
0	0	2	4	14	24	30	
0	0	2	6	26	70	132	126	
0	0	2	8	42	156	448	852	924	
0	0	2	10	62	294	1136	3280	6334	6724	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	1	
0	0	2	2	6	4	
0	0	2	4	14	24	28	
0	0	2	6	26	70	132	128	
0	0	2	8	42	156	448	852	922	
0	0	2	10	62	294	1136	3280	6334	6726	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	-1	
0	0	2	0	1	
0	0	2	2	2	0	
0	0	2	4	6	4	12	
0	0	2	6	14	22	30	61	
0	0	2	8	26	64	130	184	411	
0	0	2	10	42	142	402	882	1322	3030	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> Zcol(3,3,0,0)
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    Zcol(3,3,0,0)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 40, in Zcol
    return Zcol(n-x+1,k-x+1,j,1);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 39, in Zcol
    return Zsqu(n-1,k-1,j) - sum(Zcol(n-1,k-1,j,i) for i in range(1,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 47, in Zsqu
    return Scol(n-1,k-1,j)-Zcol(n-1,k-1,j,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 66, in Scol
    return 2*P(n-1,k-1,j,False,False) - Sx(n-1,k-1,j,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 17, in P
    return n*(P(n-1,k-1,j,False,False)-Sx(n-1,k-1,j,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 59, in Sx
    return S0(n-x,k-x,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 56, in S0
    return 2*P(n-1,k-1,j,False,False) - Scol(n-1,k-1,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 6, in P
    if (wrap==False and cyclic==False): #Pj1
RecursionError: maximum recursion depth exceeded in comparison
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> 
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	-1	
0	0	2	0	1	
0	0	2	2	2	0	
0	0	2	4	6	4	12	
0	0	2	6	14	22	30	61	
0	0	2	8	26	64	130	184	411	
0	0	2	10	42	142	402	882	1322	3030	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,False,True))+'\t';
	print(row)

	
0	
0	1	
0	2	2	
0	3	6	0	
0	4	12	8	4	
0	5	20	40	80	90	
0	6	30	96	276	516	528	
0	7	42	182	700	1988	3780	3997	
0	8	56	304	1472	5648	16304	31408	33520	
0	9	72	468	2736	13248	51408	149688	290772	312786	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,False,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	12	16	
1	5	20	42	88	80	
1	6	30	96	288	540	516	
1	7	42	180	712	2040	3936	3794	
1	8	56	300	1480	5720	16668	32368	31456	
1	9	72	462	2736	13320	52032	152418	297792	290970	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	

=============================================================== RESTART: Shell ===============================================================
>>> 
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,True))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#271>", line 4, in <module>
    row+=str(PBash(n,k,3,True,True))+'\t';
NameError: name 'PBash' is not defined
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
Traceback (most recent call last):
  File "<pyshell#275>", line 4, in <module>
    row+=str(Z0(n,k,2))+'\t';
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 22, in Z0
    return Zcol(n,k,j,0) - sum(Zxy(n,k,j,0,i) for i in range(1,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 32, in Zcol
    return Zcol(n-x+1,k-x+1,j,1);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 31, in Zcol
    return Zsqu(n-1,k-1,j) - sum(Zcol(n-1,k-1,j,i) for i in range(1,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 37, in Zsqu
    return Scol(n-1,k-1,j)-Zcol(n-1,k-1,j,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 50, in Scol
    return 2*P(n-1,k-1,j,False,False) - Sx(n-1,k-1,j,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 11, in P
    return P(n,k,j,True,False)+B(n,k,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 68, in B
    return sum(sum(Oxy(n,k,j,x,y) for y in range(j-2-x,j-1)) for x in range(0,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 68, in <genexpr>
    return sum(sum(Oxy(n,k,j,x,y) for y in range(j-2-x,j-1)) for x in range(0,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 68, in <genexpr>
    return sum(sum(Oxy(n,k,j,x,y) for y in range(j-2-x,j-1)) for x in range(0,j-1));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 65, in Oxy
    return O0(n-x-y,k-x-y,j);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 60, in O0
    return int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,False)) - 2*sum(sum(Oxy(n,k,j,x,y) for y in range(1-x,j-1-x)) for x in range(0,j-1)) + sum(c(s,j)*O0(n-s+1,k-s+1,j) for s in range(2,2*j));
ZeroDivisionError: division by zero
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> Z0Draw(6,6,2)
>>> Z0Draw(4,4,2)
>>> Zcol(3,3,2,0) - sum(Zxy(3,3,2,0,i) for i in range(1,2-1));
-2
>>> Zcol(3,3,2,0)
-2
>>> sum(Zxy(3,3,2,0,i) for i in range(1,2-1))
0
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,2,0))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> Zcol(4,4,2,1)
-2
>>> Zsqu(3,3,2)-sum(Zcol(3,3,2,i) for i in range(1,1))
-2
>>> Zsqu(3,3,2)
-2
>>> Scol(2,2,2)
0
>>> Zcol(2,2,2,0)
2
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,2,0))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> Zcol(2,2,3,0)
2
>>> ZXyBash(2,2,3,1,0)
0
>>> 
============================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,2,0))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(Scol(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(O0(n,k,j))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#313>", line 4, in <module>
    row+=str(O0(n,k,j))+'\t';
NameError: name 'j' is not defined
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(B(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
Traceback (most recent call last):
  File "<pyshell#319>", line 4, in <module>
    row+=str(U0(n,k,2))+'\t';
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 77, in U0
    return int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1)) + 2*Zxy(n-1,k-1,j,0,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  [Previous line repeated 1020 more times]
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 6, in P
    if k>n or n<0 or k<0:
RecursionError: maximum recursion depth exceeded in comparison
>>> int(2*(0-1)/(2-1)*P(2-1,0-1,2,True,True))
0
>>> 2*Zxy(2-1,0-1,2,0,2-2)
0
>>> for x in range(0,j-1):
	for y in range(1-x,j-1-x):
		print(x,y)

		
Traceback (most recent call last):
  File "<pyshell#325>", line 1, in <module>
    for x in range(0,j-1):
NameError: name 'j' is not defined
>>> for x in range(0,j-1):
	for y in range(1-x,2-1-x):
		print(x,y)

		
Traceback (most recent call last):
  File "<pyshell#327>", line 1, in <module>
    for x in range(0,j-1):
NameError: name 'j' is not defined
>>> for x in range(0,2-1):
	for y in range(1-x,2-1-x):
		print(x,y)

		
>>> U0(2,0,2)
0
>>> U0(2,1,2)
0
>>> 
>>> U0(2,2,2)
Traceback (most recent call last):
  File "<pyshell#333>", line 1, in <module>
    U0(2,2,2)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 77, in U0
    return int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1)) + 2*Zxy(n-1,k-1,j,0,j-2);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  [Previous line repeated 1020 more times]
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 6, in P
    if k>n or n<0 or k<0:
RecursionError: maximum recursion depth exceeded in comparison
>>> int(2*(2-1)/(2-1)*P(2-1,2-1,2,True,True))
Traceback (most recent call last):
  File "<pyshell#334>", line 1, in <module>
    int(2*(2-1)/(2-1)*P(2-1,2-1,2,True,True))
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 15, in P
    return P(n,k,j,True,True) + sum(sum((Uxy(n,k,j,x,y)+Zxy(n,k,j,x,y)) for y in range(j-2-x,j-1)) for x in range(0,j-1)) + sum(sum((sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-x)) + sum(Zxy(n-x-y,k-x-y,j,0,d) for d in range(j-x-y-2,j-1-y))) for y in range(0,j-2-x)) for x in range(0,j-2));
  [Previous line repeated 1021 more times]
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 6, in P
    if k>n or n<0 or k<0:
RecursionError: maximum recursion depth exceeded in comparison
>>> 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1)) + 2*Zxy(n-1,k-1,j,0,j-2);
Traceback (most recent call last):
  File "<pyshell#335>", line 1, in <module>
    2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1)) + 2*Zxy(n-1,k-1,j,0,j-2);
NameError: name 'j' is not defined
>>> 2*sum(sum((Uxy(2,2,2,x,y)-sum(Zxy(2-x-1,2-x-1,j,2,d-1) for d in range(2-x-y-1,2-x-1))-sum(Zxy(2-y-1,2-y-1,2,x,d-1) for d in range(2-x-y-1,2-y-1))) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + 2*Zxy(2-1,2-1,2,0,2-2);
0
>>> 
================================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =================================
>>> int(2*(2-1)/(2-1)*P(2-1,2-1,2,True,True))
2
>>> U0(2,2,2)
2
>>> UBash(2,2,2)
0
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	4	
0	0	2	-4	-12	
0	0	2	0	12	0	
0	0	2	4	16	4	20	
0	0	2	8	32	60	128	80	
0	0	2	12	60	188	504	828	740	
0	0	2	16	100	436	1568	4124	7256	6256	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> U0(3,3,2)
4
>>> 
================================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =================================
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	4	
0	0	2	-4	-12	
0	0	2	0	12	0	
0	0	2	4	16	4	20	
0	0	2	8	32	60	128	80	
0	0	2	12	60	188	504	828	740	
0	0	2	16	100	436	1568	4124	7256	6256	
>>> int(2*(3-1)/(4-1)*P(4-1,3-1,2,True,True))
-8
>>>  - 2*sum(sum((Uxy(4,3,2,x,y)-sum(Zxy(4-x-1,3-x-1,2,y,d-1) for d in range(2-x-y-1,2-x-1))-sum(Zxy(4-y-1,3-y-1,2,x,d-1) for d in range(2-x-y-1,2-y-1))) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + 2*Zxy(4-1,3-1,2,0,2-2);
 
SyntaxError: unexpected indent
>>> -2*sum(sum((Uxy(4,3,2,x,y)-sum(Zxy(4-x-1,3-x-1,2,y,d-1) for d in range(2-x-y-1,2-x-1))-sum(Zxy(4-y-1,3-y-1,2,x,d-1) for d in range(2-x-y-1,2-y-1))) for y in range(1-x,2-1-x)) for x in range(0,2-1)) + 2*Zxy(4-1,3-1,2,0,2-2);
4
>>> 2*Zxy(4-1,3-1,2,0,2-2)
4
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,3,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
>>> 
================================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =================================
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	6	
1	4	4	0	24	
1	5	10	10	10	150	
1	6	18	36	60	84	1020	
1	7	28	84	210	434	630	7826	
1	8	40	160	544	1552	3440	5168	66704	
1	9	54	270	1170	4338	13158	30366	47178	628830	
>>> 
================================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =================================
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
>>> 
================================= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =================================
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,False))+'\t';
	print(row)

	
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	4	
0	0	2	-4	-12	
0	0	2	0	12	0	
0	0	2	4	16	4	20	
0	0	2	8	32	60	128	80	
0	0	2	12	60	188	504	828	740	
0	0	2	16	100	436	1568	4124	7256	6256	
>>> UBash(2,2,2)
0
>>> UBash(2,2,3)
2
>>> int(2*(3-1)/(4-1)*P(4-1,3-1,2,True,True))
-8
>>> P(4-1,3-1,2,True,True)
-6
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	-6	-6	
1	4	-4	8	0	
1	5	0	10	0	10	
1	6	6	24	36	72	36	
1	7	14	56	140	322	448	350	
1	8	24	112	384	1152	2576	3936	2992	
1	9	36	198	864	3294	10116	23598	36936	29178	
>>> P(3,3,2,False,False)
0
>>> Z0(3,3,2)
0
>>> Zxy(3,3,2,0,0)
0
>>> Zsqu(2,2,2)
2
>>> Z0(2,2,2)
0
>>> Zcol(2,2,2,0)
0
>>> ZBash(2,2,3)
2
>>> 
===== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ====
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(Zcol(n,k,2,0))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(Zsqu(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(S0(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(Scol(n,k,2,0))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#391>", line 4, in <module>
    row+=str(Scol(n,k,2,0))+'\t';
TypeError: Scol() takes 3 positional arguments but 4 were given
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(Scol(n,k,2))+'\t';
	print(row)

	
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	-6	0	
1	4	-4	8	0	
1	5	0	10	0	10	
1	6	6	24	36	72	36	
1	7	14	56	140	322	448	350	
1	8	24	112	384	1152	2576	3936	2992	
1	9	36	198	864	3294	10116	23598	36936	29178	
>>> PBash(9,9,2,True,True)
27954
>>> P(3,2,2,True,True)
-6
>>> P(2,1,2,False,False)
2
>>> S0(2,1,2)
2
>>> Zsqu(2,1,2)
0
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(PBash(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	0	0	10	
1	6	18	12	24	60	36	
1	7	28	42	112	280	420	322	
1	8	40	96	336	1040	2400	3696	2832	
1	9	54	180	792	3060	9540	22428	35280	27954	
>>> P(3,2,2,True,True)
-6
>>> P(2,1,2,False,False)
2
>>> Zxy(2,1,2,0,0)
0
>>> Zsqu(2,1,2)
0
>>> Z0(2,1,2)
0
>>> Zxy(3,2,2,0,0)
2
>>> 
===== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ====
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	8	0	
1	5	10	10	0	10	
1	6	18	24	36	72	36	
1	7	28	56	140	322	448	350	
1	8	40	112	384	1152	2576	3936	2992	
1	9	54	198	864	3294	10116	23598	36936	29178	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
>>> P(4,3,2,True,True)
8
>>> P(3,2,2,False,False)
2
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	0	0	10	
1	6	18	12	24	60	36	
1	7	28	42	112	280	420	322	
1	8	40	96	336	1040	2400	3696	2832	
1	9	54	180	792	3060	9540	22428	35280	27954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(P(n,k,2,False,False)-2*ZxyBash(n,k,2,0,0)-Zsqu(n-1,k-1,2)+Z0(n-1,k-1,2));
		row+=str(Pcalc)+'\t';
	print(row)

	
0	
1	1	
2	4	0	
3	9	-6	0	
4	16	8	16	8	
5	25	40	70	80	70	
6	36	96	240	468	696	492	
7	49	182	616	1708	3766	5600	4242	
8	64	304	1312	4784	14400	33008	51040	39760	
9	81	468	2466	11232	43434	135972	322218	512712	410598	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(PBash(n,k,2,False,False)-2*ZxyBash(n,k,2,0,0)-ZBash(n-1,k-1,2)+Z0(n-1,k-1,2));
		row+=str(Pcalc)+'\t';
	print(row)

	
0	
1	1	
2	4	-2	
3	9	-6	0	
4	16	8	16	8	
5	25	40	70	80	70	
6	36	96	240	468	696	492	
7	49	182	616	1708	3766	5600	4242	
8	64	304	1312	4784	14400	33008	51040	39760	
9	81	468	2466	11232	43434	135972	322218	512712	410598	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = n*(PBash(n,k,3,False,False)-2*ZxyBash(n,k,3,0,0)-ZBash(n-1,k-1,3)+Z0(n-1,k-1,3));
		row+=str(Pcalc)+'\t';
	print(row)

	
0	
1	1	
2	4	2	
3	9	6	6	
4	16	32	80	64	
5	25	80	250	420	400	
6	36	156	624	1716	3300	3156	
7	49	266	1316	4984	14434	27776	26754	
8	64	416	2464	11856	46064	134048	260336	252896	
9	81	612	4230	24660	120402	470016	1376892	2689668	2627964	
>>> ZxyBash(11,7,4,0,2)
310
>>> SBash(11-2-1,7-2-1,4)-ZXyBash(11-1,7-1,4,2,2)
310
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,4,True,True);
		row+=str(Pbash)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,4,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	24	
1	5	20	60	80	70	
1	6	30	120	312	660	648	
1	7	42	210	784	2380	4704	4704	
1	8	56	336	1616	6480	19296	38304	38000	
1	9	72	504	2952	14760	58752	175392	349200	347580	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,3,True,True);
		row+=str(Pbash)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,3,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	8	0	
1	5	20	40	80	90	
1	6	30	96	276	516	468	
1	7	42	182	700	1988	3780	3612	
1	8	56	304	1472	5648	16304	31408	30288	
1	9	72	468	2736	13248	51408	149688	290772	282528	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,5,True,True);
		row+=str(Pbash)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	24	
1	5	20	60	120	110	
1	6	30	120	360	660	708	
1	7	42	210	840	2450	4956	4928	
1	8	56	336	1680	6640	19968	39872	39792	
1	9	72	504	3024	15030	60156	180306	360288	359946	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,5,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	24	
1	5	20	60	100	100	
1	6	30	120	336	660	648	
1	7	42	210	812	2422	4872	4858	
1	8	56	336	1648	6576	19744	39424	39392	
1	9	72	504	2988	14922	59688	178902	357480	357210	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,5,True,True);
		row+=str(Pbash)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	24	
1	5	20	60	120	110	
1	6	30	120	360	660	708	
1	7	42	210	840	2450	4956	4928	
1	8	56	336	1680	6640	19968	39872	39792	
1	9	72	504	3024	15030	60156	180306	360288	359946	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,5,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	24	
1	5	20	60	120	120	
1	6	30	120	360	648	636	
1	7	42	210	840	2436	4956	4942	
1	8	56	336	1680	6624	19952	39824	39760	
1	9	72	504	3024	15012	60120	180180	360036	359820	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,2,True,True);
		row+=str(Pbash)+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	0	0	10	
1	6	18	12	24	60	36	
1	7	28	42	112	280	420	322	
1	8	40	96	336	1040	2400	3696	2832	
1	9	54	180	792	3060	9540	22428	35280	27954	
>>> 
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,2,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	-12	0	
1	4	-12	0	0	
1	5	-10	-10	-10	10	
1	6	-6	-12	-12	36	12	
1	7	0	0	14	126	210	182	
1	8	8	32	128	528	1360	2224	1744	
1	9	18	90	414	1782	5922	14490	23382	18954	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,2,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	-10	-10	10	
1	6	18	-12	-12	36	12	
1	7	28	0	14	126	210	182	
1	8	40	32	128	528	1360	2224	1744	
1	9	54	90	414	1782	5922	14490	23382	18954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	0	
0	0	2	8	0	0	
0	0	2	12	-8	-12	20	
0	0	2	16	-4	-4	68	32	
0	0	2	20	12	44	224	420	404	
0	0	2	24	40	180	788	2300	4260	3760	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0Bash(n,k,2))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#456>", line 4, in <module>
    row+=str(U0Bash(n,k,2))+'\t';
NameError: name 'U0Bash' is not defined
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,2,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	-10	-10	10	
1	6	18	-12	-12	36	12	
1	7	28	0	14	126	210	182	
1	8	40	32	128	528	1360	2224	1744	
1	9	54	90	414	1782	5922	14490	23382	18954	
>>> P(4,2,2,False,False)
6
>>> 2*Zxy(5,3,2,0,2-2)
4
>>> 2*S0(4,2,2)-2*Z0(4,2,2)
4
>>> #sum(sum(Zxy(n-1,k-1,j,x,y) for y in range(j-3-x,j-1)) for x in range(0,j-1))
>>> sum(sum(Zxy(5-1,3-1,2,x,y) for y in range(2-3-x,2-1)) for x in range(0,2-1))
4
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> sum(sum(Zxy(5-1,3-1,2,x,y) for y in range(2-3-x,2-1)) for x in range(0,2-1))
2
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,2,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	0	0	10	
1	6	18	12	24	60	36	
1	7	28	42	112	280	420	322	
1	8	40	96	336	1040	2400	3696	2832	
1	9	54	180	792	3060	9540	22428	35280	27954	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = P(n,k,2,True,True);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	4	
0	0	2	-4	0	
0	0	2	0	0	0	
0	0	2	4	4	4	20	
0	0	2	8	20	44	108	80	
0	0	2	12	48	156	444	780	684	
0	0	2	16	88	388	1428	3860	6836	5936	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	0	
0	0	2	8	0	0	
0	0	2	12	4	4	20	
0	0	2	16	20	44	108	80	
0	0	2	20	48	156	444	780	684	
0	0	2	24	88	388	1428	3860	6836	5936	
>>> P(10,8,3,False,True)
1536180
>>> PBash(10,8,3,False,True)
1545024
>>> P(10,8,2,False,True)
272810
>>> PBash(10,8,2,False,True)
284304
>>> U0(4,3,2)
4
>>> int(2*(3-1)/(4-1)*P(4-1,3-1,2,True,True))
0
>>> 2*sum(sum((Uxy(4,3,2,x,y)-sum(Zxy(4-x-1,3-x-1,2,y,d-1) for d in range(2-x-y-1,2-x-1))-sum(Zxy(4-y-1,3-y-1,2,x,d-1) for d in range(2-x-y-1,2-y-1))) for y in range(1-x,2-1-x)) for x in range(0,2-1))
0
>>> 2*Zxy(4-1,3-1,2,0,2-2)
4
>>> UBash(4,4,2)
0
>>> UBash(4,3,2)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	4	
0	0	2	8	10	
0	0	2	12	22	24	
0	0	2	16	34	56	78	
0	0	2	20	58	128	246	260	
0	0	2	24	94	296	746	1336	1290	
0	0	2	28	142	608	2106	5524	9814	8816	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	8	0	
0	0	2	12	22	0	
0	0	2	16	34	56	20	
0	0	2	20	58	128	246	120	
0	0	2	24	94	296	746	1336	952	
0	0	2	28	142	608	2106	5524	9814	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	8	
0	0	2	0	18	
0	0	2	4	6	44	
0	0	2	8	18	16	126	
0	0	2	12	42	88	150	376	
0	0	2	16	78	256	650	1104	1570	
0	0	2	20	126	568	2010	5292	9254	9492	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	0	
1	0	0	
1	0	0	0	
1	0	0	0	0	
1	0	0	0	0	0	
1	0	0	0	0	0	0	
1	0	0	0	0	0	0	0	
1	0	0	0	0	0	0	0	0	
1	0	0	0	0	0	0	0	0	0	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	0	0	
0	0	0	0	0	0	
0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	
0	0	0	0	0	0	0	0	0	0	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
0	
0	1	
0	2	2	
0	3	-6	0	
0	4	-4	0	0	
0	5	0	0	0	10	
0	6	6	12	24	60	36	
0	7	14	42	112	280	420	322	
0	8	24	96	336	1040	2400	3696	2832	
0	9	36	180	792	3060	9540	22428	35280	27954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	8	
0	0	2	0	18	
0	0	2	4	6	44	
0	0	2	8	18	16	126	
0	0	2	12	42	88	150	376	
0	0	2	16	78	256	650	1104	1570	
0	0	2	20	126	568	2010	5292	9254	9492	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> P(0,0,2,False,False)
1
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(9,2)
P1 correct
P2 correct
P3 error
P4 correct
Z0 error
S0 correct
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(O0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
>>> verify(9,2)
P1 correct
P2 correct
P3 error
P4 correct
Z0 error
S0 correct
O0 correct
U0 error
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	1	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
1	
0	1	
0	0	1	
0	0	2	-1	
0	0	2	0	1	
0	0	2	2	2	-1	
0	0	2	4	6	4	5	
0	0	2	6	14	22	30	19	
0	0	2	8	26	64	130	184	137	
0	0	2	10	42	142	402	882	1322	999	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
1	
0	1	
0	0	1	
0	0	2	-1	
0	0	2	0	1	
0	0	2	2	2	-1	
0	0	2	4	6	4	5	
0	0	2	6	14	22	30	19	
0	0	2	8	26	64	130	184	137	
0	0	2	10	42	142	402	882	1322	999	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	0	2	
0	0	2	2	2	-2	
0	0	2	4	6	4	6	
0	0	2	6	14	22	30	18	
0	0	2	8	26	64	130	184	138	
0	0	2	10	42	142	402	882	1322	998	
>>> ZBash(8.8.3)
SyntaxError: invalid syntax
>>> ZBash(8,8,3)
1086
>>> SBash(8,8,3)
7052
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> SXBash(8,8,3,1)
8014
>>> verify(9,2)
P1 correct
P2 correct
P3 error
P4 correct
Z0 error
Z1[] error
Zsqu error
S0 correct
Scol correct
O0 correct
U0 error
>>> verify(9,3)
P1 correct
P2 correct
P3 error
P4 error
Z0 error
Z1[] error
Zsqu error
S0 correct
Scol correct
O0 correct
U0 error
>>> Z0Bash(2,2,2)
0
>>> Z0Bash(2,2,3)
0
>>> ZBash(2,2,3)
2
>>> ZBash(2,2,2)
0
>>> Z0Bash(2,2,4)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(9,2)
P1 correct
P2 correct
P3 error
P4 error
Z0 error
Z1[] error
Zsqu error
S0 correct
Scol correct
O0 correct
U0 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(9,2)
P1 	 correct
P2 	 correct
P3 	 error
P4 	 error
Z0 	 error
Z1[] 	 error
Zsqu 	 error
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> Zsqu(2,2,3)
2
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(9,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(2,8)
Traceback (most recent call last):
  File "<pyshell#547>", line 1, in <module>
    printAll(2,8)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 72, in printAll
    print(headers(triangle));
TypeError: 'list' object is not callable
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(2,8)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
P2(n, k)
0	
0	1	
0	2	-2	
0	3	0	0	
0	4	4	0	0	
0	5	10	10	10	10	
0	6	18	36	60	84	60	
0	7	28	84	210	434	630	462	
P3(n, k)
0	
0	1	
0	2	2	
0	3	-6	0	
0	4	-4	0	0	
0	5	0	0	0	10	
0	6	6	12	24	60	36	
0	7	14	42	112	280	420	322	
P4(n, k)
0	
0	1	
0	2	4	
0	3	-2	8	
0	4	0	0	18	
0	5	4	6	8	54	
0	6	10	24	48	80	166	
0	7	18	60	168	390	600	718	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	8	
0	0	2	0	18	
0	0	2	4	6	44	
0	0	2	8	18	16	126	
0	0	2	12	42	88	150	376	
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(9,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> printAll(2,8)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
P2(n, k)
0	
0	1	
0	2	-2	
0	3	0	0	
0	4	4	0	0	
0	5	10	10	10	10	
0	6	18	36	60	84	60	
0	7	28	84	210	434	630	462	
P3(n, k)
0	
0	1	
0	2	2	
0	3	-6	0	
0	4	-4	0	0	
0	5	0	0	0	10	
0	6	6	12	24	60	36	
0	7	14	42	112	280	420	322	
P4(n, k)
0	
0	1	
0	2	4	
0	3	-2	8	
0	4	0	0	18	
0	5	4	6	8	54	
0	6	10	24	48	80	166	
0	7	18	60	168	390	600	718	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	8	
0	0	2	0	18	
0	0	2	4	6	44	
0	0	2	8	18	16	126	
0	0	2	12	42	88	150	376	
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> n=2,k=2,j=2
SyntaxError: cannot assign to literal
>>> n,k,j=2
Traceback (most recent call last):
  File "<pyshell#557>", line 1, in <module>
    n,k,j=2
TypeError: cannot unpack non-iterable int object
>>> n=2;k=2;j=2;
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
2
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
2
>>> t1
0
>>> t2
0
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> UBash(2,2,3)
2
>>> UBash(2,2,2)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(9,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(2,9)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
P2(n, k)
0	
0	1	
0	2	-2	
0	3	0	0	
0	4	4	0	0	
0	5	10	10	10	10	
0	6	18	36	60	84	60	
0	7	28	84	210	434	630	462	
0	8	40	160	544	1552	3440	5168	3920	
P3(n, k)
0	
0	1	
0	2	2	
0	3	-6	0	
0	4	-4	0	0	
0	5	0	0	0	10	
0	6	6	12	24	60	36	
0	7	14	42	112	280	420	322	
0	8	24	96	336	1040	2400	3696	2832	
P4(n, k)
0	
0	1	
0	2	2	
0	3	-2	4	
0	4	0	0	8	
0	5	4	6	8	30	
0	6	10	24	48	80	108	
0	7	18	60	168	390	600	578	
0	8	28	120	440	1360	3180	4984	4200	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	4	
0	0	2	0	8	
0	0	2	4	6	20	
0	0	2	8	18	16	68	
0	0	2	12	42	88	150	236	
0	0	2	16	78	256	650	1104	1232	
0
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	8	
0	0	2	0	18	
0	0	2	4	6	44	
0	0	2	8	18	16	126	
0	0	2	12	42	88	150	376	
0	0	2	16	78	256	650	1104	1570	
0	0	2	20	126	568	2010	5292	9254	9492	
>>> n=2;k=2;j=2;
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
2
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> n=3;k=3;j=2;
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
4
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
4
>>> t1
0
>>> t2
>>> t2
0
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	4	
0	0	2	0	10	
0	0	2	4	6	24	
0	0	2	8	18	16	78	
0	0	2	12	42	88	150	260	
0	0	2	16	78	256	650	1104	1290	
0	0	2	20	126	568	2010	5292	9254	8816	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
0	
0	1	
0	2	-2	
0	3	0	0	
0	4	4	0	0	
0	5	10	10	10	10	
0	6	18	36	60	84	60	
0	7	28	84	210	434	630	462	
0	8	40	160	544	1552	3440	5168	3920	
0	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
0	
0	1	
0	2	0	
0	3	-6	0	
0	4	-4	0	0	
0	5	0	0	0	10	
0	6	6	12	24	60	36	
0	7	14	42	112	280	420	322	
0	8	24	96	336	1040	2400	3696	2832	
0	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
0	
0	1	
0	2	0	
0	3	-2	0	
0	4	0	0	0	
0	5	4	6	8	10	
0	6	10	24	48	80	60	
0	7	18	60	168	390	600	462	
0	8	28	120	440	1360	3180	4984	3920	
0	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
0
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
0	
0	1	
0	2	-2	
0	3	0	0	
0	4	4	0	0	
0	5	10	10	10	10	
0	6	18	36	60	84	60	
0	7	28	84	210	434	630	462	
0	8	40	160	544	1552	3440	5168	3920	
0	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
0	
0	1	
0	2	0	
0	3	-6	0	
0	4	-4	0	0	
0	5	0	0	0	10	
0	6	6	12	24	60	36	
0	7	14	42	112	280	420	322	
0	8	24	96	336	1040	2400	3696	2832	
0	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
0	
0	1	
0	2	0	
0	3	-2	0	
0	4	0	0	0	
0	5	4	6	8	10	
0	6	10	24	48	80	60	
0	7	18	60	168	390	600	462	
0	8	28	120	440	1360	3180	4984	3920	
0	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row += str(PBash(n,k,2,False,True)) + '\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	0	0	
1	5	12	6	8	10	
1	6	20	24	48	80	60	
1	7	30	60	168	390	600	462	
1	8	42	120	440	1360	3180	4984	3920	
1	9	56	210	960	3770	11952	28602	45856	36954	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 error
P2 	 error
P3 	 error
P4 	 error
Z0 	 error
Z1[] 	 error
Zsqu 	 error
S0 	 error
Scol 	 error
O0 	 error
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	-2	0	
1	4	0	0	0	
1	5	4	6	8	10	
1	6	10	24	48	80	60	
1	7	18	60	168	390	600	462	
1	8	28	120	440	1360	3180	4984	3920	
1	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row += str(PBash(n,k,2,False,True)) + '\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	0	0	
1	5	12	6	8	10	
1	6	20	24	48	80	60	
1	7	30	60	168	390	600	462	
1	8	42	120	440	1360	3180	4984	3920	
1	9	56	210	960	3770	11952	28602	45856	36954	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	-2	0	
1	4	0	0	0	
1	5	4	6	8	10	
1	6	10	24	48	80	60	
1	7	18	60	168	390	600	462	
1	8	28	120	440	1360	3180	4984	3920	
1	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> PBash(2,2,2,True,False)
0
>>> PBash(2,2,3,True,False)
2
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 error
P4 	 error
Z0 	 correct
Z1[] 	 error
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> ZXyBash(2,2,2,0,0)
0
>>> ZXyBash(2,2,3,1,0)
0
>>> #Zcol(2,2,j)=0 if single=0
>>> ZXyBash(2,2,4,2,0)
0
>>> #find Zcol(2,2,j) if single=1
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZXyBash(n,k,3,1,0))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	2	2	
0	0	2	4	6	6	
0	0	2	6	16	30	26	
0	0	2	8	30	84	156	146	
0	0	2	10	48	182	518	984	940	
0	0	2	12	70	336	1292	3728	7186	6928	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,3,0))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	2	0	
0	0	2	4	6	8	
0	0	2	6	16	30	26	
0	0	2	8	30	84	156	144	
0	0	2	10	48	182	518	984	942	
0	0	2	12	70	336	1292	3728	7186	6928	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZXyBash(n,k,3,1,1))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Zcol(n,k,3,1))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	0	2	
0	0	0	2	0	
0	0	0	2	2	0	
0	0	0	2	4	6	8	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	144	
0	0	0	2	10	48	182	518	984	942	
>>> #Zcol(3,3,j)=0 if single=1
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZXyBash(n,k,4,1,1))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	8	
0	0	0	2	6	16	34	32	
0	0	0	2	8	30	92	180	176	

================================================================ RESTART: Shell ===============================================================
>>> 
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> Zcol(2,2,2,0)
0
>>> verify(8,2)
P1 	 correct

P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 error
Zsqu 	 error
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 error
P4 	 error
Z0 	 correct
Z1[] 	 error
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,8)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	90	
1	6	30	84	264	480	408	
1	7	42	168	672	1890	3612	3500	
P4(n, k)
1	
1	1	
1	2	2	
1	3	6	10	
1	4	12	12	18	
1	5	20	42	88	126	
1	6	30	96	288	528	458	
1	7	42	180	712	2028	3938	4036	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	6	8	
0	0	2	4	14	24	18	
0	0	2	6	26	70	132	126	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	2	
0	0	0	2	0	
0	0	0	2	2	0	
0	0	0	2	4	6	8	
0	0	0	2	6	16	30	26	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	2	
0	0	2	4	0	
0	0	2	6	8	8	
0	0	2	8	20	36	34	
0	0	2	10	36	100	186	170	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	18	
0	0	2	8	12	0	
0	0	2	12	40	112	236	
0	0	2	16	80	306	658	436	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(ZBash(n,k,4))+'\t';
	print(row)

	
0	
0	1	
0	0	2	
0	0	2	2	
0	0	2	4	2	
0	0	2	6	12	10	
0	0	2	8	24	44	44	
0	0	2	10	40	116	228	224	
0	0	2	12	60	236	700	1384	1368	
0	0	2	14	84	416	1652	4920	9770	9700	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,4))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	6	
0	0	2	4	14	28	26	
0	0	2	6	26	78	152	150	
0	0	2	8	42	168	496	984	976	
0	0	2	10	62	310	1228	3664	7284	7240	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	-2	0	
1	4	0	0	0	
1	5	4	6	8	10	
1	6	10	24	48	80	60	
1	7	18	60	168	390	600	462	
1	8	28	120	440	1360	3180	4984	3920	
1	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	-3	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	-1	
1	2	0	
1	3	-2	4	
1	4	0	0	8	
1	5	4	6	8	30	
1	6	10	24	48	80	108	
1	7	18	60	168	390	600	578	
1	8	28	120	440	1360	3180	4984	4200	
1	9	40	210	960	3770	11952	28602	45856	37630	
Z0(n, k)
0	
0	2	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	4	
0	0	2	0	8	
0	0	2	4	6	20	
0	0	2	8	18	16	68	
0	0	2	12	42	88	150	236	
0	0	2	16	78	256	650	1104	1232	
0	0	2	20	126	568	2010	5292	9254	8676	
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	-10	
1	3	6	-6	
1	4	12	0	8	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	-2	
1	3	6	-4	
1	4	12	12	-14	
1	5	20	42	88	70	
1	6	30	96	288	528	420	
1	7	42	180	712	2028	3938	3878	
1	8	56	300	1480	5708	16658	32272	30910	
1	9	72	462	2736	13308	52010	152276	297746	291916	
Z0(n, k)
0	
0	2	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	-10	
0	0	2	4	6	
0	0	2	8	12	-28	
0	0	2	12	40	112	184	
0	0	2	16	80	306	658	482	
0	0	2	20	132	668	2310	5378	6586	
0	0	2	24	196	1246	5890	20424	45380	47968	
>>> UBash(9,9,3)
50528
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	-2	0	
1	4	0	0	0	
1	5	4	6	8	10	
1	6	10	24	48	80	60	
1	7	18	60	168	390	600	462	
1	8	28	120	440	1360	3180	4984	3920	
1	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> printAll(3,9)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
P4(n, k)
1	
1	1	
1	2	2	
1	3	6	10	
1	4	12	12	18	
1	5	20	42	88	104	
1	6	30	96	288	528	488	
1	7	42	180	712	2028	3938	3918	
1	8	56	300	1480	5708	16658	32272	31128	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	18	
0	0	2	8	12	0	
0	0	2	12	40	112	190	
0	0	2	16	80	306	658	588	
0	0	2	20	132	668	2310	5378	6460	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(Z0Bash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	18	
0	0	2	8	12	0	
0	0	2	12	40	112	190	
0	0	2	16	80	306	658	588	
0	0	2	20	132	668	2310	5378	6460	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 error
P4 	 error
Z0 	 correct
Z1[] 	 error
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	90	
1	6	30	84	264	480	408	
1	7	42	168	672	1890	3612	3500	
1	8	56	288	1424	5440	15744	30352	29280	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	

================================================================ RESTART: Shell ===============================================================
>>> 
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(3,8)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
P4(n, k)
1	
1	1	
1	2	2	
1	3	6	10	
1	4	12	12	18	
1	5	20	42	88	104	
1	6	30	96	288	528	488	
1	7	42	180	712	2028	3938	3918	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	18	
0	0	2	8	12	0	
0	0	2	12	40	112	190	
0	0	2	16	80	306	658	588	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(Z0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 error
P4 	 error
Z0 	 error
Z1[] 	 correct
Zsqu 	 error
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> UBash(2,2,3)
2
>>> printAll(3,8)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
P3(n, k)
1	
1	1	
1	2	0	
1	3	0	6	
1	4	4	0	16	
1	5	10	30	80	60	
1	6	18	84	264	480	456	
1	7	28	168	672	1890	3612	3458	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	10	
1	4	6	12	10	
1	5	12	42	72	116	
1	6	20	96	272	552	440	
1	7	30	180	696	2052	3842	4034	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	-4	
0	0	2	-4	26	
0	0	2	0	28	-28	
0	0	2	4	56	56	262	
0	0	2	8	96	250	802	372	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	6	
1	4	4	0	16	
1	5	10	30	80	60	
1	6	18	84	264	480	456	
1	7	28	168	672	1890	3612	3458	
1	8	40	288	1424	5440	15744	30352	29296	
>>> verify(8,4)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> P(2,2,3,False,False)
2
>>> 2*Zxy(3,3,3,0,1)
0
>>> Zsqu(2,2,3)
2
>>> Z0(2,2,3)
0
>>> sum(sum(Zxy(2,2,3) for y in range(-x,2)) for x in range(0,2))
Traceback (most recent call last):
  File "<pyshell#706>", line 1, in <module>
    sum(sum(Zxy(2,2,3) for y in range(-x,2)) for x in range(0,2))
  File "<pyshell#706>", line 1, in <genexpr>
    sum(sum(Zxy(2,2,3) for y in range(-x,2)) for x in range(0,2))
  File "<pyshell#706>", line 1, in <genexpr>
    sum(sum(Zxy(2,2,3) for y in range(-x,2)) for x in range(0,2))
TypeError: Zxy() missing 2 required positional arguments: 'x' and 'y'
>>> sum(sum(Zxy(2,2,3,x,y) for y in range(-x,2)) for x in range(0,2))

0

================================================================ RESTART: Shell ===============================================================
>>> 
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,4)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> Zsqu(2,2,3)
2
>>> Z0(2,2,3)
0
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,False,False))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	-4	
0	0	2	-4	14	
0	0	2	0	28	-4	
0	0	2	4	56	56	178	
0	0	2	8	96	250	802	588	
0	0	2	12	148	612	2454	4946	6412	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	18	
0	0	2	8	12	0	
0	0	2	12	40	112	190	
0	0	2	16	80	306	658	588	
0	0	2	20	132	668	2310	5378	6460	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	12	24	
0	0	2	12	40	112	106	
0	0	2	16	80	306	658	804	
0	0	2	20	132	668	2310	5378	5812	
>>> MBash(4,4,4)
0
>>> MBash(4,4,3)
0
>>> ZxyBash(2,2,4,0,1)
0
>>> MBash(4,4,4)
0
>>> 2*UBash(3,3,4)
0
>>> MBash(5,5,4)
12
>>> 2*UBash(4,4,4)
12
>>> 2*ZxyBash(3,3,4,0,1)
0
>>> MBash(5,5,4)
12
>>> MDraw(5,5,4)
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,2))+'\t';
	print(row)

	
0	
0	0	
0	0	0	
0	0	2	4	
0	0	2	0	8	
0	0	2	4	6	20	
0	0	2	8	18	16	68	
0	0	2	12	42	88	150	236	
0	0	2	16	78	256	650	1104	1232	

================================================================ RESTART: Shell ===============================================================
>>> 
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> n=3;k=3;j=2
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> t1
0
>>> t2
0
>>> 2*Zxy(n-1,k-1,j,0,j-2);
0
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
4
>>> PDraw(2,2,2,True,True)
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	

================================================================ RESTART: Shell ===============================================================
>>> 
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> PList(2,2,2,True,True)
>>> P(2,2,2,True,True)
2
>>> PBash(2,2,2,True,True)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> #checking P3
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> PBash(4,4,4,True,True)
16
>>> P(4,4,4,True,True)
24
>>> PBash(5,5,5,True,True)
110
>>> P(5,5,5,True,True)
120
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,4,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,4,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	12	24	
0	0	2	12	40	112	106	
0	0	2	16	80	306	658	804	
0	0	2	20	132	668	2310	5378	5812	
0	0	2	24	196	1246	5890	20424	45380	50378	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	18	
0	0	2	8	12	0	
0	0	2	12	40	112	190	
0	0	2	16	80	306	658	588	
0	0	2	20	132	668	2310	5378	6460	
0	0	2	24	196	1246	5890	20424	45380	48578	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,4))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	146	
0	0	2	16	90	344	828	964	
0	0	2	20	142	732	2664	6264	7184	
0	0	2	24	206	1336	6528	23132	53260	60172	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,4))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	20	44	
0	0	2	12	48	118	118	
0	0	2	16	88	336	826	960	
0	0	2	20	140	722	2648	6202	7272	
0	0	2	24	204	1324	6494	23000	53012	59604	
>>> U0(5,4,3)
12
>>> PBash(4,3,3,True,True)
0
>>> 2*Zxy(5-1,4-1,3,0,3-2)
4
>>> UDraw(5,4,3)
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> UBash(5,4,3)
18
>>> U0(5,4,3)
12
>>> PBash(4,3,3,True,True)
0
>>> n=5;k=4;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> t1
0
>>> t2
8
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
12
>>> P(4,3,3,True,True)
0
>>> MBash(5,4,3)
4
>>> Z0Bash(3,2,3)
2
>>> UBash(3,2,3)
2
>>> U0(3,2,3)
2
>>> U0(3,2,3)-Z0(2,1,3)+Zxy(2,1,3,0,1)
2
>>> U0(4,3,3)+Zxy(3,2,3,0,1)
4
>>> n=5;k=4;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> n
5
>>> k
4
>>> j
3
>>> t2 = sum(sum((Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> x=0;y=1
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> for x in range(0,3):
	for y in range(1-x,3):
		print(x,y)

		
0 1
0 2
1 0
1 1
1 2
2 -1
2 0
2 1
2 2
>>> x=0;y=2
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=1;y=0;
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=1;y=1
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=1;y=2;
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=-1
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
-2
>>> x=2;y=0;
Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
SyntaxError: multiple statements found while compiling a single statement
>>> x=2;y=0;
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=2;y=1
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=2;
>>> Uxy(n,k,j,x,y)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=0;y=1
>>> Uxy(n,k,j,x,y)
2
>>> x=0;y=1
>>> Uxy(n,k,j,x,y)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))
0
>>> sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> Uxy(5,4,3,0,1)
2
>>> U0(4,3,3)
4
>>> UDraw(4,3,3)
>>> n=5;k=4;j=3;x=0;y=1
>>> sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-1,j-1))
0
>>> sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-y-1,j-1))
2
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> U0(5,4,3)
18
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	2	
0	0	2	6	16	
0	0	2	10	18	26	
0	0	2	14	50	132	166	
0	0	2	18	94	354	792	894	
0	0	2	22	150	756	2646	6052	6788	
0	0	2	26	218	1386	6592	22772	50916	55962	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	0	0	
1	5	12	6	8	10	
1	6	20	24	48	80	60	
1	7	30	60	168	390	600	462	
1	8	42	120	440	1360	3180	4984	3920	
1	9	56	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> UBash(2,2,2)
0
>>> UBash(2,2,3)
2
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,2))+'\t';
	print(row)

	
Traceback (most recent call last):
  File "<pyshell#867>", line 4, in <module>
    row+=str(PBash(n,k,2))+'\t';
TypeError: PBash() missing 2 required positional arguments: 'wrap' and 'cyclic'
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,2,False,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	0	0	
1	5	12	6	8	10	
1	6	20	24	48	80	60	
1	7	30	60	168	390	600	462	
1	8	42	120	440	1360	3180	4984	3920	
1	9	56	210	960	3770	11952	28602	45856	36954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> P(2,2,2,True,True)
0
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,3,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
>>> PDraw(3,2,3,True,True)
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,2,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	0	0	10	
1	6	18	12	24	60	36	
1	7	28	42	112	280	420	322	
1	8	40	96	336	1040	2400	3696	2832	
1	9	54	180	792	3060	9540	22428	35280	27954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	2	
0	0	2	6	4	
0	0	2	10	18	38	
0	0	2	14	50	132	118	
0	0	2	18	94	354	792	954	
0	0	2	22	150	756	2646	6052	6596	
0	0	2	26	218	1386	6592	22772	50916	56250	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(P(n,k,4,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(PBash(n,k,4,True,True))+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
1	9	72	504	2952	14760	58752	175392	349200	347634	
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	0	0	
1	5	12	6	8	10	
1	6	20	24	48	80	60	
1	7	30	60	168	390	600	462	
1	8	42	120	440	1360	3180	4984	3920	
1	9	56	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> n=3;k=3;j=3;
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2)
2
>>> t1
8
>>> t2
6
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	20	30	
0	0	2	12	52	124	128	
0	0	2	16	96	346	802	922	
0	0	2	20	152	748	2656	6020	6644	
0	0	2	24	220	1378	6602	22740	50964	56118	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> U0(5,4,3)
20
>>> UBash(5,4,3)
18
>>> n=5;k=4;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(1-x,j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(1-x,j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
20
>>> 2*Zxy(n-1,k-1,j,0,j-2)
4
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
4
>>> x=0;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=1;y=0;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
4
>>> x=1;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> t1
0
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
0
>>> t2
16
>>> x=2;y=-1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> U0(n-x-y,k-x-y,j)
4
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))
2
>>> sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	524	
1	7	30	180	712	2040	3936	3786	
1	8	42	300	1480	5720	16668	32368	31498	
1	9	56	462	2736	13320	52032	152418	297792	290878	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50708	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row);

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> n=5;k=5;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2)
24
>>> PBash(4,4,3,True,True)
16
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
32
>>> t1
24
>>> t2
16
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> UDraw(5,5,3)
>>> PDraw(4,4,3,True,True)
>>> MBash(5,5,3)-2*Z0Bash(3,3,3)
12
>>> for x in range(0,j):
	for 
SyntaxError: invalid syntax
>>> for x in range(0,j):
	for y in
SyntaxError: invalid syntax
 
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(x,y);

		
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1)))

		
6
0
6
0
2
0
2
0
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))
0
>>> sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row);

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50708	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,4))+'\t';
	print(row);

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	152	
0	0	2	16	90	344	828	956	
0	0	2	20	142	732	2664	6264	7184	
0	0	2	24	206	1336	6528	23132	53260	60220	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,4))+'\t';
	print(row);

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	146	
0	0	2	16	90	344	828	964	
0	0	2	20	142	732	2664	6264	7184	
0	0	2	24	206	1336	6528	23132	53260	60172	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,8)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	12	24	
1	5	12	42	88	56	
1	6	20	96	288	540	582	
1	7	30	180	712	2040	3936	3606	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	4	
0	0	2	4	-8	
0	0	2	8	18	60	
0	0	2	12	46	108	4	
0	0	2	16	86	308	708	1112	
>>> for n in range(10):
	row='';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> n=3;k=3;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
4
>>>  int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
 
SyntaxError: unexpected indent
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
4
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> t1
0
t
>>> t2
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	524	
1	7	30	180	712	2040	3936	3786	
1	8	42	300	1480	5720	16668	32368	31498	
1	9	56	462	2736	13320	52032	152418	297792	290878	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50708	
>>> n=5;k=5;j=3
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Zxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1)))

		
6
0
6
0
2
0
2
0
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-x,j-1))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-y,j-1)))

		
6
Traceback (most recent call last):
  File "<pyshell#1003>", line 3, in <module>
    print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-x,j-1))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-y,j-1)))
  File "<pyshell#1003>", line 3, in <genexpr>
    print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-x,j-1))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-y,j-1)))
NameError: name 'Z2' is not defined
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> n=5;k=5;j=3
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-x,j-1))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-y,j-1)))

		
6
0
6
0
0
0
0
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> n=5;k=5;j=3
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-x,j-1))-sum(Z2(n-x-y-d,k-x-y-d,j) for d in range(j-y,j-1)))

		
6
0
6
0
0
0
0
0
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1)))

		
6
Traceback (most recent call last):
  File "<pyshell#1011>", line 3, in <module>
    print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1)))
  File "<pyshell#1011>", line 3, in <genexpr>
    print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1)))
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 135, in Z2xy
    return Z2(n-x-y,k-x-y);
TypeError: Z2() missing 1 required positional argument: 'j'
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> n=5;k=5;j=3
>>> for x in range(0,j):
	for y in range(max(0,1-x),j):
		print(U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1)))

		
6
0
6
0
0
0
0
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	72	
1	6	20	96	288	540	528	
1	7	30	180	712	2040	3936	3742	
1	8	42	300	1480	5720	16668	32368	31578	
1	9	56	462	2736	13320	52032	152418	297792	290586	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	18	28	
0	0	2	12	46	108	88	
0	0	2	16	86	308	708	864	
0	0	2	20	138	676	2380	5376	5730	
0	0	2	24	202	1260	5992	20576	46042	51164	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> n=5;k=5;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> return 0
SyntaxError: 'return' outside function
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
28
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
32
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> t1
8
>>> t2
4
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	524	
1	7	30	180	712	2040	3936	3786	
1	8	42	300	1480	5720	16668	32368	31498	
1	9	56	462	2736	13320	52032	152418	297792	290878	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50708	
>>> for j in range(2,8):
	print(UBash(j+2,j+2,j),U0(j+2,j+2,j))

	
0 0
20 24
146 152
996 1004
7426 7436
61904 61916
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,9)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	516	
1	7	30	180	712	2040	3936	3798	
1	8	42	300	1480	5720	16668	32368	31450	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	120	
0	0	2	16	86	308	708	784	
0	0	2	20	138	676	2380	5376	5974	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True)) - 2*(MBash(n,k,3)-2*Z0Bash(n-2,k-2,3)) + 2*Z0Bash(n-2,k-2,3) + 2*UBash(n-1,k-1,3) + 3*UBash(n-2,k-2,3) +2*UBash(n-3,k-3,3)+UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3)+2*ZxyBash(n-2,k-2,3,0,1)+2*ZxyBash(n-3,k-3,3,0,1)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	
Traceback (most recent call last):
  File "<pyshell#1047>", line 4, in <module>
    Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True)) - 2*(MBash(n,k,3)-2*Z0Bash(n-2,k-2,3)) + 2*Z0Bash(n-2,k-2,3) + 2*UBash(n-1,k-1,3) + 3*UBash(n-2,k-2,3) +2*UBash(n-3,k-3,3)+UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3)+2*ZxyBash(n-2,k-2,3,0,1)+2*ZxyBash(n-3,k-3,3,0,1)
ZeroDivisionError: division by zero
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True)) - 2*(MBash(n,k,3)-2*Z0Bash(n-2,k-2,3)) + 2*Z0Bash(n-2,k-2,3) + 2*UBash(n-1,k-1,3) + 3*UBash(n-2,k-2,3) +2*UBash(n-3,k-3,3)+UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3)+2*ZxyBash(n-2,k-2,3,0,1)+2*ZxyBash(n-3,k-3,3,0,1)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	0	2	
0	0	2	8	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	120	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> def U2Bash(n,k,j):
	if n==2 and k==2:
		return 0;
	return UBash(n,k,j)

>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True)) - 2*(MBash(n,k,3)-2*Z0Bash(n-2,k-2,3)) + 2*Z0Bash(n-2,k-2,3) + 2*U2Bash(n-1,k-1,3) + 3*U2Bash(n-2,k-2,3) +2*U2Bash(n-3,k-3,3)+U2Bash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3)+2*ZxyBash(n-2,k-2,3,0,1)+2*ZxyBash(n-3,k-3,3,0,1)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	0	2	
0	0	2	4	
0	0	2	4	0	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	14	
1	5	12	42	88	74	
1	6	20	96	288	540	506	
1	7	30	180	712	2040	3936	3782	
1	8	42	300	1480	5720	16668	32368	31432	
1	9	56	462	2736	13320	52032	152418	297792	290956	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	-2	
0	0	2	4	4	
0	0	2	8	18	16	
0	0	2	12	46	108	114	
0	0	2	16	86	308	708	778	
0	0	2	20	138	676	2380	5376	5958	
0	0	2	24	202	1260	5992	20576	46042	50490	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	18	28	
0	0	2	12	46	108	88	
0	0	2	16	86	308	708	864	
0	0	2	20	138	676	2380	5376	5730	
0	0	2	24	202	1260	5992	20576	46042	51164	
>>> n=4;k=4;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
2
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
0
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> t1
0
>>> t2
2
>>> UDraw(4,4,3)
>>> for x in range(0,3):
	for y in range(max(0,1-x),3):
		print(x,y)

		
0 1
0 2
1 0
1 1
1 2
2 0
2 1
2 2
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=0;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=1;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=1;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> U0(n-x-y,k-x-y,j)
0
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))
0
>>> sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	108	
0	0	2	16	86	308	708	820	
0	0	2	20	138	676	2380	5376	5874	
0	0	2	24	202	1260	5992	20576	46042	50780	
>>> n=5;k=5;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
20
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
24
>>> t1
24
>>> t2
16
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
32
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> x=0y=1
SyntaxError: invalid syntax
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
6
>>> x=1;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
6
>>> x=1;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=0;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> U0(n-x-y,k-x-y,j)
0
>>> U0(3,3,3)
0
>>> sum(Z2xy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
2
>>> sum(Z2xy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))
0
>>> sum(Z2xy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> Z2xy(2,2,3,0,1)
2
>>> Zcol(2,2,2,0)
0
>>> Zcol(2,2,2,1)
2
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> for n in range(10):
	for
SyntaxError: invalid syntax
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(U0(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	10	
0	0	2	8	18	16	
0	0	2	12	46	108	140	
0	0	2	16	86	308	708	740	
0	0	2	20	138	676	2380	5376	6118	
0	0	2	24	202	1260	5992	20576	46042	50108	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> UBash(3,3,4)
0
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,4))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	146	
0	0	2	16	90	344	828	964	
0	0	2	20	142	732	2664	6264	7184	
0	0	2	24	206	1336	6528	23132	53260	60172	
>>> Z0(2,2,2)
0
>>> Z0(2,2,3)
0
>>> Z0(2,2,4)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	524	
1	7	30	180	712	2040	3936	3786	
1	8	42	300	1480	5720	16668	32368	31498	
1	9	56	462	2736	13320	52032	152418	297792	290878	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50708	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,3))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> UBash(4,4,3）
      
SyntaxError: invalid character '）' (U+FF09)
>>> UBash(4,4,3)
6
>>> Z0Bash(3,3,3)
0
>>> UDraw(4,4,3)
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	524	
1	7	30	180	712	2040	3936	3786	
1	8	42	300	1480	5720	16668	32368	31498	
1	9	56	462	2736	13320	52032	152418	297792	290878	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50708	
>>> n=5;k=5;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
24
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
32
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> t1
24
>>> t2
16
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
6
>>> x=0;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=1;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
6
>>> x=1;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=2;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
2
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))
0
>>> ZCxy(1,1,3,0,0)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	524	
1	7	30	180	712	2040	3936	3786	
1	8	42	300	1480	5720	16668	32368	31498	
1	9	56	462	2736	13320	52032	152418	297792	290878	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	112	
0	0	2	16	86	308	708	812	
0	0	2	20	138	676	2380	5376	5902	
0	0	2	24	202	1260	5992	20576	46042	50712	
>>> n=5;k=5;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
Traceback (most recent call last):
  File "<pyshell#1201>", line 1, in <module>
    t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
  File "<pyshell#1201>", line 1, in <genexpr>
    t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
  File "<pyshell#1201>", line 1, in <genexpr>
    t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
  File "<pyshell#1201>", line 1, in <genexpr>
    t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
TypeError: ZCxy() missing 2 required positional arguments: 'xPrev' and 'yPrev'
>>> n=5;k=5;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
24
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
32
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=0;y=2;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=1;y=0;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=1;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
2
>>> x=2;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
2
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> n-x-y-1
1
>>> j
3
>>> ZCxy(1,1,3,0,0)
Traceback (most recent call last):
  File "<pyshell#1232>", line 1, in <module>
    ZCxy(1,1,3,0,0)
TypeError: ZCxy() missing 2 required positional arguments: 'xPrev' and 'yPrev'
>>> ZCxy(1,1,3,0,0,1,2)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(3,10)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	20	18	
1	5	20	54	100	92	
1	6	30	112	318	600	570	
1	7	42	200	768	2208	4244	4082	
1	8	56	324	1570	6080	17682	34300	33292	
1	9	72	490	2868	13980	54552	159702	311808	304490	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	16	16	
1	5	20	50	90	80	
1	6	30	108	300	552	516	
1	7	42	196	742	2100	3990	3794	
1	8	56	320	1536	5888	16976	32656	31456	
1	9	72	486	2826	13680	53046	154350	299628	290970	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	0	
1	4	12	0	16	
1	5	20	30	80	60	
1	6	30	84	264	480	456	
1	7	42	168	672	1890	3612	3458	
1	8	56	288	1424	5440	15744	30352	29296	
1	9	72	450	2664	12870	50004	145656	283104	275166	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	4	
1	4	6	12	18	
1	5	12	42	88	80	
1	6	20	96	288	540	516	
1	7	30	180	712	2040	3936	3790	
1	8	42	300	1480	5720	16668	32368	31462	
1	9	56	462	2736	13320	52032	152418	297792	290946	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	4	
0	0	2	4	14	24	22	
0	0	2	6	26	70	132	124	
0	0	2	8	42	156	448	852	816	
0	0	2	10	62	294	1136	3280	6334	6112	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	6	6	
0	0	0	2	6	16	30	26	
0	0	0	2	8	30	84	156	146	
0	0	0	2	10	48	182	518	984	940	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	6	8	8	
0	0	2	8	20	36	32	
0	0	2	10	36	100	186	172	
0	0	2	12	56	212	602	1140	1086	
0	0	2	14	80	384	1474	4246	8170	7868	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	6	
0	2	6	18	30	28	
0	2	8	32	86	162	150	
0	2	10	50	186	532	1008	962	
0	2	12	72	342	1318	3798	7318	7052	
0	2	14	98	566	2748	10656	31034	60274	58570	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	2	
0	2	6	10	8	
0	2	8	22	38	34	
0	2	10	38	104	192	178	
0	2	12	58	218	618	1170	1112	
0	2	14	82	392	1504	4330	8326	8014	
0	2	16	110	638	3090	11974	34832	67592	65622	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	24	
0	0	2	12	50	116	132	
0	0	2	16	90	328	764	852	
0	0	2	20	142	708	2512	5708	6334	
0	0	2	24	206	1304	6240	21532	48278	53088	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	116	
0	0	2	16	86	308	708	792	
0	0	2	20	138	676	2380	5376	5946	
0	0	2	24	202	1260	5992	20576	46042	50564	
>>> UBash(6,6,3)
118
>>> n=6;k=6;j=3
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
116
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
120
>>> 2*Zxy(n-1,k-1,j,0,j-2)
4
>>> t1
64
>>> t2
56
>>> MBash(n,k,3)-2*Z0Bash(n-2,k-2,3)
32
>>> UDraw(6,6,3)
>>> #t2 should be 58
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
20
>>> x=0;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=1;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
20
>>> x=1;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=1;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=2;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
-2
>>> U0(n-x-y,k-x-y,j)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))
2
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
2
>>> ZCxy(0,0,3,0,0,2,2)
0
>>> ZCxy(1,1,3,0,0,2,2)
2
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,4)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> printAll(4,9)
P1(n, k)
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	22	
1	5	20	60	116	114	
1	6	30	120	354	700	692	
1	7	42	210	832	2478	4920	4884	
1	8	56	336	1670	6648	19848	39504	39318	
P2(n, k)
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	110	110	
1	6	30	120	348	684	672	
1	7	42	210	826	2450	4844	4788	
1	8	56	336	1664	6608	19680	39072	38800	
P3(n, k)
1	
1	1	
1	2	2	
1	3	6	6	
1	4	12	24	16	
1	5	20	60	80	110	
1	6	30	120	312	660	636	
1	7	42	210	784	2380	4704	4634	
1	8	56	336	1616	6480	19296	38304	38064	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	6	
1	4	6	24	22	
1	5	12	60	104	114	
1	6	20	120	336	680	674	
1	7	30	210	808	2430	4824	4788	
1	8	42	336	1640	6560	19584	38976	38782	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	2	
0	0	2	2	6	6	
0	0	2	4	14	28	26	
0	0	2	6	26	78	152	150	
0	0	2	8	42	168	496	984	976	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	2	2	
0	0	0	2	4	8	8	
0	0	0	2	6	18	34	34	
0	0	0	2	8	32	94	186	182	
Zsqu(n, k)
0	
0	0	
0	0	2	
0	0	2	2	
0	0	2	4	2	
0	0	2	6	12	10	
0	0	2	8	24	44	44	
0	0	2	10	40	116	228	224	
0	0	2	12	60	236	700	1384	1368	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	2	
0	2	4	8	8	
0	2	6	18	36	34	
0	2	8	32	96	186	184	
0	2	10	50	200	590	1170	1158	
0	2	12	72	360	1426	4252	8448	8392	
Scol(n, k)
0	
0	2	
0	2	2	
0	2	4	4	
0	2	6	12	10	
0	2	8	24	46	44	
0	2	10	40	118	230	226	
0	2	12	60	238	704	1392	1376	
0	2	14	84	418	1658	4938	9804	9734	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	128	152	
0	0	2	16	90	348	840	984	
0	0	2	20	142	736	2692	6344	7284	
U0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	140	
0	0	2	16	90	344	828	968	
0	0	2	20	142	732	2664	6264	7192	
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,4))+'
		
SyntaxError: EOL while scanning string literal
>>> row+=str(UBash(n,k,4))+'\t';
Traceback (most recent call last):
  File "<pyshell#1279>", line 1, in <module>
    row+=str(UBash(n,k,4))+'\t';
NameError: name 'row' is not defined
>>> for n in range(9):
	row = '';
	for k in range(n+1):
		row+=str(UBash(n,k,4))+'\t';
	print(row)

	
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	146	
0	0	2	16	90	344	828	964	
0	0	2	20	142	732	2664	6264	7184	
>>> n=6;k=6;j=4
>>> t1 = 2*sum(sum((Uxy(n,k,j,x,y)-sum(Zxy(n-x-1,k-x-1,j,y,d-1) for d in range(j-x-y-1,j-x-1))-sum(Zxy(n-y-1,k-y-1,j,x,d-1) for d in range(j-x-y-1,j-y-1))) for y in range(max(0,1-x),j-1-x)) for x in range(0,j-1));
>>> t2 = sum(sum((U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))) for y in range(max(0,1-x),j)) for x in range(0,j));
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True)) - t1 + t2 + 2*Zxy(n-1,k-1,j,0,j-2);
140
>>> UDraw(6,6,4)
>>> for x in range(0,4):
	for y in range(max(0,1-x),4):
		print(x,y)

		
0 1
0 2
0 3
1 0
1 1
1 2
1 3
2 0
2 1
2 2
2 3
3 0
3 1
3 2
3 3
>>> int(2*(k-1)/(n-1)*P(n-1,k-1,j,True,True))
220
>>> 2*Zxy(n-1,k-1,j,0,j-2)
0
>>> t1
148
>>> t2
68
>>> x=0;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
28
>>> x=0;y=2;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=0;y=3
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=1;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
28
>>> x=1;y=1;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=1;y=2;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=1;y=3;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
-2
>>> x=2;y=0;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
6
>>> x=2;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
-2
>>> x=2;y=3
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=3;y=0
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
x
>>> x=3;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
-2
>>> x=3;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=3;y=3
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> U0(n-x-y,k-x-y,j)
0
>>> x=1;y=3
>>> U0(n-x-y,k-x-y,j)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
4
>>> ZCxy(1,1,4,0,0,1,3)
2
>>> ZCxy(1,1,4,0,1,1,3)
2
>>> Z0(2,2,4)
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,4)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 error
>>> n=6;k=6;j=4
>>> x=1;y=3;
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
2
>>> x=3;y=1
>>> U0(n-x-y,k-x-y,j)+sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))+sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))-sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> x=2;y=2
>>> U0(n-x-y,k-x-y,j)
2
>>> sum(Zxy(n-y-1,k-y-1,j,0,d-1) for d in range(j-1,j-x))
0
>>> sum(Zxy(n-x-1,k-x-1,j,0,d-1) for d in range(j-1,j-y))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-x,j-1))
0
>>> sum(ZCxy(n-x-y-1,k-x-y-1,j,0,d-1,x,y) for d in range(j-y,j-1))
0
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,4)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,5)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 error
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(9,5)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	0	0	
1	5	12	6	8	10	
1	6	20	24	48	80	60	
1	7	30	60	168	390	600	462	
1	8	42	120	440	1360	3180	4984	3920	
1	9	56	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row += str(PBash(n,k,2,False,False)) + "\t';
		
SyntaxError: EOL while scanning string literal
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row += str(PBash(n,k,2,False,False)) + "\t";
	print(row)

	
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row += str(PBash(n,k,2,True,False)) + "\t";
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		row += str(PBash(n,k,2,True,True)) + "\t";
	print(row)

	
1	
1	1	
1	2	0	
1	3	0	0	
1	4	4	0	0	
1	5	10	0	0	10	
1	6	18	12	24	60	36	
1	7	28	42	112	280	420	322	
1	8	40	96	336	1040	2400	3696	2832	
1	9	54	180	792	3060	9540	22428	35280	27954	
>>> P(3,2,2,True,True)
-6
>>> n=3;k=2;j=2
>>> n*(P(n-1,k-1,j,False,False) - 2*Zxy(n,k,j,0,j-2) - sum(sum(Zxy(n-1,k-1,j,x,y) for y in range(j-3-x,j-1)) for x in range(0,j-1)))
-6
>>> P(n-1,k-1,j,False,False)
2
>>> 2*Zxy(n,k,j,0,j-2)
4
>>> 
============================== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py =============================
>>> verify(8,2)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,3)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(8,4)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> verify(9,5)
P1 	 correct
P2 	 correct
P3 	 correct
P4 	 correct
Z0 	 correct
Z1[] 	 correct
Zsqu 	 correct
S0 	 correct
Scol 	 correct
O0 	 correct
U0 	 correct
>>> printAll(2,10)
P1(n, k)
1	
1	1	
1	2	0	
1	3	2	0	
1	4	6	4	2	
1	5	12	18	20	14	
1	6	20	48	90	124	90	
1	7	30	100	272	582	860	646	
1	8	42	180	650	1928	4386	6748	5242	
1	9	56	294	1332	5110	15912	37566	59612	47622	
P2(n, k)
1	
1	1	
1	2	-2	
1	3	0	0	
1	4	4	0	0	
1	5	10	10	10	10	
1	6	18	36	60	84	60	
1	7	28	84	210	434	630	462	
1	8	40	160	544	1552	3440	5168	3920	
1	9	54	270	1170	4338	13158	30366	47178	36954	
P3(n, k)
1	
1	1	
1	2	0	
1	3	-6	0	
1	4	-4	0	0	
1	5	0	0	0	10	
1	6	6	12	24	60	36	
1	7	14	42	112	280	420	322	
1	8	24	96	336	1040	2400	3696	2832	
1	9	36	180	792	3060	9540	22428	35280	27954	
P4(n, k)
1	
1	1	
1	2	0	
1	3	-2	0	
1	4	0	0	0	
1	5	4	6	8	10	
1	6	10	24	48	80	60	
1	7	18	60	168	390	600	462	
1	8	28	120	440	1360	3180	4984	3920	
1	9	40	210	960	3770	11952	28602	45856	36954	
Z0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
Z1[](n, k)
0	
0	0	
0	0	2	
0	0	0	0	
0	0	0	2	0	
0	0	0	2	0	0	
0	0	0	2	2	2	0	
0	0	0	2	4	6	4	4	
0	0	0	2	6	14	22	30	20	
0	0	0	2	8	26	64	130	184	136	
Zsqu(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	2	2	0	
0	0	2	4	6	4	4	
0	0	2	6	14	22	30	20	
0	0	2	8	26	64	130	184	136	
0	0	2	10	42	142	402	882	1322	1000	
S0(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
Scol(n, k)
0	
0	2	
0	2	0	
0	2	2	0	
0	2	4	2	0	
0	2	6	8	6	4	
0	2	8	18	28	34	24	
0	2	10	32	78	152	214	156	
0	2	12	50	168	466	1012	1506	1136	
0	2	14	72	310	1132	3390	7760	11990	9348	
O0(n, k)
0	
0	0	
0	0	2	
0	0	2	0	
0	0	2	4	2	
0	0	2	8	10	4	
0	0	2	12	30	40	30	
0	0	2	16	62	148	230	184	
0	0	2	20	106	376	946	1580	1322	
0	0	2	24	162	772	2754	7200	12434	10668	
U0(n, k)
0	
0	0	
0	0	0	
0	0	2	0	
0	0	2	0	0	
0	0	2	4	6	0	
0	0	2	8	18	16	20	
0	0	2	12	42	88	150	120	
0	0	2	16	78	256	650	1104	952	
0	0	2	20	126	568	2010	5292	9254	8000	
>>> test = [1,2,3]
>>> test.pop(1)
2
>>> test
[1, 3]
>>> test.push
Traceback (most recent call last):
  File "<pyshell#1381>", line 1, in <module>
    test.push
AttributeError: 'list' object has no attribute 'push'
(
>>> test.push(1,2)
Traceback (most recent call last):
  File "<pyshell#1382>", line 1, in <module>
    test.push(1,2)
AttributeError: 'list' object has no attribute 'push'
>>> test.push(1)
Traceback (most recent call last):
  File "<pyshell#1383>", line 1, in <module>
    test.push(1)
AttributeError: 'list' object has no attribute 'push'
>>> 