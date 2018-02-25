# Bash-Login-Script

This login facility uses Bash to verify username and password pairs (but seriously... do not use this on a production server)<br>

### HOW IT WORKS
The main file `index.html` takes a username and password then uses `GET` to send the pairs to the backend cgi.<br>
The `checkit.cgi` file parses the QUERY_STRING to extract the username and password and checks this against hardcoded values. <br>

- Webpages are HTML5 compliant
- CSS is embedded in the files
- Username and password can be changed in the `checkit.cgi` file
- No php, python, perl, haserl or other scripting language is required 
