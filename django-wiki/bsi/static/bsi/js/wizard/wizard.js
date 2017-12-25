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

    if(localStorage.getItem('remainingComponents')=== null){
        remainingComponents = components.slice();
        localStorage.setItem('remainingComponents',JSON.stringify(remainingComponents));
    } else{
        remainingComponents = JSON.parse(localStorage.getItem('remainingComponents'));
    }

   /* if(localStorage.getItem('listOfBack') === null){
        currentTopicString = String(currentTopic);
        listOfBack = {};
        listOfBack[currentTopicString] = remainingComponents;
        localStorage.setItem('listOfBack',JSON.stringify(listOfBack));
    }*/

    $("#topic").text(sortedTopics[currentTopic]);
    currentSortedTopic = sortedTopics.slice();

    if(remainingComponents.length  <= thresholdTopicNumber){
        presentResults();
    }

}

function yesPress() {
    checkTopics(true);
}

function noPress() {
    checkTopics(false);
}

function checkTopics(yes) {
    var currentTopicString = currentSortedTopic[currentTopic];
    remainingComponents.forEach(function (element) {
        var check = element['topics'].includes(currentTopicString)
        if(yes){
          check= !check;
        }

        if(check){
            var index = remainingComponents.indexOf(element)
            if (index > -1) {
                remainingComponents.splice(index, 1);
            }
        }
    })
    currentTopic = currentTopic + 1;

    if(remainingComponents.length <= thresholdTopicNumber ){
        $("#topic").text(currentSortedTopic[currentTopic]);
        presentResults();
    } else{
        $("#topic").text(currentSortedTopic[currentTopic]);
    }

    safeData();
}


function dontknowPress() {
    currentTopic = currentTopic + 1;
    $("#topic").text(currentSortedTopic[currentTopic]);
    safeData();
}

function restart(){
    currentTopic = 0;
    [].splice.apply(remainingComponents, [0, remainingComponents.length].concat(orginalTopic));
    //$("#topic").text(currentSortedTopic[currentTopic]);
    localStorage.setItem('currentTopic',String(currentTopic));
    localStorage.removeItem('remainingComponents');
    $("#list").empty();
    initWizard();
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
    localStorage.removeItem('visible');
}

function buttonsWizard() {
    $('#yesButton').on('click', function (e) {
        yesPress();
        valid = false;
    })

    $('#noButton').on('click', function (e) {
        noPress();
         valid = false;
    })

    $('#dontKnowButton').on('click', function (e) {
        dontknowPress();
         valid = false;
    })

    $('#restart').on('click', function (e) {
        restart();
         valid = false;
    })
}


function initWizardsComponents(){
    //handle löschend er Wizarddaten
    wireupEvents();
    buttonsWizard();
    getDataFromServer();
    setPanel();
    $('a').bind('click',function () {
        valid = true;
        console.log('in Bind of a');
    });

    $('#opener').on('click', function() {
        initWizard();
        var panel = $('#slide-panel');
        if (panel.hasClass("visible")) {
            panel.removeClass('visible').animate({'left':'98%'});
            localStorage.removeItem('visible');
        } else {
            localStorage.setItem('visible',String(true));
            panel.addClass('visible').animate({'left':'70%'});
        }
        valid = false;
        return false;
    });
}

function wireupEvents(){
    if(!valid){
        console.log('Balc');
        window.onbeforeunload = askWheatherToClose;
    }
}

function askWheatherToClose(event){
    if(!valid){
        clearLocalStorage();
    }
}

function setPanel() {
    var panel = $('#slide-panel');
    if(localStorage.getItem('visible')!== null){
        panel.addClass('visible').animate({'left':'62%'});
        initWizard();
    }
}