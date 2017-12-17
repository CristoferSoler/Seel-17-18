var orginalTopic;


function initWizard(components,sortedTopics) {
    var components = JSON.parse(components)['components'];
    //speichern der Ausgangsdaten
    orginalTopic = components;

    $("#topic").text(JSON.parse(sortedTopics)[1]);
    //window.alert(JSON.parse(sortedTopics)[1])
    components.forEach(function (element) {
        //window.alert(JSON.stringify(element))
    })
}

function yesPress() {
    window.alert('Yes');
}

function noPress() {
    window.alert('No');
}

function dontknowPress() {
    window.alert('dont know');
}