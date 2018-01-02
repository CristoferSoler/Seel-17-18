var orginalTopic;
var remainingComponents;
var currentTopic = 0;
var currentSortedTopic;
const thresholdTopicNumber = 10;
var valid = false;

const entryQuestionThread = 'Would you like to know more about a specific IT Thread?';
const entryQuestionComponent = 'Do you have a specific IT problem and would you like to know more about it and see its solutions?';
const questionThread = 'Do you have a problem with ';
const questionComponent = 'Do you have a problem with '

function inilizeData() {
    getDataFromServer();

    var components = JSON.parse(localStorage.getItem('componentsTopic'))['element'];
    var sortedTopics = JSON.parse(localStorage.getItem('sortedTopics'))['sortedTopicList'];

    if (localStorage.getItem('remainingComponents') === null) {
        remainingComponents = components.slice();
        localStorage.setItem('remainingComponents', JSON.stringify(remainingComponents));
    } else {
        remainingComponents = JSON.parse(localStorage.getItem('remainingComponents'));
    }

    if (localStorage.getItem('listOfBack') === null) {
        var currentTopicString = String(currentTopic);
        var listOfBack = {};
        listOfBack[currentTopicString] = remainingComponents;
        localStorage.setItem('listOfBack', JSON.stringify(listOfBack));
    }

    $("#topic").text(sortedTopics[currentTopic] + '?');
    currentSortedTopic = sortedTopics.slice();

    if (remainingComponents.length <= thresholdTopicNumber) {
        presentResults();
    }
    var mode = localStorage.getItem('mode');
    if(mode !== null){
        if(mode == 't'){
            $('#question').text(questionThread);
        } else {
            if(mode == 'c'){
                $('#question').text(questionComponent);
            }
        }
    }

    $("#dontKnowButton").removeClass('disabled');

    if (currentTopic === -2) {
        $("#topicBack").addClass('disabled');
    }
}

function initWizard() {

    if(localStorage.getItem('currentTopic')=== null){
        currentTopic = -2;
        localStorage.setItem('currentTopic',String(currentTopic));
    } else{
        currentTopic = parseInt(localStorage.getItem('currentTopic'));
    }
    if(currentTopic < 0){
        if(currentTopic == -1){
            $('#question').text(entryQuestionThread);
            $('#topic').text('');
        } else{
            if(currentTopic == - 2){
                $('#question').text(entryQuestionComponent);
                $('#topic').text('');
            }
        }

    } else {
        inilizeData();
    }
}

function yesPress() {
    console.log(currentTopic);
    if(currentTopic < 0){
        if(currentTopic == -2){
            currentTopic = 0;
            localStorage.setItem('currentTopic',String(currentTopic));
            localStorage.setItem('mode','c');
            $('#question').text(questionComponent);
            $('#dontKnowButton').removeClass('disabled');
            $('#topicBack').removeClass('disabled');

            initWizard()
        } else {
            if(currentTopic == -1){
                currentTopic = 0;
                localStorage.setItem('currentTopic',String(currentTopic));
                localStorage.setItem('mode','t');
                $('#question').text(questionThread);
                initWizard();
            }
        }
    } else{
        checkTopics(true);
    }
}

function noPress() {
    if(currentTopic < 0){
        if(currentTopic == -2){
            currentTopic = currentTopic + 1;
            localStorage.setItem('currentTopic',String(currentTopic));
            $('#question').text(entryQuestionThread);
            $('#topic').text('');
            $('#topicBack').removeClass('disabled');

        } else {
            if(currentTopic == -1){
                $('#question').text('Fehler');
                $('#topic').text('');
            }
        }
    } else {
        checkTopics(false);
    }

}

function checkTopicStayInside(yes) {
    var currentTopicString = currentSortedTopic[currentTopic];
    remainingComponents.forEach(function (element) {
        var check = element['topics'].includes(currentTopicString)
        if (yes) {
            check = !check;
        }

        if (check) {
            var index = remainingComponents.indexOf(element)
            if (index > -1) {
                remainingComponents.splice(index, 1);
            }
        }
    })
}

