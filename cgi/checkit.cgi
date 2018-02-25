#!/bin/bash
echo "Content-type: text/html"
echo ""

TNAME="caat"
TPASS="secret"

NAME=$(echo $QUERY_STRING | cut -d'=' -f2 | cut -d'&' -f1)
PASS=$(echo $QUERY_STRING | cut -d'=' -f3 | cut -d'&' -f1)

echo "<!DOCTYPE html>"
echo "<html>"
echo "<head>"
echo "<style>" 
echo "#icon{width:80px; height:80px; background-repeat:no-repeat; float:left; background-image:url(/icon.gif); background-position:center;}"
echo "#main{margin:auto; border:2px solid; width:400px; background:#F1F3F5; font-family:Arial;}"
echo ".caption{font-family:Arial; font-weight:bold; margin:10px; font-size:24px; color:#C64934;}"
echo ".text{border:1px solid #cccccc;}"
echo "form{margin-left:80px; border:1px solid; width:270px; background:#E9ECEF; font-family:Arial; font-weight:bold; font-size:12px; padding:5px; margin-bottom:10px;}"
echo "</style>"
echo "<title>Server Login System</title>"
echo "</head>"
echo "<body>"
echo "   <div id='main'>"

if [[ "$NAME" == "$TNAME" && "$PASS" == "$TPASS" ]]; then
   echo "      <div class='caption'>CORRECT</div>"
   echo "      <div id='icon'>&nbsp;</div>"
   echo "      <form action='/index.html' method='get' name='checkit'>"
   echo "         <table>"
   echo "         <tr><td></td><td><input class='text' type='submit' name='btn' value='CORRECT!' /></td></tr>"
   echo "         <p>Username/Password is correct!</p>"
else
   echo "      <div class='caption'>ERROR</div>"
   echo "      <div id='icon'>&nbsp;</div>"
   echo "      <form action='/index.html' method='get' name='checkit'>"
   echo "         <table>"
   echo "         <tr><td></td><td><input class='text' type='submit' name='btn' value='Try Again!' /></td></tr>"
   echo "         <p>Login FAILED!</p>"
fi

echo "         </table>"  
echo "      </form>"
echo "   </div>"
echo "</body>"
echo "</html>" 