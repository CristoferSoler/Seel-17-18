/*
* Wizard modul
* This file contains all functions needed for the wizard aka Virtual Assistant. Questions are created based
* on the topics of articles. After a certain number of x, suitable articles are displayed.
* */

//Variablen
var answerList;
var amountOfTotalTopics = 0;
var elementWithTopicsList;
var valid = false;
var sortedTopicList;
var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;

//Question for the wizard
const entryQuestionThread = 'Would you like to know more about a specific IT Threat?';
const entryQuestionComponent = 'Do you have a specific problem concerning the protection of an IT System or IT Process, or\n' +
    'generally a problem about IT Security?';
const questionThread = 'Do you have a problem with ';
const questionComponent = 'Do you have a problem with '
// define how many answer must answer before results are displayed
const showResultCount = 10;
// define the ammount of results which are displayed
const numberOfShownResults = 5;
// define if there is a dynamic or strict border of results
const dynamicBorderOfResults = true;

function sortArrayByKey(array, key) {
    return array.sort(function(a, b) {
        var x = a[key]; var y = b[key];
        return ((x < y) ? -1 : ((x > y) ? 1 : 0));
    });
}

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
    currentElements.forEach(function (element) {
        var path = element['path'];
        var title = element['title'];

        $('#articleTopicList').append("<a class=\"list-group-item list-group-item-action\" href='" + path + "'>" + title + "</a>");
    });

    var visible = stringToBoolean(localStorage.getItem('topicListVisible'))
    if (localStorage.getItem('topicListVisible') !== null) {
        if (visible) {
            if(amountOfTotalTopics < showResultCount-1){
                $('#collapse1').collapse("show");
                $('#topicIcon').removeClass('glyphicon-plus');
                $('#topicIcon').addClass('glyphicon-minus');
            }
        }
    }
    valid = false;

}


function inilizeData() {
    if(localStorage.getItem('elementWithTopicsList') === null){
        getDataFromServer();
    }

    if (localStorage.getItem('answerList') === null) {
        answerList = [];
    } else {
        answerList = JSON.parse(localStorage.getItem('answerList'));
    }

    if (amountOfTotalTopics < 0) {
        invisbaleTopicResutlPanel()
    } else {
        $('#topics').removeClass('invisible');
        $('#results').addClass('invisible');
    }

    if(localStorage.getItem('elementWithTopicsList')!== null){
        elementWithTopicsList = JSON.parse(localStorage.getItem('elementWithTopicsList'))['element'];
        if(elementWithTopicsList == undefined){
            elementWithTopicsList = JSON.parse(localStorage.getItem('elementWithTopicsList'));
        }
    }

    sortedTopicList = JSON.parse(localStorage.getItem('sortedTopics'))['sortedTopicList'];

    $("#topic").text(sortedTopicList[amountOfTotalTopics]['topic'] + '?');
    showElements();
    showResults();

    var mode = localStorage.getItem('mode');
    if (mode !== null) {
        if (mode == 't') {
            $('#question').text(questionThread);
        } else {
            if (mode == 'c') {
                $('#question').text(questionComponent);
            }
        }
    }

    $("#dontKnowButton").removeClass('disabled');

    if (amountOfTotalTopics === -2) {
        $("#topicBack").addClass('disabled');
    } else {
        $("#topicBack").removeClass('disabled');
    }
}

function initWizard() {

    if (localStorage.getItem('amountOfTotalTopics') === null) {
        amountOfTotalTopics = -2;
        localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics));
    } else {
        amountOfTotalTopics = parseInt(localStorage.getItem('amountOfTotalTopics'));
    }

    if (amountOfTotalTopics < 0) {
        $('#topics').addClass('invisible')
        $('#results').addClass('invisible')
    }

    if (amountOfTotalTopics < 0) {
        if (amountOfTotalTopics == -1) {
            $('#question').text(entryQuestionThread);
            $('#topic').text('');
        } else {
            if (amountOfTotalTopics == -2) {
                $('#question').text(entryQuestionComponent);
                $('#topic').text('');
            }
        }

    } else {
        inilizeData();
    }
}

