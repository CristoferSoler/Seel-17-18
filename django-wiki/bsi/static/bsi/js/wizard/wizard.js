var orginalTopic;
var remainingComponents;
var currentTopic = 0;
var currentSortedTopic;
const thresholdTopicNumber = 10;
var valid = false;

function initWizard() {
    if(localStorage.getItem('currentTopic')=== null){
        currentTopic = 0;
        localStorage.setItem('currentTopic',String(currentTopic));
    } else{
        currentTopic = parseInt(localStorage.getItem('currentTopic'));
    }

    var components = JSON.parse(localStorage.getItem('componentsTopic'))['components'];
    var sortedTopics = JSON.parse(localStorage.getItem('sortedTopics'))['sortedTopicList'];

    console.log(components);

    //braiche ich glaube nicht mehr
    orginalTopic = components.slice();

    if(localStorage.getItem('remainingComponents')=== null){
        remainingComponents = components.slice();
        localStorage.setItem('remainingComponents',JSON.stringify(remainingComponents));
    } else{
        remainingComponents = JSON.parse(localStorage.getItem('remainingComponents'));
    }

    console.log(sortedTopics);

    $("#topic").text(sortedTopics[currentTopic]);
    currentSortedTopic = sortedTopics.slice();
}

function yesPress() {
    var currentTopicString = currentSortedTopic[currentTopic];
    console.log(currentTopicString);
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
        $("#topic").text(currentSortedTopic[currentTopic]);
        console.log('buh')
        presentResults();
    } else{
        $("#topic").text(currentSortedTopic[currentTopic]);
    }

    safeData();

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
        $("#topic").text(currentSortedTopic[currentTopic]);
        console.log(JSON.stringify(remainingComponents));
        presentResults();
    } else{
        $("#topic").text(currentSortedTopic[currentTopic]);
    }

    safeData();

    console.log(remainingComponents.length);
}

function dontknowPress() {
    currentTopic = currentTopic +1;
    $("#topic").text(currentSortedTopic[currentTopic]);

    safeData();

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

function getDataFromServer(){
    if(localStorage.getItem('componentsTopic') === null){
        $.getJSON('/_wizard/componentsPlusTopics/',function (result) {
            localStorage.setItem('componentsTopic',JSON.stringify(result));
        });
    }

    if(localStorage.getItem('sortedTopics') === null){
        console.log('test');
        $.getJSON('/_wizard/sortedTopics/',function (result) {
            localStorage.setItem('sortedTopics',JSON.stringify(result));
        });
    }
}

function safeData() {
    localStorage.setItem('currentTopic',String(currentTopic));
    localStorage.setItem('remainingComponents',JSON.stringify(remainingComponents))
}

function clearLocalStorage(){
    localStorage.removeItem('componentsTopic');
    localStorage.removeItem('currentTopic');
    localStorage.removeItem('remainingComponents');
    localStorage.removeItem('sortedTopics');
}

function buttonsWizard() {
    $('#yesButton').on('click', function (e) {
        yesPress();
    })

    $('#noButton').on('click', function (e) {
        noPress();
    })

    $('#dontKnowButton').on('click', function (e) {
        dontknowPress();
    })

    $('#restart').on('click', function (e) {
        restart();
    })
}


function initWizardsComponents(){
    //handle löschend er Wizarddaten
    wireupEvents();
    buttonsWizard();
    getDataFromServer();

    $('#wizard').on('show.bs.modal', function (e) {
        valid = false;
        initWizard('{{ components|safe }}','{{ sortedTopics|safe }}')
    });

    $('#opener').on('click', function() {
        var panel = $('#slide-panel');
        if (panel.hasClass("visible")) {
            panel.removeClass('visible').animate({'left':'97%'});
        } else {
            panel.addClass('visible').animate({'left':'80%'});
        }
        return false;
    });

    $('a').bind('click',function () {
        valid = true;
    });

}

function wireupEvents(){
    if(!valid){
        window.onbeforeunload = askWheatherToClose;
    }
}

function askWheatherToClose(event){
    if(!valid){
        clearLocalStorage();
    }
}
