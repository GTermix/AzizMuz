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



// js to handle pagination in videos page
function updatePageContentEvent(links, page, index) {
  var videos = links;
  var currentPage_ = page;
  var iframes = document.querySelectorAll(".grid-container .grid-item iframe");
  for (var i = 0; i < iframes.length; i++) {
    if (videos[i]) {
      iframes[i].src = "https://www.youtube.com/embed/" + videos[i];
      iframes[i].style.display = "block"; // Show the iframe
    } else {
      iframes[i].src = "https://www.youtube.com/embed/"; // Clear the src of unused iframes
      iframes[i].style.display = "none"; // Hide the iframe
    }
  }

  var previousPage = currentPage_ - 1;
  if (previousPage >= 1) {
    a = document.querySelectorAll(".num")[0];
    a.style.display = "inline";
    if (a.classList.contains("current")) {
      a.classList.remove("current");
    }
    a.textContent = previousPage;
  } else {
    document.querySelectorAll(".num")[0].style.display = "none";
  }

  u = document.querySelectorAll(".num")[1];
  u.textContent = currentPage_;
  if (!u.classList.contains("current")) {
    u.classList.add("current");
    u.style.display = "inline";
  }

  var nextPage = currentPage_ + 1;
  if (nextPage <= totalPages) {
    a = document.querySelectorAll(".num")[2];
    a.style.display = "inline";
    if (a.classList.contains("current")) {
      a.classList.remove("current");
    }
    document.querySelectorAll(".num")[2].textContent = nextPage;
  } else {
    document.querySelectorAll(".num")[2].style.display = "none";
  }

  // Enable or disable the pagination buttons based on the current page
  document.querySelector(".pagination .previous").disabled = currentPage_ === 1;
  document.querySelector(".pagination .first").disabled = currentPage_ === 1;
  document.querySelector(".pagination .next").disabled =
    currentPage_ === totalPages || currentPage_ === 1;
  document.querySelector(".pagination .last").disabled =
    currentPage_ === totalPages || currentPage_ === 1;
}
document.querySelectorAll(".video-object").forEach((el) => {
  el.addEventListener("click", (event) => {
    let videoCode = el.getAttribute("code");
    // send request to /videos-api/data/{$videoCode} to retrieve page data
    fetch("/videos-api/data/" + videoCode)
      .then((response) => response.json())
      .then((data) => {
        links = data.links;
        page = parseInt(data.page);
        index = parseInt(data.index);
        updatePageContentEvent(links, page, index);
      });
  });
});
