var orginalTopic;
var remainingComponents;
var currentTopic = 0;
var currentSortedTopic;

function initWizard(components,sortedTopics) {
    var components = JSON.parse(components)['components'];
    //speichern der Ausgangsdaten
    orginalTopic = components;
    remainingComponents = components;
    $("#topic").text(JSON.parse(sortedTopics)[currentTopic]);
    currentSortedTopic = sortedTopics;
}

function yesPress() {
    var currentTopicString = JSON.parse(currentSortedTopic)[currentTopic];
    remainingComponents.forEach(function (element) {
        if(!(element['topics'].includes(currentTopicString))){
            var index = remainingComponents.indexOf(element)
            if (index > -1) {
                remainingComponents.splice(index, 1);
            }
        }
    })
    currentTopic = currentTopic + 1;

    if(remainingComponents.length <= 10 ){
        console.log(JSON.stringify(remainingComponents));
    } else{
        $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    }
    console.log(remainingComponents.length);
}

function noPress() {
    var currentTopicString = JSON.parse(currentSortedTopic)[currentTopic];
    console.log(currentTopicString);
    remainingComponents.forEach(function (element) {
        if(element['topics'].includes(currentTopicString)){
            var index = remainingComponents.indexOf(element)
            if (index > -1) {
                remainingComponents.splice(index, 1);
            }
        }
    })
    currentTopic = currentTopic + 1;

    if(remainingComponents.length <= 10 ){
        console.log(JSON.stringify(remainingComponents));
    } else{
        $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    }
    console.log(remainingComponents.length);
}

function dontknowPress() {
    currentTopic = currentTopic +1;
    $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    console.log(remainingComponents.length);
}

function restart(){
    currentTopic = 0;
    remainingComponents = orginalTopic;
    remainingComponents = orginalTopic.splice(0);
    $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    console.log(remainingComponents.length)
}