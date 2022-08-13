Python 3.9.10 (main, Feb 19 2022, 01:53:40) 
[Clang 10.0.0 (clang-1000.10.44.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> 
>>> 
= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> UXBash(5,5,3)
8
>>> 
= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> UXBash(5,5,3)
[2, 4, 3, 1, 5]
[2, 4, 3, 5, 1]
[4, 2, 3, 1, 5]
[4, 2, 3, 5, 1]
[1, 5, 3, 2, 4]
[5, 1, 3, 2, 4]
[1, 5, 3, 4, 2]
[5, 1, 3, 4, 2]
8
>>> UBash(5,5,3)
20
>>> UList(5,5,3)
[3, 2, 4, 1, 5]
[3, 4, 2, 5, 1]
[2, 4, 3, 1, 5]
[2, 4, 3, 5, 1]
[4, 2, 3, 1, 5]
[4, 2, 3, 5, 1]
[4, 3, 1, 5, 2]
[2, 4, 1, 5, 3]
[4, 2, 5, 1, 3]
[4, 1, 5, 3, 2]
[2, 3, 5, 1, 4]
[3, 1, 5, 2, 4]
[3, 5, 1, 4, 2]
[2, 5, 1, 3, 4]
[1, 5, 3, 2, 4]
[5, 1, 3, 2, 4]
[1, 5, 3, 4, 2]
[5, 1, 3, 4, 2]
[1, 5, 2, 4, 3]
[5, 1, 4, 2, 3]
>>> UList(5,5,3)
[3, 2, 4, 1, 5]
[3, 4, 2, 5, 1]
[2, 4, 3, 1, 5]
[2, 4, 3, 5, 1]
[4, 2, 3, 1, 5]
[4, 2, 3, 5, 1]
[4, 3, 1, 5, 2]
[2, 4, 1, 5, 3]
[4, 2, 5, 1, 3]
[4, 1, 5, 3, 2]
[2, 3, 5, 1, 4]
[3, 1, 5, 2, 4]
[3, 5, 1, 4, 2]
[2, 5, 1, 3, 4]
[1, 5, 3, 2, 4]
[5, 1, 3, 2, 4]
[1, 5, 3, 4, 2]
[5, 1, 3, 4, 2]
[1, 5, 2, 4, 3]
[5, 1, 4, 2, 3]
>>> consecutivity(5,[5,1,3,2,4],False,True)
2
>>> consecutivity(5,[4,2,3,1,5],False,True)
2
>>> useBaseIndependently(5,[5,1,3,2,4])
True
>>> useBaseIndependently(5,[4,2,3,1,5])
True
>>> UXBash(5,5,3)
[2, 4, 3, 1, 5]
[2, 4, 3, 5, 1]
[4, 2, 3, 1, 5]
[4, 2, 3, 5, 1]
[1, 5, 3, 2, 4]
[5, 1, 3, 2, 4]
[1, 5, 3, 4, 2]
[5, 1, 3, 4, 2]
8
>>> UBash(4,4,3)
6
>>> for n in range(10)L
SyntaxError: invalid syntax
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
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True))-2*MBash(n,k,3)+6*Z0Bash(n-2,k-2,3)+2*UBash(n-1,k-1,3)+3*UBash(n-2,k-2,3)+2*UBash(n-3,k-3,3)+1*UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3)
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	8	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	104	120	
0	0	2	16	86	304	704	784	
0	0	2	20	138	672	2372	5364	5948	
0	0	2	24	202	1256	5980	20544	45982	50476	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Ubash = UBash(n,k,3);
		row+=str(Ubash)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> 
= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> UVBash(5,5,3)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    UVBash(5,5,3)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 362, in UVBash
    if consecutivity(n, p, False, True)<j and useBaseIndevependently(n,p):
NameError: name 'useBaseIndevependently' is not defined
>>> 
= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> UVBash(5,5,3)
80
>>> 
= RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py
>>> UVBash(5,5,3)
6
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Ubash = UBash(n,k,3);
		row+=str(Ubash)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	18	20	
