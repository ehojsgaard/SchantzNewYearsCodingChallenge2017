import Data.List(intercalate)
next y c=1.00847*(c+(if y < 2029 then 8900 else 17800)-(if c > 200000 then 0 else 1000))
s=(2016,0):map(\(y,r)->(y+1,next y r))s
(p,q:_)=span((< 1000000).snd)s
main=putStrLn$intercalate"\n"$map(\(a,b)->show a++"\t"++show b)$p++[q]