function  yesPress() {
    if (amountOfTotalTopics < 0) {
        if (amountOfTotalTopics == -2) {
            amountOfTotalTopics = 0;
            localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics));
            localStorage.setItem('mode', 'c');
            $('#question').text(questionComponent);
            $('#dontKnowButton').removeClass('disabled');
            $('#topicBack').removeClass('disabled');

            initWizard()
        } else {
            if (amountOfTotalTopics == -1) {
                amountOfTotalTopics = 0;
                localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics));
                localStorage.setItem('mode', 't');
                $('#question').text(questionThread);
                initWizard();
            }
        }
    } else {
        checkTopics('y', false);
    }
}

function noPress() {
    if (amountOfTotalTopics < 0) {
        if (amountOfTotalTopics == -2) {
            amountOfTotalTopics = amountOfTotalTopics + 1;
            localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics));
            $('#question').text(entryQuestionThread);
            $('#topic').text('');
            $('#topicBack').removeClass('disabled');

        } else {
            if (amountOfTotalTopics == -1) {
                $('#question').text('Would you like to find out if you have a problem you are not aware of?\n\n ' +
                    'Unfortunately this feature is not available yet. Please press restart');

                $('#question').html($('#question').html().replace(/\n/g,'<br/>'));
                $('#topic').text('');
                $('#yesButton').addClass('disabled');
                $('#noButton').addClass('disabled');
                $('#dontKnowButton').addClass('disabled');
                $('#topicBack').addClass('disabled');
            }
        }
    } else {
        checkTopics('n', false);
    }

}

function dontknowPress() {
    if ($("#topicBack").hasClass('disabled')) {
        $("#topicBack").removeClass('disabled');
    }
    checkTopics('d', false);
}

function setStateForTopic(topic) {
    if (this.currentTopic === topic.name) {
        topic.state = this.pick;
        return topic
    } else {
        return topic;
    }
}

function filterState(topic) {
    return topic.state === this.pick;
}

function filterTopic(topic) {
    return topic.name === this.currentTopic;
}

function amountOfStates(changedTopicsOfElements,amountOfNoCorrect) {
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

        if (filteredCurrentTopicInElementsTopic.length === 0) {
            if(answerList !== null && answerList.length >= 1){
                amountOfNoCorrect += 1;
            } else {
                amountOfNoCorrect = 0;
            }
        }

        amountOfCorrectTopics = filteredTopicOfElementsCorrect.length + amountOfNoCorrect;

        var filteredTopicOfElementsDontKnow = changedTopicsOfElements.filter(filterState, {pick: 'd'});
        amountOfNotSureTopics = filteredTopicOfElementsDontKnow.length;
    }

    return {
        notSure: amountOfNotSureTopics,
        correct: amountOfCorrectTopics,
        correctNo: amountOfNoCorrect
    }

}

function calculatePercentage(amountOfCorrent, amountOfNotSure) {
    var dividend = amountOfCorrent + 0.5 * amountOfNotSure + 1;
    var divisor = amountOfTotalTopics + 1;
    result = dividend / divisor;
    return result;
}

function calculatePercentageOfOneElement(element) {
    var topicsOfElement = element['topics'];
    var changedTopicsOfElements;
    if (this.goBack) {
        changedTopicsOfElements = topicsOfElement.map(setStateForTopic, {
            pick: 'i',
            name: element['name'],
            currentTopic: this.currentTopic
        });
    } else {
        changedTopicsOfElements = topicsOfElement.map(setStateForTopic, {
            pick: this.pick,
            name: element['name'],
            currentTopic: this.currentTopic
        });
    }

    amount = amountOfStates.call(this, changedTopicsOfElements,element['amountOfNoCorrect']);
    percentage = calculatePercentage(amount.correct, amount.notSure);
    element.topics = changedTopicsOfElements;
    element.percentage = percentage;
    element.amountOfNoCorrect = amount.correctNo;

    return element;
}