0	0	2	12	46	108	118	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
>>> for n in range(2,10):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True))-2*MBash(n,k,3)+6*Z0Bash(n-2,k-2,3)+2*UBash(n-1,k-1,3)+3*UBash(n-2,k-2,3)+2*UBash(n-3,k-3,3)+1*UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3) + 2*Z0Bash(n-3,k-3,3)+2*Z0Bash(n-4,k-4,3)+2*Z0Bash(n-5,k-5,3)
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	8	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	120	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5380	5960	
0	0	2	24	202	1260	5992	20580	46042	50532	
>>> for n in range(2,12):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True))-2*MBash(n,k,3)+6*Z0Bash(n-2,k-2,3)+2*UBash(n-1,k-1,3)+3*UBash(n-2,k-2,3)+2*UBash(n-3,k-3,3)+1*UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3) + 2*Z0Bash(n-3,k-3,3)+2*Z0Bash(n-4,k-4,3)+2*Z0Bash(n-5,k-5,3)
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	8	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	120	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5380	5960	
0	0	2	24	202	1260	5992	20580	46042	50532	
0	0	2	28	278	2108	12648	58460	197706	437384	477010	
Traceback (most recent call last):
  File "<pyshell#30>", line 4, in <module>
    Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True))-2*MBash(n,k,3)+6*Z0Bash(n-2,k-2,3)+2*UBash(n-1,k-1,3)+3*UBash(n-2,k-2,3)+2*UBash(n-3,k-3,3)+1*UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3) + 2*Z0Bash(n-3,k-3,3)+2*Z0Bash(n-4,k-4,3)+2*Z0Bash(n-5,k-5,3)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 30, in PBash
    if consecutivity(n, p, wrap, cyclic) < j:
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 83, in consecutivity
    if diff!=1 and diff!=n-1: #end streak
KeyboardInterrupt
>>> for n in range(2,12):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,3,True,True))-2*MBash(n,k,3)+6*Z0Bash(n-2,k-2,3)+2*UBash(n-1,k-1,3)+3*UBash(n-2,k-2,3)+2*UBash(n-3,k-3,3)+1*UBash(n-4,k-4,3)-2*Z0Bash(n-3,k-3,3)-2*Z0Bash(n-4,k-4,3)-2*Z0Bash(n-5,k-5,3) + 2*Z0Bash(n-3,k-3,3)+2*Z0Bash(n-4,k-4,3)
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	8	
0	0	2	4	6	
0	0	2	8	18	24	
0	0	2	12	46	108	120	
0	0	2	16	86	308	708	788	
0	0	2	20	138	676	2380	5376	5960	
0	0	2	24	202	1260	5992	20576	46042	50528	
0	0	2	28	278	2108	12648	58456	197702	437372	477002	
0	0	2	32	366	3268	23692	137808	625138	2086500	4575594	4959324	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,3,False, True);
		row+=str(Pbash)+'\t';
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
>>> for n in range(10);
SyntaxError: invalid syntax
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pcalc = PBash(n,k,3,True,True)+2*UBash(n-1,k-1,3)-2*Z0Bash(n-2,k-2,3)+UBash(n-2,k-2,3)-2*Z0Bash(n-3,k-3,3)+2*Z0Bash(n-1,k-1,3)+Z0Bash(n-2,k-2,3);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	8	18	
1	5	20	38	88	76	
1	6	30	92	284	528	508	
1	7	42	176	704	2012	3888	3750	
1	8	56	296	1468	5668	16528	32104	31208	
1	9	72	458	2720	13236	51720	151522	296088	289338	
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> NBash(10,6,3)
126
>>> UBash(8,6,3)-2*Z0Bash(7,3,3)
2368
>>> UBash(8,4,3)-2*Z0Bash(7,3,3)
126
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Nbash = NBash(n,k,3);
		row+=str(Nbash)+'\t';
	print(row);

	
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	0	0	
0	0	0	0	2	0	
0	0	0	0	2	0	6	
0	0	0	0	2	4	18	16	
0	0	0	0	2	8	42	96	110	
0	0	0	0	2	12	78	280	660	744	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Ncalc = UBash(n-2,k-2,3)-2*Z0Bash(n-3,k-3,3);
		row+=str(Ncalc)+'\t';
	print(row);

	
0	
0	0	
0	0	0	
0	0	0	0	
0	0	0	0	2	
0	0	0	0	2	0	
0	0	0	0	2	0	6	
0	0	0	0	2	4	18	16	
0	0	0	0	2	8	42	96	110	
0	0	0	0	2	12	78	280	660	744	
>>> for n in range(10):
	row = '';
	for k in range(n+1):
		Pbash = PBash(n,k,3,False, True);
		row+=str(Pbash)+'\t';
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
		Pcalc = PBash(n,k,3,True,True)+2*UBash(n-1,k-1,3)-2*Z0Bash(n-2,k-2,3)+UBash(n-2,k-2,3)-2*Z0Bash(n-3,k-3,3)+2*Z0Bash(n-1,k-1,3)+Z0Bash(n-2,k-2,3)+2*Z0Bash(n-1,k-1,3);
		row+=str(Pcalc)+'\t';
	print(row)

	
