$a=2016;$b=0;do{say"$a\t$b";$t=$b<1e6;$b=1.00847*($b+($a++<2029?89:178)*100-($b<2e5)*1e3)}while($t)