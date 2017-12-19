var orginalTopic;
var remainingComponents;
var currentTopic = 0;
var currentSortedTopic;

function initWizard(components,sortedTopics) {
    var components = JSON.parse(components)['components'];
    //speichern der Ausgangsdaten
    orginalTopic = components.slice();
    remainingComponents = components.slice();
    $("#topic").text(JSON.parse(sortedTopics)[currentTopic]);
    currentSortedTopic = sortedTopics.slice();
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
        $("#list").empty()
        $("#list").append('<ul>');
        for(i=0;i<remainingComponents.length;i++) {
            $("#list").append("<li><a href='#'>" + remainingComponents[i].name +"</a></li>");
        }
        $("#list").append('</ul>');
    } else{
        $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    }
    console.log(remainingComponents.length);
}

function noPress() {
    var currentTopicString = JSON.parse(currentSortedTopic)[currentTopic];
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
    //console.log(orginalTopic.length);
    [].splice.apply(remainingComponents, [0, remainingComponents.length].concat(orginalTopic));
    $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    console.log(remainingComponents.length)
}