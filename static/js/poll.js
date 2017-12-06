/**
 * Created by jamesstrater-smith on 7/31/17.
 */

var chappelleVotes = 0;
var murphyVotes = 0;
var burrVotes = 0;

function updateGrandTotal (){
    var chappelleTotal = document.getElementById('chappelleVotes').innerHTML;
    var murphyTotal = document.getElementById('murphyVotes').innerHTML;
    var burrTotal = document.getElementById('burrVotes').innerHTML;

    if (document.getElementById('nom1').checked === true){
        chappelleVotes++;
        chappelleTotal = chappelleVotes;
        document.getElementById('chappelleVotes').innerHTML = chappelleTotal;
    } else if (document.getElementById('nom2').checked === true){
        murphyVotes++;
        murphyTotal = murphyVotes;
        document.getElementById('murphyVotes').innerHTML = murphyTotal;
    } else if (document.getElementById('nom3').checked === true){
        burrVotes++;
        burrTotal = burrVotes;
        document.getElementById('burrVotes').innerHTML = burrTotal;
    }
}

function setCookie() {
    var exdays = 10;
    var d = new Date();
    d.setTime(d.getTime() + (exdays*24*60*60*1000));

    document.cookie = "expires=" + d.toGMTString();

    var nodes = document.getElementsByClassName("autofill");
    for (var i = 0; i < nodes.length; i++) {
        var node = nodes[i];
        document.cookie = createCookieString(node.id, node.innerHTML);
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
            node.innerHTML = value;
            if (name === "chappelleVotes") {
                chappelleVotes = value;
            } else if (name === "murphyVotes") {
                murphyVotes = value;
            } else if (name === "burrVotes"){
                burrVotes = value;
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
    var decodedCookie = decodeURIComponent(document.cookie);
    var ca = decodedCookie.split(';');

    extractFieldsFromCookie(ca);
}