1	
1	1	
1	2	2	
1	3	6	4	
1	4	12	12	18	
1	5	20	42	88	80	
1	6	30	96	288	540	516	
1	7	42	180	712	2040	3936	3794	
1	8	56	300	1480	5720	16668	32368	31456	
1	9	72	462	2736	13320	52032	152418	297792	290970	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ubash = UBash(n,k,4);
		row+=str(Ubash)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	146	
0	0	2	16	90	344	828	964	
0	0	2	20	142	732	2664	6264	7184	
0	0	2	24	206	1336	6528	23132	53260	60172	
0	0	2	28	282	2204	13524	64088	221960	502808	561256	
>>> 2*(3/5)*PBash(5,3,3,True,True)-2*MBash(6,4,3)+2*Z0Bash(4,2,3)
16.0
>>> UXBash(6,4,3)
24
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*MBash(n,k,4)+4*Z0Bash(n-3,k-3,4)-2*(2*UBash(n-2,k-2,4)-2*Z0Bash(n-3,k-3,4)-2*Z0Bash(n-4,k-4,4))+4*Z0Bash(n-3,k-3,4)+4*Z0Bash(n-4,k-4,4)-2*(UBash(n-2,k-2,4)-2*Z0Bash(n-4,k-4,4))+4*Z0Bash(n-3,k-3,4)+2*UBash(n-1,k-1,4)+3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+1*UBash(n-6,k-6,4)+2*Z0Bash(n-4,k-4,4)+2*Z0Bash(n-5,k-5,4)+2*Z0Bash(n-6,k-6,4)-4*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-6*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	14	28	
0	0	2	12	42	112	128	
0	0	2	16	82	316	748	860	
0	0	2	20	134	688	2476	5780	6622	
0	0	2	24	198	1276	6184	21792	50028	56392	
0	0	2	28	274	2128	12976	61228	211516	478168	532924	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*UBash(n-1,k-1,4)-3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+1*UBash(n-6,k-6,4)+16*Z0Bash(n-3,k-3,4)+10*Z0Bash(n-4,k-4,4)-4*Z0Bash(n-5,k-5,4)-4*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	112	152	
0	0	2	16	90	332	828	956	
0	0	2	20	142	720	2652	6228	7150	
0	0	2	24	206	1324	6504	23048	53092	60016	
0	0	2	28	282	2192	13488	63932	221492	501896	560356	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*MBash(n,k,4)+4*Z0Bash(n-3,k-3,4)-2*(2*UBash(n-2,k-2,4)-2*Z0Bash(n-3,k-3,4)-2*Z0Bash(n-4,k-4,4))+4*Z0Bash(n-3,k-3,4)+4*Z0Bash(n-4,k-4,4)-2*(UBash(n-2,k-2,4)-2*Z0Bash(n-4,k-4,4))+4*Z0Bash(n-3,k-3,4)+2*UBash(n-1,k-1,4)+3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+1*UBash(n-6,k-6,4)+2*Z0Bash(n-4,k-4,4)+2*Z0Bash(n-5,k-5,4)+2*Z0Bash(n-6,k-6,4)-4*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-6*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	14	28	
0	0	2	12	42	112	128	
0	0	2	16	82	316	748	860	
0	0	2	20	134	688	2476	5780	6622	
0	0	2	24	198	1276	6184	21792	50028	56392	
0	0	2	28	274	2128	12976	61228	211516	478168	532924	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*UBash(n-1,k-1,4)-3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+UBash(n-6,k-6,4)+20*Z0Bash(n-3,k-3,4)+10*Z0Bash(n-4,k-4,4)-4*Z0Bash(n-5,k-5,4)-4*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4);
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	120	152	
0	0	2	16	90	340	828	964	
0	0	2	20	142	728	2660	6252	7174	
0	0	2	24	206	1332	6520	23104	53204	60120	
0	0	2	28	282	2200	13512	64036	221804	502504	560956	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mcalc = 2*UBash(n-1,k-1,4)-2*Z0Bash(n-3,k-3,4);
		row+=str(Mcalc)+'\t';
	print(row)

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	8	12	
0	0	0	4	16	40	56	
0	0	0	4	24	96	248	288	
0	0	0	4	32	176	684	1644	1916	
0	0	0	4	40	280	1456	5300	12472	14316	
0	0	0	4	48	408	2660	13004	46108	106216	120044	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mbash = MBash(n,k,4);
		row+=str(Mbash)+'\t';
	print(row)

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	12	12	
0	0	0	4	20	44	68	
0	0	0	4	28	108	288	340	
0	0	0	4	36	196	776	1880	2192	
0	0	0	4	44	308	1624	5956	14060	16180	
0	0	0	4	52	444	2928	14408	51252	118384	134060	
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> MList(6,4,4)
[4, 5, 6, 1]
[5, 6, 1, 4]
[4, 1, 6, 5]
[1, 6, 5, 4]
[3, 5, 6, 1]
[5, 6, 1, 3]
[3, 1, 6, 5]
[1, 6, 5, 3]
[2, 5, 6, 1]
[5, 2, 1, 6]
[6, 1, 2, 5]
[1, 6, 5, 2]
[4, 2, 1, 6]
[4, 6, 1, 2]
[2, 1, 6, 4]
[6, 1, 2, 4]
[3, 2, 1, 6]
[3, 6, 1, 2]
[2, 1, 6, 3]
[6, 1, 2, 3]
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> for n in range(2,11):
	row = ''l
	
