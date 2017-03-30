
function seminarShow(x) {
  $('div').filter('.seminar-show').hide();
  $('div').filter('#' + x).show();
}

$(document).ready(function() {
  seminarShow('2017s1');
});
