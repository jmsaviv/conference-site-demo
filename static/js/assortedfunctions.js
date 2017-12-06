/* Name: James Strater Smith
 Class: CS336
 Created: 7/20/16
 Description: js workshop validation script */

function workshopValidation() {

    var workshopA = document.getElementById("workshopA");
    var workshopB = document.getElementById("workshopB");
    var workshopC = document.getElementById("workshopC");
    var workshopD = document.getElementById("workshopD");
    var workshopE = document.getElementById("workshopE");
    var workshopF = document.getElementById("workshopF");
    var workshopG = document.getElementById("workshopG");
    var workshopH = document.getElementById("workshopH");
    var workshopI = document.getElementById("workshopI");
    var workshopJ = document.getElementById("workshopJ");

    if (workshopB.checked === true && (workshopD.checked === true || workshopE.checked === true || workshopF.checked === true)) {
        warning1();
    }
    else if (workshopF.checked === true && (workshopG.checked === true || workshopI.checked === true)) {
        warning2();
    }
    else if (workshopH.checked === true && workshopF.checked === false) {
        warning3();
    }
}

var strWindowFeatures = "menubar=no,location=no,scrollbars=no,status=no,height=500,width=400";

function warning1() {
    var windowOpen = window.open("", "new", strWindowFeatures);
    windowOpen.document.write("<body bgcolor=#8a2be2>");
    windowOpen.document.write("Registering for TV Comedy Writing excludes you from registering for any workshops " +
        "in session 2.");
    windowOpen.document.write("<form>");
    windowOpen.document.write("<input type='button' value='Close Window' onClick='window.close()'>");
    windowOpen.document.write("<form>");
    windowOpen.document.write("</body>");
    windowOpen.document.write("</html>");
}

function warning2() {
    var windowOpen = window.open("", "new", strWindowFeatures);
    windowOpen.document.write("<body bgcolor=#8a2be2>");
    windowOpen.document.write("Registering for Movie Production excludes you from registering for both " +
        "Improv Acting and Dramatic Acting in session 3. You must register for Comedy Acting instead.");
    windowOpen.document.write("<form>");
    windowOpen.document.write("<input type='button' value='Close Window' onClick='window.close()'>");
    windowOpen.document.write("<form>");
    windowOpen.document.write("</body>");
    windowOpen.document.write("</html>");
}

function warning3() {
    var windowOpen = window.open("", "new", strWindowFeatures);
    windowOpen.document.write("<body bgcolor=#8a2be2>");
    windowOpen.document.write("Cannot register for Comedy Acting in session 3 unless you also register for " +
        "Movie Production in session 2.");
    windowOpen.document.write("<form>");
    windowOpen.document.write("<input type='button' value='Close Window' onClick='window.close()'>");
    windowOpen.document.write("<form>");
    windowOpen.document.write("</body>");
    windowOpen.document.write("</html>");
}

function thanksAlert() {
    var nominee1 = document.getElementById("nom1");
    var nominee2 = document.getElementById("nom2");
    var nominee3 = document.getElementById("nom3");

    if (nominee1.checked === true) {
        alert("Thank you for voting for Dave Chappelle");
    }

    else if (nominee2.checked === true) {
        alert("Thank you for voting for Charlie Murphy");
    }

    else if (nominee3.checked === true) {
        alert("Thank you for voting for Bill Burr");
    }
}