SyntaxError: invalid syntax
>>> row = '';
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mbash = MBash(n,k,3);
		row+=str(Mbash)+'\t';
	print(row);

	
0	0	0	
0	0	0	0	
0	0	0	4	0	
0	0	0	4	4	12	
0	0	0	4	12	36	36	
0	0	0	4	20	88	204	228	
0	0	0	4	28	164	588	1368	1532	
0	0	0	4	36	264	1300	4620	10488	11672	
0	0	0	4	44	388	2436	11672	40256	90380	99424	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mcalc = 2*UBash(n-1,k-1,3)-2*Z0Bash(n-2,k-2,3);
		row+=str(Mcalc)+'\t';
	print(row);

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	4	12	
0	0	0	4	12	36	36	
0	0	0	4	20	88	204	228	
0	0	0	4	28	164	588	1368	1532	
0	0	0	4	36	264	1300	4620	10488	11672	
0	0	0	4	44	388	2436	11672	40256	90380	99424	
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mbash = MBash(n,k,3);
		row+=str(Mbash)+'\t';
	print(row);

	
0	0	0	
0	0	0	0	
0	0	0	4	0	
0	0	0	4	4	12	
0	0	0	4	12	36	36	
0	0	0	4	20	88	204	228	
0	0	0	4	28	164	588	1368	1532	
0	0	0	4	36	264	1300	4620	10488	11672	
0	0	0	4	44	388	2436	11672	40256	90380	99424	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mcalc = 2*UBash(n-1,k-1,4)-2*Z0Bash(n-3,k-3,4);
		row+=str(Mcalc)+'\t';
	print(row)

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	8	12	
0	0	0	4	16	40	56	
0	0	0	4	24	96	248	288	
0	0	0	4	32	176	684	1644	1916	
0	0	0	4	40	280	1456	5300	12472	14316	
0	0	0	4	48	408	2660	13004	46108	106216	120044	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mbash = MBash(n,k,4);
		row+=str(Mbash)+'\t';
	print(row)

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	8	12	
0	0	0	4	16	44	56	
0	0	0	4	24	100	252	300	
0	0	0	4	32	180	696	1680	1968	
0	0	0	4	40	284	1476	5388	12708	14588	
0	0	0	4	48	412	2688	13168	46760	107792	121896	
>>> MList(6,4,4)
[5, 6, 1, 4]
[4, 1, 6, 5]
[3, 5, 6, 1]
[5, 6, 1, 3]
[3, 1, 6, 5]
[1, 6, 5, 3]
[2, 5, 6, 1]
[5, 2, 1, 6]
[6, 1, 2, 5]
[1, 6, 5, 2]
[4, 2, 1, 6]
[4, 6, 1, 2]
[2, 1, 6, 4]
[6, 1, 2, 4]
[3, 6, 1, 2]
[2, 1, 6, 3]
>>> 2*UBash(5,3,4)-2*Z0Bash(3,1,4)
16
>>> 2*Z0Bash(3,1,4)
0
>>> MList(6,5,4)
[4, 3, 5, 6, 1]
[3, 5, 6, 1, 4]
[5, 6, 1, 4, 3]
[3, 4, 1, 6, 5]
[4, 1, 6, 5, 3]
[1, 6, 5, 3, 4]
[4, 2, 5, 6, 1]
[4, 5, 2, 1, 6]
[4, 5, 6, 1, 2]
[5, 4, 2, 1, 6]
[5, 4, 6, 1, 2]
[2, 5, 6, 1, 4]
[5, 2, 1, 6, 4]
[5, 6, 1, 4, 2]
[2, 4, 1, 6, 5]
[4, 6, 1, 2, 5]
[4, 1, 6, 5, 2]
[2, 1, 6, 4, 5]
[6, 1, 2, 4, 5]
[2, 1, 6, 5, 4]
[6, 1, 2, 5, 4]
[1, 6, 5, 2, 4]
[2, 3, 5, 6, 1]
[3, 2, 5, 6, 1]
[3, 5, 2, 1, 6]
[5, 3, 6, 1, 2]
[2, 5, 6, 1, 3]
[5, 2, 1, 6, 3]
[5, 6, 1, 2, 3]
[5, 6, 1, 3, 2]
[2, 3, 1, 6, 5]
[3, 2, 1, 6, 5]
[3, 6, 1, 2, 5]
[3, 1, 6, 5, 2]
[2, 1, 6, 3, 5]
[6, 1, 2, 5, 3]
[1, 6, 5, 2, 3]
[1, 6, 5, 3, 2]
[3, 4, 2, 1, 6]
[4, 3, 6, 1, 2]
[4, 2, 1, 6, 3]
[3, 6, 1, 2, 4]
[2, 1, 6, 3, 4]
[6, 1, 2, 4, 3]
>>> import PIL
>>> im = Image.new()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    im = Image.new()
NameError: name 'Image' is not defined
>>> from PIL import Image
>>> im = Image.new()
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    im = Image.new()
TypeError: new() missing 2 required positional arguments: 'mode' and 'size'
>>> im = Image.new(mode = 'RGBA', size = (1920,1080))
>>> im.show()
>>> img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193) )
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    img  = Image.new( mode = "RGB", size = (width, height), color = (209, 123, 193) )
NameError: name 'width' is not defined
>>> img  = Image.new( mode = "RGB", size = (1920,1080), color = (209, 123, 193) )
>>> img.show()
>>> sin(30)
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    sin(30)
NameError: name 'sin' is not defined
>>> Math.sin(30)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    Math.sin(30)
NameError: name 'Math' is not defined
>>> import Math
>>> Math.sin(30)
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    Math.sin(30)
AttributeError: module 'Math' has no attribute 'sin'
>>> import math
>>> math.sin(30)
-0.9880316240928618
>>> def f():
	return 1,2;

