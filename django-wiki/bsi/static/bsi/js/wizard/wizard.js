//TODO Back,Restart,PresentResult

var amountOfTotalTopics = 0;
const thresholdTopicNumber = 10;
var elementWithTopicsList;
var valid = false;
var sortedTopicList;

const entryQuestionThread = 'Would you like to know more about a specific IT Threat?';
const entryQuestionComponent = 'Do you have a specific IT problem and would you like to know more about it and see its solutions?';
const questionThread = 'Do you have a problem with ';
const questionComponent = 'Do you have a problem with '

var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;

function setValid(validValue) {
    valid = validValue;
}

function stringToBoolean(boolString) {
        if (boolString == 'true') {
            bool = true;
        } else {
            bool = false;
        }
        return bool;
    }

function setCurrentTopicWordPanel() {
    $('#topicWord').text(sortedTopicList[amountOfTotalTopics]['topic']);
}

function showElements() {
    $('#articleTopicList').empty();
    var currentElements = sortedTopicList[amountOfTotalTopics]['elements'];
    setCurrentTopicWordPanel();
    currentElements.forEach(function(element) {
        var path = element['path'];
        var title = element['title'];

        $('#articleTopicList').append("<li class='list-group-item'><a href='" + path+"'>" + title +"</a></li>");
        valid = false;
    });

    var visible = stringToBoolean(localStorage.getItem('topicListVisible'))
    if(localStorage.getItem('topicListVisible')!==null){
        if(visible){
            $('#collapse1').collapse("show");
            $('#topicIcon').removeClass('glyphicon-plus');
            $('#topicIcon').addClass('glyphicon-minus');
        }
    }

}


function inilizeData() {
    getDataFromServer();

    if(amountOfTotalTopics < 0){
       invisbaleTopicResutlPanel()
    } else{
        $('#topics').removeClass('invisible');
        $('#results').addClass('invisible')
    }

    elementWithTopicsList = JSON.parse(localStorage.getItem('elementWithTopicsList'))['element'];
    sortedTopicList = JSON.parse(localStorage.getItem('sortedTopics'))['sortedTopicList'];

    $("#topic").text(sortedTopicList[amountOfTotalTopics]['topic'] + '?');

    //TODO
    /*
    if (remainingComponents.length <= thresholdTopicNumber) {
        $('#results').removeClass('invisible');
        showResults();
    }*/

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

    if (amountOfTotalTopics === -2) {
        $("#topicBack").addClass('disabled');
    } else{
        $("#topicBack").removeClass('disabled');
    }

    if(amountOfTotalTopics >= 0){
        showElements();
    }

}

function initWizard() {

    if(localStorage.getItem('amountOfTotalTopics')=== null){
        amountOfTotalTopics = -2;
        localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics));
    } else{
        amountOfTotalTopics = parseInt(localStorage.getItem('amountOfTotalTopics'));
    }

    if(amountOfTotalTopics < 0){
        $('#topics').addClass('invisible')
        $('#results').addClass('invisible')
    }

    if(amountOfTotalTopics < 0){
        if(amountOfTotalTopics == -1){
            $('#question').text(entryQuestionThread);
            $('#topic').text('');
        } else{
            if(amountOfTotalTopics == - 2){
                $('#question').text(entryQuestionComponent);
                $('#topic').text('');
            }
        }

    } else {
        inilizeData();
    }
}

function yesPress() {
    console.log(amountOfTotalTopics);
    if(amountOfTotalTopics < 0){
        if(amountOfTotalTopics == -2){
            amountOfTotalTopics = 0;
            localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics));
            localStorage.setItem('mode','c');
            $('#question').text(questionComponent);
            $('#dontKnowButton').removeClass('disabled');
            $('#topicBack').removeClass('disabled');

            initWizard()
        } else {
            if(amountOfTotalTopics == -1){
                amountOfTotalTopics = 0;
                localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics));
                localStorage.setItem('mode','t');
                $('#question').text(questionThread);
                initWizard();
            }
        }
    } else{
        checkTopics('y');
    }
}

