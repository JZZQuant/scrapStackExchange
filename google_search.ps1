$url = "https://www.google.com/"
$searchtype = "search"#$args[0]
$search_string = "labview" #$args[1]
$no_of_search_results_per_page = "100" #$args[2]
$start_page = 0#$args[3]
$end_page = 100#$args[4]
$starting_url = "https://www.google.com/"+$searchtype+"?num="+$no_of_search_results_per_page +"&q="+$search_string+"&start="

for ($i = $start_page; $i -lt $end_page; $i++ )
{
    $final_url = $starting_url+$i.ToString()+'00'
    Write-Output $final_url  
    $hsg = Invoke-WebRequest -Uri $final_url -Credential 
    $hsg.Links | where innerHTML | sort innerHTML -Unique | Out-File "C:\dump\$search_string$i.txt"
}



