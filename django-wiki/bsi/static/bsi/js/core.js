function ajaxError(){}

$.ajaxSetup({
  timeout: 7000,
  cache: false,
  error: function(e, xhr, settings, exception) {
      ajaxError();
  }
});

function jsonWrapper(url, callback) {
  $.getJSON(url, function(data) {
    if (data == null) {
      ajaxError();
    } else {
      callback(data);
    }
  });
}

$(document).ready(function() {
  var btnGroup = $("span[data-bind='bs-drp-sel-label']");
  localStorage.setItem('searchToken', btnGroup.text());

  if (localStorage.getItem(('searchTocken') !== undefined)){
      btnGroup.text(localStorage.getItem('searchToken'));
  }
  $("ul.dropdown > li > a[href='#']").click(function(){
      localStorage.setItem('searchToken', $(this).text());
  })
});