function noPress() {
    if(amountOfTotalTopics < 0){
        if(amountOfTotalTopics == -2){
            amountOfTotalTopics = amountOfTotalTopics + 1;
            localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics));
            $('#question').text(entryQuestionThread);
            $('#topic').text('');
            $('#topicBack').removeClass('disabled');

        } else {
            if(amountOfTotalTopics == -1){
                $('#question').text('Would you like to find out if you have a problem you are not aware of? Unfortunately this feature is not available yet. Please press restart');
                $('#topic').text('');
                $('#yesButton').addClass('disabled');
                $('#noButton').addClass('disabled');
                $('#dontKnowButton').addClass('disabled');
                $('#topicBack').addClass('disabled');
            }
        }
    } else {
        checkTopics('n');
    }

}

function dontknowPress() {
    if($("#topicBack").hasClass('disabled')){
        $("#topicBack").removeClass('disabled');
    }
    checkTopics('d');
}

function setStateForTopic(topic) {
    if (this.currentTopic === topic.name){
        topic.state = this.pick;
        return topic
    } else{
        return topic;
    }
}

function filterState(topic) {
    return topic.state === this.pick;
}

function filterTopic(topic) {
    return topic.name === this.currentTopic;
}

function amountOfStates(changedTopicsOfElements) {
    var amountOfCorrectTopics = 0;
    var amountOfNotSureTopics = 0;

    if (this.pick !== 'n') {
        var filteredTopicOfElementsCorrect = changedTopicsOfElements.filter(filterState, {pick: 'y'});
        var filteredTopicOfElementsDontKnow = changedTopicsOfElements.filter(filterState, {pick: 'd'});
        amountOfCorrectTopics = filteredTopicOfElementsCorrect.length;
        amountOfNotSureTopics = filteredTopicOfElementsDontKnow.length;
    } else {
        var filteredTopicOfElementsCorrect = changedTopicsOfElements.filter(filterState, {pick: 'y'});
        var filteredCurrentTopicInElementsTopic = changedTopicsOfElements.filter(filterTopic, {currentTopic: this.currentTopic});

        amountOfCorrectTopics = filteredTopicOfElementsCorrect.length;
        if (filteredCurrentTopicInElementsTopic.length === 0) {
            amountOfCorrectTopics += 1;
        }

        var filteredTopicOfElementsDontKnow = changedTopicsOfElements.filter(filterState, {pick: 'd'});
        amountOfNotSureTopics = filteredTopicOfElementsDontKnow.length;
    }

    return{
        notSure:amountOfNotSureTopics,
        correct:amountOfCorrectTopics
    }

}

function calculatePercentage(amountOfCorrent, amountOfNotSure) {
    var dividend = amountOfCorrent + 0.5 * amountOfNotSure + 1;
    var divisor = amountOfTotalTopics + 1;
    result = dividend/divisor;
    return result;
}

function calculatePercentageOfOneElement(element) {
    var topicsOfElement = element['topics'];
    var changedTopicsOfElements = topicsOfElement.map(setStateForTopic,{pick:this.pick,name:element['name'],currentTopic:this.currentTopic});
    amount = amountOfStates.call(this, changedTopicsOfElements);

    percentage = calculatePercentage(amount.correct,amount.notSure);

    element.topics = changedTopicsOfElements;
    element.percentage = percentage;

    return element;
}

function calculatePercentageOfAllElements(pick) {
    var currentTopicString = sortedTopicList[amountOfTotalTopics-1]['topic'];
    elementWithTopicsList = elementWithTopicsList.map(calculatePercentageOfOneElement ,{pick: pick,currentTopic:currentTopicString});
}