function calculatePercentageOfAllElements(pick, goBack) {
    var currentTopicString = sortedTopicList[amountOfTotalTopics - 1]['topic'];
    if (goBack) {
        amountOfTotalTopics = amountOfTotalTopics - 1;
    }
    elementWithTopicsList = elementWithTopicsList.map(calculatePercentageOfOneElement, {
        pick: pick,
        currentTopic: currentTopicString,
        goBack: goBack
    });
}

function checkTopics(pick, goBack) {

    if ($("#topicBack").hasClass('disabled')) {
        $("#topicBack").removeClass('disabled');
    }
    //List for go a question back

    if (!goBack) {
        answerList.push(pick);
        amountOfTotalTopics = amountOfTotalTopics + 1;
    }

    calculatePercentageOfAllElements(pick, goBack);
    postprocessingCalculation();
}

function checkExistsThereATopic() {
    var numberOfTopics = sortedTopicList.length;

    if(amountOfTotalTopics === numberOfTopics-1){
        $('#yesButton').addClass('disabled');
        $('#noButton').addClass('disabled');
        $('#dontKnowButton').addClass('disabled');
        $('#question').text('No more topics available. Please try again and press restart.');
        $('#topic').text('');
        invisbaleTopicResutlPanel()
    }
}

function postprocessingCalculation() {
    safeData();
    $("#topic").text(sortedTopicList[amountOfTotalTopics]['topic'] + '?');
    showElements();
    showResults();
    checkExistsThereATopic();
}


function restart() {
    invisbaleTopicResutlPanel();

    amountOfTotalTopics = -2;
    localStorage.setItem('amountOfTotalTopics', amountOfTotalTopics);

    $("#list").empty();
    $('#dontKnowButton').addClass('disabled');
    $('#topicBack').addClass('disabled');

    if ($('#yesButton').hasClass('disabled')) {
        $('#yesButton').removeClass('disabled');
    }
    if ($('#noButton').hasClass('disabled')) {
        $('#noButton').removeClass('disabled');
    }

    $('#question').text(entryQuestionComponent);
    $('#topic').text('');

    clearTopicStorage();
}

function checkGui() {
    if ($('#yesButton').hasClass('disabled')) {
        $('#yesButton').removeClass('disabled');
    }
    if ($('#noButton').hasClass('disabled')) {
        $('#noButton').removeClass('disabled');
    }
    if ($('#dontKnowButton').hasClass('disabled')) {
        $('#dontKnowButton').removeClass('disabled');
    }

    $('#question').text(questionComponent);

    //$('#topics').removeClass('invisible');
    //$('#results').removeClass('invisible');
}

