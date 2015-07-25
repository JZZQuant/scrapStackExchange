$url = "https://www.google.com/search?num=100&q=labview&start="

for ($i = 0; $i -lt 3;$i++)
{
    $temp = $url + $i.ToString() +"00"
    $WebClient = New-Object System.Net.WebClient
    $WebClient.DownloadFileAsync($temp,"C:\Users\Raghava\Desktop\abc"+$i.ToString()+".html")
}


