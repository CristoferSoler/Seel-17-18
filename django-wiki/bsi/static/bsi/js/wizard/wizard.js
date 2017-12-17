
function initWizard(components) {
    var components = JSON.parse(components)['components'];
    components.forEach(function (element) {
        window.alert(JSON.stringify(element))
    })
}