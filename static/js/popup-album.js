const gridItems = document.querySelectorAll(".grid-item");

gridItems.forEach((gridItem) => {
  const imageSrc = gridItem.querySelector("img").getAttribute("src");
  const title = gridItem.querySelector("h3").textContent;
  const date = gridItem.querySelector("p").textContent;

  gridItem.addEventListener("click", function () {
    const popup = document.createElement("div");
    popup.className = "popup";
    popup.innerHTML = `
      <div class="popup-content">
        <img src="${imageSrc}" alt="Popup Image" />
        <h2>${title}</h2>
        <p>${date}</p>
        <button class="close-popup">Close</button>
      </div>
    `;

    document.body.appendChild(popup);

    const closePopupButton = popup.querySelector(".close-popup");
    closePopupButton.addEventListener("click", function () {
      popup.remove();
    });
  });
});
