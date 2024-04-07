

// element.addEventListener("click", () => {
//         const index = Array.from(gridItems).indexOf(element);
//         $('.grid-container').magnificPopup('open', index);

// $(document).ready(()=> {
//   $(".popup-link").magnificPopup({
//     type: "image",
//     closeOnContentClick: true,
//     gallery: {
//       enabled: true,
//     },
//   });
// });

// const gridItems = document.querySelectorAll(".grid-item");

// gridItems.forEach((gridItem) => {
//   const imageSrc = gridItem.querySelector("img").getAttribute("src");
//   const title = gridItem.querySelector("h3").textContent;
//   const date = gridItem.querySelector("p").textContent;

//   gridItem.addEventListener("click", function () {
//     const popup = document.createElement("div");
//     popup.className = "popup";
//     popup.innerHTML = `
//       <div class="popup-content">
//       <div class="image-container">
//           <img src="${imageSrc}" alt="Popup Image" />
//           <div class="text-container">
//             <h2>${title}</h2>
//             <p>${date}</p>
//           </div>
//         </div>
//         <button class="close-popup">Close</button>
//       </div>
//     `;

//     document.body.appendChild(popup);

//     const closePopupButton = popup.querySelector(".close-popup");
//     closePopupButton.addEventListener("click", function () {
//       popup.remove();
//     });
//   });
// });
