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
  var defaultValue = "All";

  if (localStorage.getItem('searchToken')) {
    btnGroup.text(localStorage.getItem('searchToken'));
  }
  else
  {
    localStorage.setItem('searchToken', defaultValue);
  }

  $("ul.dropdown-menu > li > a[href='#']").click(function(){
      localStorage.setItem('searchToken', $(this).text());
  })
});