function topicBack() {
    if ((amountOfTotalTopics - 1) >= 0) {
        var lastAnswer = answerList.pop();
        checkTopics(lastAnswer, true);
        checkGui();
    } else {
        if (amountOfTotalTopics - 1 == -2) {
            amountOfTotalTopics = -2;
            $("#topicBack").addClass('disabled');
            $("#dontKnowButton").addClass('disabled');

            $('#question').text(entryQuestionComponent);
            $('#topic').text('');
            localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics))
            localStorage.setItem('mode', 'c');
            clearTopicStorage();

        } else {
            if (amountOfTotalTopics - 1 == -1) {
                if (localStorage.getItem('mode') == 'c') {
                    amountOfTotalTopics = -2;
                    $("#topicBack").addClass('disabled');
                    $("#dontKnowButton").addClass('disabled');
                    $('#question').text(entryQuestionComponent);
                    $('#topic').text('');
                    localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics))
                    localStorage.setItem('mode', 'c');
                    clearTopicStorage();

                }
                if (localStorage.getItem('mode') == 't') {
                    amountOfTotalTopics = amountOfTotalTopics - 1;
                    $('#question').text(entryQuestionThread);
                    $("#dontKnowButton").addClass('disabled');
                    $('#topic').text('');
                    localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics))
                    localStorage.setItem('mode', 't');
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
    localStorage.removeItem('answerList');
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
    var answserList = JSON.parse(localStorage.getItem('answerList'));
    if (answserList !== null && answserList.length >= showResultCount ) {

        $('#results').removeClass('invisible');
        $("#list").empty();

        //Deep Copy
        var copyOfElementsWithTopicLists = JSON.parse(JSON.stringify(elementWithTopicsList));
        var sortedElementswithTopicLists = sortArrayByKey(copyOfElementsWithTopicLists, 'percentage').reverse();

        if(dynamicBorderOfResults){
            var highestPercentage = sortedElementswithTopicLists[0]['percentage'];

            if(sortedElementswithTopicLists[numberOfShownResults]['percentage'] === highestPercentage) {
                var counter = numberOfShownResults + 1;
                while (sortedElementswithTopicLists[counter]['percentage'] === highestPercentage) {
                    counter += 1;
                }
            } else{
                counter = numberOfShownResults;
            }
        } else {
            counter = numberOfShownResults;
        }

        sortedElementswithTopicLists.slice(0,counter).forEach(function (element) {
            $("#list").append("<li class='list-group-item'><a class='test' href='" + element["path"] + "'>" + element["name"] + "</a></li>");
        });

        var isExpanded = $('#collapse1').attr("aria-expanded");
        if (stringToBoolean(isExpanded)) {
            $("#collapse1").collapse("hide");
            localStorage.setItem('topicListVisible','false');
            $('#collapseResults').collapse("show");
            $('#topicIcon').removeClass('glyphicon-minus');
            $('#topicIcon').addClass('glyphicon-plus');
            $('#resultIcon').removeClass('glyphicon-plus');
            $('#resultIcon').addClass('glyphicon-minus');

        } else {
            var isExpandedResults = $('#collapseResults').attr("aria-expanded");
            if(!stringToBoolean(isExpandedResults)){
                $(".panel-collapse").collapse("hide");
                $('#collapseResults').collapse("show");
                $('#resultIcon').removeClass('glyphicon-plus');
                $('#resultIcon').addClass('glyphicon-minus');
            }
        }
    } else{
        $('#results').addClass('invisible');
        $("#list").empty();
    }
    valid = false;
}

function getDataFromServer() {

    if (localStorage.getItem('mode') == 'c') {
        data = {'element': 'c'}
    } else {
        if (localStorage.getItem('mode') == 't') {
            data = {'element': 't'}
        }
    }

    if (localStorage.getItem('elementWithTopicsList') === null) {
        $.ajax({
            dataType: 'json',
            url: '/_wizard/elementsPlusTopics/',
            data: data,
            async: false,
            success: function (result) {
                localStorage.setItem('elementWithTopicsList', JSON.stringify(result));
            }
        });
    }

    if (localStorage.getItem('sortedTopics') === null) {
        $.ajax({
            dataType: 'json',
            url: '/_wizard/sortedTopics/',
            data: data,
            async: false,
            success: function (result) {
                localStorage.setItem('sortedTopics', JSON.stringify(result));
            }
        });
    }

}

function safeData() {
    localStorage.setItem('answerList', JSON.stringify(answerList));
    localStorage.setItem('amountOfTotalTopics', String(amountOfTotalTopics));
    localStorage.setItem('elementWithTopicsList', JSON.stringify(elementWithTopicsList))
}

function clearLocalStorage() {
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
    localStorage.removeItem('answerList');
}

