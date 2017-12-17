var orginalTopic;


function initWizard(components,sortedTopics) {
    var components = JSON.parse(components)['components'];
    //speichern der Ausgangsdaten
    orginalTopic = components;
    window.alert(JSON.parse(sortedTopics)[1])
    components.forEach(function (element) {
        //window.alert(JSON.stringify(element))
    })
}