$(document).on('click', '.tab', function() {
    $(this).addClass('active');
    let thisClass = $(this).attr('class').split(' ')[1];
    $('.tabdesc').hide();
    $('.' + thisClass).show();
    // $('.t1').show();
    $(this).siblings().removeClass('active');
    // $('.' + thisClass + ' .tabdesc').siblings().hide();
    
})

$(document).on('click', '.acc1', function() {
    $(this).find('.ac1p1').slideToggle().remo;
    $(this).siblings().find('.ac1p1').slideUp();
}
)

$(document).on('click', '.open', function() {
    $('.popbox').show();
    var thisimg = $(this).data('callimg');
    
})

$(document).on('click', '.closebtn', function() {
    $('.popbox').hide();
})

// $(document).on('click', '.rest', function() {
//     $('.menu').hide();
// })

$(document).on('click', '.btn', function() {
    $('.menu').toggleClass('collapsed');
})

$(document).on('click', '.pics', function() {
    $('.popimage').addClass('active');
})

$(document).on('click', '.pics', function() {
    $('.popimage').addClass('active');
    var imgSrc = $(this).attr('src');
    console.log(imgSrc);
    $('.poppic').attr("src",imgSrc);
})

$(document).on('click', '.cls', function() {
    $('.popimage').removeClass('active');
    $('.poppic').attr("src","");
})