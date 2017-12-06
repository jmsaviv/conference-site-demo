/* Name: James Strater Smith
 Class: CS336
 Created: 7/28/16
 Description: js cookie script */

function setCookie() {
    var exdays = 10;
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));

    document.cookie = "expires=" + d.toGMTString();

    var nodes = document.getElementsByClassName("autofill");
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        if (node.type === "radio") {
            if (!node.checked) {
                continue;
            }
        }
        document.cookie = createCookieString(node.id, node.value);
    }
}

function createCookieString(name, value) {
    return name + "=" + value + ";";
}

function extractFieldsFromCookie(ca) {
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        var pcs = c.split("=");
        var name = pcs[0];
        var value = pcs[1];
        var node = document.getElementById(name);
        if (node === null || node === "") {
        } else {
            if (node.type === "radio") {
                node.checked = true;
            } else {
                node.value = value;
            }
        }
    }
}

function getFieldFromCookie(cname, ca) {
    var name = cname + "=";
    for(var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) === ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) === 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

function checkCookie() {
    var id = document.getElementById("conferenceId").value;
    if (id.length === 6) {
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        var storedId = getFieldFromCookie("conferenceId", ca);
        if (storedId === id) {
            extractFieldsFromCookie(ca);
        } else {
            // Do nothing... not the conferenceID we know
        }
    } else {
        // Length not right, don't bother testing
    }
}
