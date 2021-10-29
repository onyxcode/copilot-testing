// fetch a copypasta from the internet and print it to the screen
function fetch_copypasta() {
    var xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            var copypasta = xhr.responseText;
            document.getElementById("copypasta").innerHTML = copypasta;
        }
    }
    xhr.open("GET", "https://www.reddit.com/r/copypasta/random.json", true);
    xhr.send();
}

fetch_copypasta();