function checkExistsThereATopicAfterClickButton(yes,topicElements,nextTopic,goForward) {
    var currentTopicString = sortedTopicList[nextTopic]['topic'];
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

function checkTopics(pick) {

    if($("#topicBack").hasClass('disabled')){
        $("#topicBack").removeClass('disabled');
    }

    amountOfTotalTopics = amountOfTotalTopics + 1;
    calculatePercentageOfAllElements(pick);

    //checkExistsThereATopicAfterClickButton(true,remainingComponents.slice(),amountOfTotalTopics,true);
    //checkExistsThereATopicAfterClickButton(false,remainingComponents.slice(),amountOfTotalTopics,true);
    //addGoBackListTopicList();

    postprocessingCalculation();
}

function temp(element) {
    delete element.topics;
    delete element.path;
    return element;
}

function postprocessingCalculation() {
    /*tempEl = jQuery.extend(true, [], elementWithTopicsList);
    tempElements = tempEl.map(temp);

    window.alert(JSON.stringify(tempElements));*/
    safeData();
    $("#topic").text(sortedTopicList[amountOfTotalTopics]['topic'] + '?');
    showElements();
    showResults();
    }

function addGoBackListTopicList() {
    var topicString = String(amountOfTotalTopics);
    var goBackList = JSON.parse(localStorage.getItem('listOfBack'));
    console.log(goBackList);
    goBackList[topicString] = remainingComponents;
    localStorage.setItem('listOfBack',JSON.stringify(goBackList));
}


function restart(){
    invisbaleTopicResutlPanel();

    amountOfTotalTopics = -2;
    localStorage.setItem('amountOfTotalTopics',amountOfTotalTopics);

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
        checkExistsThereATopicAfterClickButton(true,remainingComponents.slice(),amountOfTotalTopics,false);
        checkExistsThereATopicAfterClickButton(false,remainingComponents.slice(),amountOfTotalTopics),false;
    }
}

function topicBack() {
    if((amountOfTotalTopics -1) >= 0) {
        amountOfTotalTopics = amountOfTotalTopics - 1;
        var currentTopicString = String(amountOfTotalTopics);
        var listOfBack = JSON.parse(localStorage.getItem('listOfBack'));
        remainingComponents = listOfBack[currentTopicString];
        postprocessingCalculation();
        checkEnableButtons();
        setCurrentTopicWordPanel();
        showElements();
        if (remainingComponents.length > thresholdTopicNumber) {
            $('#results').addClass('invisible');
        }

    } else{
        if(amountOfTotalTopics - 1 == -2){
            amountOfTotalTopics = - 2;
            $("#topicBack").addClass('disabled');
            $("#dontKnowButton").addClass('disabled');

            $('#question').text(entryQuestionComponent);
            $('#topic').text('');
            localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics))
            localStorage.setItem('mode','c');
            clearTopicStorage();

        } else {
            if(amountOfTotalTopics -1 == -1){
                if(localStorage.getItem('mode') == 'c'){
                    amountOfTotalTopics = - 2;
                    $("#topicBack").addClass('disabled');
                    $("#dontKnowButton").addClass('disabled');
                    $('#question').text(entryQuestionComponent);
                    $('#topic').text('');
                    localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics))
                    localStorage.setItem('mode','c');
                    clearTopicStorage();

                }
                if(localStorage.getItem('mode') == 't'){
                    amountOfTotalTopics = amountOfTotalTopics -1;
                    $('#question').text(entryQuestionThread);
                     $("#dontKnowButton").addClass('disabled');
                    $('#topic').text('');
                    localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics))
                    localStorage.setItem('mode','t');
                    clearTopicStorage();
                }

                invisbaleTopicResutlPanel();
            }
        }
    }
}

function clearTopicStorage() {
   localStorage.removeItem('elementWithTopicsList');
   localStorage.removeItem('remainingComponents');
   localStorage.removeItem('sortedTopics');
   localStorage.removeItem('listOfBack');
}

function invisbaleTopicResutlPanel() {
    $('.panel-collapse').collapse('hide');
    $('#topicIcon').removeClass('glyphicon-minus');
    $('#topicIcon').addClass('glyphicon-plus');
    $('#resultIcon').removeClass('glyphicon-minus');
    $('#resultIcon').addClass('glyphicon-plus');

    $('#topics').addClass('invisible');
    $('#results').addClass('invisible');
}