function buttonsWizard() {
    $('#yesButton').on('click', function (e) {
        if (!($('#yesButton').hasClass('disabled'))) {
            valid = false;
            yesPress();

        }
    })

    $('#noButton').on('click', function (e) {
        if (!($('#noButton').hasClass('disabled'))) {
            valid = false;
            noPress();

        }
    })

    $('#dontKnowButton').on('click', function (e) {
        if (!($('#dontKnowButton').hasClass('disabled'))) {
            valid = false;
            dontknowPress();

        }
    })

    $('#restart').on('click', function (e) {
        restart();
        valid = false;
    })

    $('#topicBack').on('click', function (e) {
        if (!($('#topicBack').hasClass('disabled'))) {
            topicBack();
            valid = false;
        }
    })

    $('#help').on('click', function (e) {
        valid = true;

    })

    $('#collapse1').on('show.bs.collapse', function () {
       valid = false
    });

    $('#collapseResults').on('show.bs.collapse', function () {
       valid = false
    });

}


function initWizardsComponents() {
    //handle löschend er Wizarddaten
    wireupEvents();
    buttonsWizard();
    setPanel();
    $('a').bind('click', function () {
        valid = true;
    });

    $('li a').bind('click', function () {
        valid = true;
    });

    $(document).on('click', '.list-group-item', function(e){
        valid = true;
    });

    $('#topicList').click(function () {
        var isExpandedString = $('#collapse1').attr("aria-expanded");
        var isExpanded;
        isExpanded = stringToBoolean(isExpandedString);

        if(isExpanded == undefined){
            $('#topicIcon').removeClass('glyphicon-plus');
            $('#topicIcon').addClass('glyphicon-minus');
        }

        if (isExpanded) {
            $('#topicIcon').removeClass('glyphicon-minus');
            $('#topicIcon').addClass('glyphicon-plus');
        } else {
            $('#topicIcon').removeClass('glyphicon-plus');
            $('#topicIcon').addClass('glyphicon-minus');
        }

        localStorage.setItem('topicListVisible', String(!isExpanded));


    });

    $('#resultList').click(function () {
        var isExpandedString = $('#collapseResults').attr("aria-expanded");
        var isExpanded;
        isExpanded = stringToBoolean(isExpandedString);

        if (isExpanded) {
            $('#resultIcon').removeClass('glyphicon-minus');
            $('#resultIcon').addClass('glyphicon-plus');
        } else {
            $('#resultIcon').removeClass('glyphicon-plus');
            $('#resultIcon').addClass('glyphicon-minus');
        }

        localStorage.setItem('resultListVisible', String(!isExpanded));

    });


    $('#opener').on('click', function () {
        var panel = $('#slide-panel');
        if (panel.hasClass("visible")) {
            if(width >= 576){
                panel.removeClass('visible').animate({'right': '50px'});
            } else {
                panel.removeClass('visible').animate({'right': '35px'});
            }
            localStorage.removeItem('visible');
        } else {
            localStorage.setItem('visible', String(true));
            initWizard();
            if (width >= 992) {
                panel.addClass('visible').animate({'right': '560px'});
            } else {
                if (width < 992 && width >= 576) {
                panel.addClass('visible').animate({'right': '550px'});
                } else {
                    panel.addClass('visible').animate({'right': '320px'});
                }
            }
        }
        valid = false;
        return false;
    });
}

function wireupEvents() {
    if (!valid) {
        window.onbeforeunload = askWheatherToClose;
    }
}

function askWheatherToClose(event) {
    if (!valid) {
        clearLocalStorage();
    }
}

function setPanel() {
    var panel = $('#slide-panel');
    if (localStorage.getItem('visible') !== null) {
        if (width >= 992 ) {
            panel.addClass('visible').animate({'right': '550px'});
        } else {
            if (width < 992 && width >= 576) {
                panel.addClass('visible').animate({'right': '550px'});
            }
            else {
                panel.addClass('visible').animate({'right': '320px'});
            }
        }
        initWizard();
    }
}