function checkExistsThereATopicAfterClickButton(yes,topicElements,nextTopic,goForward) {
    var currentTopicString = currentSortedTopic[nextTopic];
    topicElements.forEach(function (element) {
        var check = element['topics'].includes(currentTopicString)
        if (yes) {
            check = !check;
        }

        if (check) {
            var index = topicElements.indexOf(element)
            if (index > -1) {
                topicElements.splice(index, 1);
            }
        }
    })

    if(goForward){
        if(topicElements.length < 1 && yes){
            $('#yesButton').addClass('disabled');
        }
        if(topicElements.length < 1 && !yes){
            $('#noButton').addClass('disabled');
        }
        if($('#yesButton').hasClass('disabled')&& $('#noButton').hasClass('disabled')){
             $('#dontKnowButton').addClass('disabled');
        }
    } else{
        if(topicElements.length >= 1 && yes){
            $('#yesButton').removeClass('disabled');
        }
        if(topicElements.length >= 1 && !yes){
            $('#noButton').removeClass('disabled');
        }
        if(!$('#yesButton').hasClass('disabled') || !$('#noButton').hasClass('disabled')){
             $('#dontKnowButton').removeClass('disabled');
        }
    }


}

function checkTopics(yes) {

    if($("#topicBack").hasClass('disabled')){
        $("#topicBack").removeClass('disabled');
    }

    checkTopicStayInside(yes);

    currentTopic = currentTopic + 1;

    checkExistsThereATopicAfterClickButton(true,remainingComponents.slice(),currentTopic,true);
    checkExistsThereATopicAfterClickButton(false,remainingComponents.slice(),currentTopic,true);

    addGoBackListTopicList();
    checkPresentResults();
}

function checkPresentResults() {
        if (remainingComponents.length <= thresholdTopicNumber) {
            $("#topic").text(currentSortedTopic[currentTopic] + '?');
            presentResults();
        } else {
            $("#list").empty();
            $("#topic").text(currentSortedTopic[currentTopic]+ '?');
        }
        safeData();
    }


function dontknowPress() {
    if($("#topicBack").hasClass('disabled')){
        $("#topicBack").removeClass('disabled');
    }

    currentTopic = currentTopic + 1;
    addGoBackListTopicList();
    $("#topic").text(currentSortedTopic[currentTopic] + '?');

    checkExistsThereATopicAfterClickButton(true,remainingComponents.slice(),currentTopic,true);
    checkExistsThereATopicAfterClickButton(false,remainingComponents.slice(),currentTopic),true;

    addGoBackListTopicList()

    safeData();
}

function addGoBackListTopicList() {
    var topicString = String(currentTopic);
    var goBackList = JSON.parse(localStorage.getItem('listOfBack'));
    console.log(goBackList);
    goBackList[topicString] = remainingComponents;
    localStorage.setItem('listOfBack',JSON.stringify(goBackList));
}


function restart(){
    currentTopic = -2;
    $("#list").empty();
    $('#dontKnowButton').addClass('disabled');
    $('#topicBack').addClass('disabled');

    if($('#yesButton').hasClass('disabled')) {
        $('#yesButton').removeClass('disabled');
    }
    if($('#noButton').hasClass('disabled')) {
        $('#noButton').removeClass('disabled');
    }

    $('#question').text(entryQuestionComponent);
    $('#topic').text('');

    clearTopicStorage();

    //initWizard();
}

function checkEnableButtons () {
    if(remainingComponents.length >= 1){
        checkExistsThereATopicAfterClickButton(true,remainingComponents.slice(),currentTopic,false);
        checkExistsThereATopicAfterClickButton(false,remainingComponents.slice(),currentTopic),false;
    }
}

