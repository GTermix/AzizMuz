// Create the video element using jQuery
var videoElement = $('<video></video>', {
    'class': 'mfp-iframe',
    'src': 'https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_1mb.mp4',
    'frameborder': '0',
    'allowfullscreen': '',
    'controls': '',
    'controlsList': 'nodownload'
});
// Select the iframe element
var originalIframe = $('iframe.mfp-iframe');

// Create a clone of the original iframe
var clonedIframe = originalIframe.clone();

// Remove the original iframe
originalIframe.remove();

// Insert the cloned iframe back into the DOM
$('div.mfp-iframe-scaler').append(clonedIframe);
// Append the video element to its container
videoElement.appendTo('mfp-iframe');
// Select the iframe element using a jQuery selector
var iframeElement = $('.mfp-iframe').children();
iframeElement.each(function() {
    console.log($(this))
});

// Remove the iframe element
iframeElement.remove();