>>> t1,t2 = f()
>>> t1
1
>>> t2
2
>>> def f():
	return (1,2);

>>> t1,t2 = f()
>>> t1
1
>>> t2
2
>>> int(5/3)
1
>>> im = Image.new(mode = 'RGBA', size = (1920,1080))
>>> im.show()
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> MDraw(6,5,4)
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    MDraw(6,5,4)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 510, in MDraw
    drawPaths(im, n, pathPerms, 0.85);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 497, in drawPaths
    drawPath(image, pathPerms[i], vertexCoords);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 452, in drawPath
    draw.line(vertexCoords[pathPerm[i-1]] + vertexCoords[pathPerm[i]], width=3, fill='black');
IndexError: list index out of range
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> MDraw(6,5,4)
Traceback (most recent call last):
  File "<pyshell#138>", line 1, in <module>
    MDraw(6,5,4)
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 510, in MDraw
    drawPaths(im, n, pathPerms, 0.85);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 497, in drawPaths
    drawPath(image, pathPerms[i], vertexCoords);
  File "/Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py", line 452, in drawPath
    draw.line(vertexCoords[pathPerm[i-1]] + vertexCoords[pathPerm[i]], width=3, fill='black');
IndexError: list index out of range
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> MDraw(6,5,4)
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> polygonCoords(4,0,0,2)
[(1.4142135623730951, 1.414213562373095), (1.4142135623730951, -1.414213562373095), (-1.414213562373095, -1.4142135623730951), (-1.4142135623730954, 1.414213562373095)]
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> MDraw(6,5,4)
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mcalc = 2*UBash(n-1,k-1,4)-2*Z0Bash(n-3,k-3,4);
		row+=str(Mcalc)+'\t';
	print(row)

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	8	12	
0	0	0	4	16	40	56	
0	0	0	4	24	96	248	288	
0	0	0	4	32	176	684	1644	1916	
0	0	0	4	40	280	1456	5300	12472	14316	
0	0	0	4	48	408	2660	13004	46108	106216	120044	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Mbash = MBash(n,k,4);
		row+=str(Mbash)+'\t';
	print(row)

	
