window.addEventListener("load", function () {
  renderPictures(1);
  renderPaginationButtons();
  var grid = document.querySelector(".grid-container");
  var iso = new Isotope(grid, {
    itemSelector: ".grid-item",
    percentPosition: true,
    masonry: {
      columnWidth: ".grid-item",
      gutter: 10,
    },
  });
});

function renderPictures(page) {
  var startIndex = (page - 1) * picturesPerPage;
  var endIndex = startIndex + picturesPerPage;
  var pagePictures = pictureLinks.slice(startIndex, endIndex);

  var gridContainer = document.getElementById("gridContainer");
  gridContainer.innerHTML = "";

  pagePictures.forEach(function (pictureLink) {
    var gridItem = document.createElement("div");
    gridItem.classList.add("grid-item");

    var img = document.createElement("img");
    img.src = pictureLink;
    img.classList.add("images");

    var itemDetails = document.createElement("div");
    itemDetails.classList.add("item-details");

    var h3 = document.createElement("h3");
    h3.innerText = "Title";

    var p = document.createElement("p");
    p.innerText = "Date";

    itemDetails.appendChild(h3);
    itemDetails.appendChild(p);

    gridItem.appendChild(img);
    gridItem.appendChild(itemDetails);

    gridContainer.appendChild(gridItem);
  });
}
function renderPictures(page) {
  var startIndex = (page - 1) * picturesPerPage;
  var endIndex = startIndex + picturesPerPage;
  var pageItems = album.slice(startIndex, endIndex);

  var gridContainer = document.getElementById("gridContainer");
  gridContainer.innerHTML = "";

  pageItems.forEach(function (item) {
    var gridItem = document.createElement("div");
    gridItem.classList.add("grid-item");

    var img = document.createElement("img");
    img.src = item.image;
    img.classList.add("images");

    var itemDetails = document.createElement("div");
    itemDetails.classList.add("item-details");

    var h3 = document.createElement("h3");
    h3.innerText = item.title;

    var p = document.createElement("p");
    p.innerText = item.date;

    itemDetails.appendChild(h3);
    itemDetails.appendChild(p);

    gridItem.appendChild(img);
    gridItem.appendChild(itemDetails);

    gridContainer.appendChild(gridItem);
  });
}
function renderPaginationButtons() {
  var paginationContainer = document.querySelector(".pagination");
  paginationContainer.innerHTML = "";

  for (var i = 1; i <= totalPages; i++) {
    var button = document.createElement("button");
    button.innerText = i;
    button.addEventListener("click", function () {
      var page = parseInt(this.innerText);
      renderPictures(page);
    });

    paginationContainer.appendChild(button);
  }
}
