$hsg1 = Invoke-WebRequest -Uri "http://sourceforge.net/directory/language%3Aproglang_labview/?page=3"


#$t1 = $hsg1.AllElements | Where class -EQ 'projects' 
$t1 = $hsg1.RawContent

$r = 'href\=\"\/projects\/(.+)\/\?source\=directory\"'

$k = ($t1 | Select-String $r -AllMatches).Matches
$k.Count
foreach ($n in $k)
{
 # $n.Value
}