function showResults() {
    $('#results').removeClass('invisible');
    //console.log(remainingComponents);
    $("#list").empty();
    //$("#list").append('<ul class="urd-square-success">');
    /*for(i=0;i<remainingComponents.length;i++) {
        $("#list").append("<li class='list-group-item'><a href='" + remainingComponents[i].path+"'>" + remainingComponents[i].name +"</a></li>");
    }*/
    elementWithTopicsList.forEach(function (element) {
        $("#list").append("<li class='list-group-item'>" + element.name + ': ' + element.percentage + "</li>");
    });

    var isExpanded = $('#collapse1').attr("aria-expanded");
    if(isExpanded){
         $(".panel-collapse").collapse("hide");
         //$("#collapseDiv").collapse("show");
        $('#collapseResults').collapse("show");
        $('#topicIcon').removeClass('glyphicon-minus');
        $('#topicIcon').addClass('glyphicon-plus');
        $('#resultIcon').removeClass('glyphicon-plus');
        $('#resultIcon').addClass('glyphicon-minus');

    } else {
        $('#collapseResults').collapse("show");
        $('#resultIcon').removeClass('glyphicon-plus');
        $('#resultIcon').addClass('glyphicon-minus');
    }

    valid = false;
}

function getDataFromServer(){

    if(localStorage.getItem('mode') == 'c'){
        data = {'element':'c'}
    } else {
        if(localStorage.getItem('mode')== 't'){
            data = {'element':'t'}
        }
    }

    if(localStorage.getItem('elementWithTopicsList') === null){
        $.ajax({
            dataType:'json',
            url:'/_wizard/elementsPlusTopics/',
            data: data,
            async: false,
            success:function (result) {
                localStorage.setItem('elementWithTopicsList',JSON.stringify(result));
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
    localStorage.setItem('amountOfTotalTopics',String(amountOfTotalTopics));
    localStorage.setItem('elementWithTopicsList',JSON.stringify(elementWithTopicsList))
}

function clearLocalStorage(){
    localStorage.removeItem('elementWithTopicsList');
    localStorage.removeItem('amountOfTotalTopics');
    localStorage.removeItem('remainingComponents');
    localStorage.removeItem('sortedTopics');
    localStorage.removeItem('visible');
    localStorage.removeItem('listOfBack');
    localStorage.removeItem('mode');
    localStorage.removeItem('selectedNode');
    localStorage.removeItem('topicListVisible');
    localStorage.removeItem('resultListVisible');
}

function buttonsWizard() {
    $('#yesButton').on('click', function (e) {
        if(!($('#yesButton').hasClass('disabled'))){
            valid = false;
            yesPress();

        }
    })

    $('#noButton').on('click', function (e) {
        if(!($('#noButton').hasClass('disabled'))) {
            valid = false;
            noPress();

        }
    })

    $('#dontKnowButton').on('click', function (e) {
        if(!($('#dontKnowButton').hasClass('disabled'))){
            valid = false;
            dontknowPress();

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

    $('#help').on('click', function (e) {
        valid = true;

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

    $('#topicList').click(function () {
            var isExpandedString = $('#collapse1').attr("aria-expanded");
            var isExpanded;
            isExpanded = stringToBoolean(isExpandedString);

            if(isExpanded){
                $('#topicIcon').removeClass('glyphicon-minus');
                $('#topicIcon').addClass('glyphicon-plus');
            } else {
                $('#topicIcon').removeClass('glyphicon-plus');
                $('#topicIcon').addClass('glyphicon-minus');
            }

            localStorage.setItem('topicListVisible',String(!isExpanded));


        });

        $('#resultList').click(function () {
            var isExpandedString = $('#collapseResults').attr("aria-expanded");
            var isExpanded;
            isExpanded = stringToBoolean(isExpandedString);

            if(isExpanded){
                $('#resultIcon').removeClass('glyphicon-minus');
                $('#resultIcon').addClass('glyphicon-plus');
            } else {
                $('#resultIcon').removeClass('glyphicon-plus');
                $('#resultIcon').addClass('glyphicon-minus');
            }

            localStorage.setItem('resultListVisible',String(!isExpanded));

        });


    $('#opener').on('click', function() {
        initWizard();
        var panel = $('#slide-panel');
        if (panel.hasClass("visible")) {
            panel.removeClass('visible').animate({'right':'50px'});
            localStorage.removeItem('visible');
        } else {
            localStorage.setItem('visible',String(true));
            if(width > 1200){
                panel.addClass('visible').animate({'right':'550px'});
            }else{
                panel.addClass('visible').animate({'right':'320px'});
            }
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
        if(width > 1200){
            panel.addClass('visible').animate({'right':'550px'});
        }else{
            panel.addClass('visible').animate({'right':'320px'});
        }
        initWizard();
    }
}