// LMS PAGE

$(document).on('click', '.lms_show', function(){
    $('.accn').toggleClass('active');
    $('.lms_show').toggleClass('active');
})

$(document).on('mouseenter', '.servbtn', function() {
    $('.menudrop').show();
})

$(document).on('mouseleave', '.servbtn', function() {
    $('.menudrop').hide();
})

$(document).on('mouseenter', '.menudrop', function() {
    $('.menudrop').show();
})

$(document).on('mouseleave', '.menudrop', function() {
    $('.menudrop').hide();
})

$(document).on('mouseenter', '.md', function() {
    $(this).css("background-color", "#008080");
})

$(document).on('mouseleave', '.md', function() {
    $(this).css("background-color", "#323956");
})

$(document).on('click', '.ham', function(){
    $('.collapsemenu').toggleClass('active');
})