function topicBack() {
    if((currentTopic -1) >= 0) {
        currentTopic = currentTopic - 1;
        var currentTopicString = String(currentTopic);
        var listOfBack = JSON.parse(localStorage.getItem('listOfBack'));
        remainingComponents = listOfBack[currentTopicString];
        checkPresentResults();
        checkEnableButtons();
    } else{
        if(currentTopic - 1 == -2){
            currentTopic = - 2;
            $("#topicBack").addClass('disabled');
            $("#dontKnowButton").addClass('disabled');

            $('#question').text(entryQuestionComponent);
            $('#topic').text('');
            localStorage.setItem('mode','c');
            clearTopicStorage();

        } else {
            if(currentTopic -1 == -1){
                if(localStorage.getItem('mode') == 'c'){
                    currentTopic = - 2;
                    $("#topicBack").addClass('disabled');
                    $("#dontKnowButton").addClass('disabled');
                    $('#question').text(entryQuestionComponent);
                    $('#topic').text('');
                    localStorage.setItem('mode','c');
                    clearTopicStorage();

                }
                if(localStorage.getItem('mode') == 't'){
                    currentTopic = currentTopic -1;
                    $('#question').text(entryQuestionThread);
                     $("#dontKnowButton").addClass('disabled');
                    $('#topic').text('');
                    localStorage.setItem('mode','t');
                    clearTopicStorage();
                }
            }

        }
    }



}

function clearTopicStorage() {
   localStorage.removeItem('componentsTopic');
    localStorage.removeItem('remainingComponents');
    localStorage.removeItem('sortedTopics');
    localStorage.removeItem('listOfBack');
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

    $('li a').bind('click',function () {
        valid = true;
        console.log('in Bind of test');
    });

    //localStorage.setItem("wizard", JSON.stringify(remainingComponents))
}

function getDataFromServer(){

    if(localStorage.getItem('mode') == 'c'){
        data = {'element':'c'}
    } else {
        if(localStorage.getItem('mode')== 't'){
            data = {'element':'t'}
        }
    }

    if(localStorage.getItem('componentsTopic') === null){
        $.ajax({
            dataType:'json',
            url:'/_wizard/elementsPlusTopics/',
            data: data,
            async: false,
            success:function (result) {
                localStorage.setItem('componentsTopic',JSON.stringify(result));
            }
        });
    }

    if(localStorage.getItem('sortedTopics') === null){
        $.ajax({
            dataType:'json',
            url:'/_wizard/sortedTopics/',
            data: data,
            async: false,
            success:function (result) {
                localStorage.setItem('sortedTopics',JSON.stringify(result));
            }
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
    localStorage.removeItem('listOfBack');
    localStorage.removeItem('mode');
}

function buttonsWizard() {
    $('#yesButton').on('click', function (e) {
        if(!($('#yesButton').hasClass('disabled'))){
            yesPress();
            valid = false;
        }
    })

    $('#noButton').on('click', function (e) {
        if(!($('#noButton').hasClass('disabled'))) {
            noPress();
            valid = false;
        }
    })

    $('#dontKnowButton').on('click', function (e) {
        if(!($('#dontKnowButton').hasClass('disabled'))){
            dontknowPress();
            valid = false;
        }
    })

    $('#restart').on('click', function (e) {
        restart();
         valid = false;
    })

    $('#topicBack').on('click', function (e) {
        if(!($('#topicBack').hasClass('disabled'))){
            topicBack();
            valid = false;
        }
    })
}


function initWizardsComponents(){
    //handle löschend er Wizarddaten
    wireupEvents();
    buttonsWizard();
    setPanel();
    $('a').bind('click',function () {
        valid = true;
        console.log('in Bind of test');
    });

    $('li a').bind('click',function () {
        valid = true;
        console.log('in Bind of test');
    });

    $('#opener').on('click', function() {
        initWizard();
        var panel = $('#slide-panel');
        if (panel.hasClass("visible")) {
            panel.removeClass('visible').animate({'left':'97%'});
            localStorage.removeItem('visible');
        } else {
            localStorage.setItem('visible',String(true));
            panel.addClass('visible').animate({'left':'62%'});
        }
        valid = false;
        return false;
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

function setPanel() {
    var panel = $('#slide-panel');
    if(localStorage.getItem('visible')!== null){
        panel.addClass('visible').animate({'left':'62%'});
        initWizard();
    }
}