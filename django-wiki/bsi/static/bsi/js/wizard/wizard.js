var orginalTopic;
var remainingComponents;
var currentTopic = 0;
var currentSortedTopic;
const thresholdTopicNumber = 10;

function initWizard(components,sortedTopics) {
    if(localStorage.getItem('currentTopic')=== null){
        currentTopic = 0;
        localStorage.setItem('currentTopic',str(currentTopic));
    } else{
        currentTopic = Int(localStorage.getItem('currentTopic'));
    }

    var components = JSON.parse(localStorage.getItem('componentsTopic'));

    //braiche ich glaube nicht mehr
    orginalTopic = components.slice();

    if(localStorage.getItem('remainingComponents')=== null){
        remainingComponents = components.slice();
        localStorage.setItem('remainingComponents',remainingComponents);
    } else{
        remainingComponents = JSON.parse(localStorage.getItem('remainingComponents'));
    }

    remainingComponents =
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

    if(remainingComponents.length <= thresholdTopicNumber ){
        console.log(JSON.stringify(remainingComponents));
        $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
        console.log('buh')
        presentResults();
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

    if(remainingComponents.length <= thresholdTopicNumber ){
        $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
        console.log(JSON.stringify(remainingComponents));
        presentResults();
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
    console.log('Hello');
    [].splice.apply(remainingComponents, [0, remainingComponents.length].concat(orginalTopic));
    $("#topic").text(JSON.parse(currentSortedTopic)[currentTopic]);
    console.log(remainingComponents.length);
    $("#list").empty();
}

function presentResults() {
    //console.log(remainingComponents);
    $("#list").empty();
    console.log(remainingComponents.length);
    //$("#list").append('<ul class="urd-square-success">');
    for(i=0;i<remainingComponents.length;i++) {
        $("#list").append("<li><a href='" + remainingComponents[i].path+"'>" + remainingComponents[i].name +"</a></li>");
    }
    $("#list").append('</ul>');
    //localStorage.setItem("wizard", JSON.stringify(remainingComponents))
}