0	0	0	
0	0	0	4	
0	0	0	4	0	
0	0	0	4	8	12	
0	0	0	4	16	40	56	
0	0	0	4	24	96	248	288	
0	0	0	4	32	176	684	1644	1916	
0	0	0	4	40	280	1456	5300	12472	14316	
0	0	0	4	48	408	2660	13004	46108	106216	120044	
>>> 
=========== RESTART: /Users/admin/Documents/Restricted nPk/Programs/Restricted Permutations.py ==========
>>> MDraw(6,5,4)
>>> MDraw(8,5,4)
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*MBash(n,k,4)+4*Z0Bash(n-3,k-3,4)-2*(2*UBash(n-2,k-2,4)-2*Z0Bash(n-3,k-3,4)-2*Z0Bash(n-4,k-4,4))+4*Z0Bash(n-3,k-3,4)+4*Z0Bash(n-4,k-4,4)-2*(UBash(n-2,k-2,4)-2*Z0Bash(n-4,k-4,4))+4*Z0Bash(n-3,k-3,4)+2*UBash(n-1,k-1,4)+3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+1*UBash(n-6,k-6,4)+2*Z0Bash(n-4,k-4,4)+2*Z0Bash(n-5,k-5,4)+2*Z0Bash(n-6,k-6,4)-4*Z0Bash(n-4,k-4,4)-6*Z0Bash(n-5,k-5,4)-6*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4)
		row+=str(Ucalc)+'\t';
	print(row)

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	120	152	
0	0	2	16	90	340	828	964	
0	0	2	20	142	728	2660	6252	7174	
0	0	2	24	206	1332	6520	23104	53204	60120	
0	0	2	28	282	2200	13512	64036	221804	502504	560956	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*UBash(n-1,k-1,4)-3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+UBash(n-6,k-6,4)+20*Z0Bash(n-3,k-3,4)+10*Z0Bash(n-4,k-4,4)-4*Z0Bash(n-5,k-5,4)-4*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4);
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	120	152	
0	0	2	16	90	340	828	964	
0	0	2	20	142	728	2660	6252	7174	
0	0	2	24	206	1332	6520	23104	53204	60120	
0	0	2	28	282	2200	13512	64036	221804	502504	560956	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ubash = UBash(n,k,4);
		row+=str(Ubash)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	146	
0	0	2	16	90	344	828	964	
0	0	2	20	142	732	2664	6264	7184	
0	0	2	24	206	1336	6528	23132	53260	60172	
0	0	2	28	282	2204	13524	64088	221960	502808	561256	
>>> for n in range(2,11):
	row = '';
	for k in range(n+1):
		Ucalc = int(2*(k-1)/(n-1)*PBash(n-1,k-1,4,True,True))-2*UBash(n-1,k-1,4)-3*UBash(n-2,k-2,4)+4*UBash(n-3,k-3,4)+3*UBash(n-4,k-4,4)+2*UBash(n-5,k-5,4)+UBash(n-6,k-6,4)+20*Z0Bash(n-3,k-3,4)+10*Z0Bash(n-4,k-4,4)-4*Z0Bash(n-5,k-5,4)-4*Z0Bash(n-6,k-6,4)-6*Z0Bash(n-7,k-7,4)-2*Z0Bash(n-8,k-8,4) + 2*Z0Bash(n-3,k-3,4);
		row+=str(Ucalc)+'\t';
	print(row);

	
0	0	2	
0	0	2	0	
0	0	2	4	6	
0	0	2	8	22	28	
0	0	2	12	50	124	152	
0	0	2	16	90	344	828	968	
0	0	2	20	142	732	2664	6264	7186	
0	0	2	24	206	1336	6528	23132	53260	60172	
0	0	2	28	282	2204	13524	64088	221960	502808	561256	
>>> 